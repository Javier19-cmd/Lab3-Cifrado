import itertools

def keystream(key):
    # Genera un keystream infinito
    return itertools.cycle(key)

def encrypt(plaintext, key):
    # Encripta el texto plano
    return ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(plaintext, keystream(key)))

def decrypt(ciphertext, key):
    # Desencripta el texto cifrado
    return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(ciphertext, keystream(key)))


key = "password"
plaintext = "Hello, World!"
ciphertext = encrypt(plaintext, key)
print("Texto cifrado:", ciphertext)

decrypted = decrypt(ciphertext, key)
print("Texto descifrado:", decrypted)