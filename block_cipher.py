from PIL import Image
from Crypto.Cipher import AES
import os

# Genera una clave de 16 bytes
key = os.urandom(16)

def pad(data):
    return data + b"\x00" * (16 - len(data) % 16)

def encrypt_ecb(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(data))

def encrypt_cbc(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    return cipher.encrypt(pad(data))

# Ejemplo con formato jpeg
with Image.open('foto1.jpeg') as im:
    data = im.tobytes()

# Haciendo los cifrados
encrypted_ecb_data = encrypt_ecb(data, key)
encrypted_cbc_data = encrypt_cbc(data, key)

# Resultados
with Image.frombytes('RGB', im.size, encrypted_ecb_data) as im_ecb:
    im_ecb.save('imagen_ecb.jpg')

with Image.frombytes('RGB', im.size, encrypted_cbc_data) as im_cbc:
    im_cbc.save('imagen_cbc.jpg')

# Ejemplo con formato webp
with Image.open('Logo-UVG.webp') as im:
    data1 = im.tobytes()
    
encrypted_ecb_data = encrypt_ecb(data1, key)
encrypted_cbc_data = encrypt_cbc(data1, key)

# Resultados
with Image.frombytes('RGB', im.size, encrypted_ecb_data) as im_ecb:
    im_ecb.save('imagen_ecb.webp')

with Image.frombytes('RGB', im.size, encrypted_cbc_data) as im_cbc:
    im_cbc.save('imagen_cbc.webp')

# Ejemplo con formato ppm
with Image.open('tux.ppm') as im:
    data1 = im.tobytes()
    
encrypted_ecb_data = encrypt_ecb(data1, key)
encrypted_cbc_data = encrypt_cbc(data1, key)

# Resultados
with Image.frombytes('RGB', im.size, encrypted_ecb_data) as im_ecb:
    im_ecb.save('imagen_ecb.ppm')

with Image.frombytes('RGB', im.size, encrypted_cbc_data) as im_cbc:
    im_cbc.save('imagen_cbc.ppm')

# Enseñando las imagenes de los resultados
Image.open('imagen_ecb.ppm').show()
Image.open('imagen_cbc.ppm').show()