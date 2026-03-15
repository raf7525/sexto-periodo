import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def criptografia_secreta():
    chave = AESGCM.generate_key(bit_length=256)

    aesgcm = AESGCM(chave)
    texto = b"CESAR School"
    nonce = os.urandom(12)
    aad = b"nao sei oque eh mas dava errado sem"
    texto_cripto_tag = aesgcm.encrypt(nonce,texto,aad)
    print("--- Processo de Criptografia ---")
    print(f"Texto Claro Original: {texto.decode()}")
    print(f"Nonce (Hex): {nonce.hex()}")
    print(f"Cifrado + Tag (Hex): {texto_cripto_tag.hex()}")

    try:
        texto_descriptografado = aesgcm.decrypt(nonce,texto_cripto_tag, aad)
        
        print("\n--- Processo de Descriptografia ---")
        print("Sucesso! Integridade confirmada e dados descriptografados:")
        print(texto_descriptografado.decode())
    except Exception as e:
        print("\nFalha na descriptografia! Os dados ou a Tag foram adulterados.")

if __name__ == "__main__":
    criptografia_secreta()
    