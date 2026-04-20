# Supondo que você tenha o arquivo brute.txt com as 100 senhas
with open('/home/raf75/sexto-periodo/cibersecurity/Brute Force/brute1.txt', 'r') as f:
    senhas_carlos = [l.strip() for l in f]

print("--- COPIE PARA O PAYLOAD SET 1 (Users) ---")
for _ in senhas_carlos:
    print("wiener\ncarlos")

print("\n--- COPIE PARA O PAYLOAD SET 2 (Passwords) ---")
for s in senhas_carlos:
    print(f"peter\n{s}")