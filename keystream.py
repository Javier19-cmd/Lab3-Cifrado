import itertools

def keystream(key):
    # Generando un keystream infinito
    return itertools.cycle(key)

def encrypt(plaintext, key):
    # Encriptando el texto plano
    return ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(plaintext, keystream(key)))

def decrypt(ciphertext, key):
    # Desencriptando el texto cifrado
    return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(ciphertext, keystream(key)))


key = "83b916a2fd4c7e5b6c8d1eaf29476501fc6e2b9a8d34f7e56c8d9e0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f89101112131415161718192021222324252627282930313233343536373839404142434445464748494a4b4c4d4e4f505152535455565758595a5b5c5d5e5f606162636465666768696a6b6c6d6e6f707172737475767778797a7b7c7d7e7f808182838485868788898a8b8c8d8e8f909192939495969798999a9b9c9d9e9fa0a1a2a3a4a5a6a7a8a9aaabacadaeaf"
plaintext = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus id justo eget purus aliquam venenatis sed non enim. Sed tristique fringilla risus, eget bibendum nunc. Sed ultricies fringilla arcu, eu bibendum lorem convallis at. Vivamus nec lectus semper, suscipit sapien eget, tristique velit. Integer at leo sed nisl hendrerit ultricies. Sed vitae dolor neque. Aliquam posuere sapien nec pharetra venenatis. Pellentesque nec tempor turpis. Vestibulum sit amet vestibulum felis. Suspendisse potenti. Nulla facilisi. Morbi nec nulla ac nisi ullamcorper consequat. Nullam nec feugiat eros. Fusce vehicula urna quis diam hendrerit, ac tristique nunc vestibulum. Nullam non lacinia lorem, eget laoreet odio. Mauris pretium quam at metus tincidunt, a gravida enim suscipit. Donec ac est massa."

ciphertext = encrypt(plaintext, key)
print("Texto cifrado:")
print(ciphertext)

print()
decrypted = decrypt(ciphertext, key)
print("Texto descifrado:")
print(decrypted)