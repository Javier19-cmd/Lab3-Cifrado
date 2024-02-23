from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from PIL import Image
import io
import numpy as np

with Image.open('foto1.jpeg') as img:
    byte_arr = io.BytesIO()
    img.save(byte_arr, format='JPEG')
    img_bytes = byte_arr.getvalue()

# Definiendo la clave y el vector de inicialización (IV)
clave = b'clavede16bytess_'
iv = b'iv_de_16_bytes__'

# Creando el objeto de cifrado para cifrar
cipher_ecb_encrypt = AES.new(clave, AES.MODE_ECB)
cipher_cbc_encrypt = AES.new(clave, AES.MODE_CBC, iv)

# Cifrando la imagen
img_cifrada_ecb = cipher_ecb_encrypt.encrypt(pad(img_bytes, AES.block_size))
img_cifrada_cbc = cipher_cbc_encrypt.encrypt(pad(img_bytes, AES.block_size))

    
# Creando un nuevo objeto de cifrado para descifrar
cipher_ecb_decrypt = AES.new(clave, AES.MODE_ECB)
cipher_cbc_decrypt = AES.new(clave, AES.MODE_CBC, iv)

# Convirtiendo los bytes descifrados a una imagen
img_descifrada_ecb = unpad(cipher_ecb_decrypt.decrypt(img_cifrada_ecb), AES.block_size)
img_descifrada_cbc = unpad(cipher_cbc_decrypt.decrypt(img_cifrada_cbc), AES.block_size)

# Y luego convertir los bytes descifrados de nuevo a una imagen
img_ecb = Image.open(io.BytesIO(img_descifrada_ecb))
img_cbc = Image.open(io.BytesIO(img_descifrada_cbc))

img_ecb.show()
img_cbc.show()

############################################################################################################
with Image.open('Logo-UVG.webp') as img: 
    byte_arr = io.BytesIO()
    img.save(byte_arr, format='WEBP')  # Cambia 'JPEG' a 'WEBP'
    img_bytes = byte_arr.getvalue()

# Definiendo la clave y el vector de inicialización (IV)
clave = b'clavede16bytess_'
iv = b'iv_de_16_bytes__'

# Creando el objeto de cifrado para cifrar
cipher_ecb_encrypt = AES.new(clave, AES.MODE_ECB)
cipher_cbc_encrypt = AES.new(clave, AES.MODE_CBC, iv)

# Cifrando la imagen
img_cifrada_ecb = cipher_ecb_encrypt.encrypt(pad(img_bytes, AES.block_size))
img_cifrada_cbc = cipher_cbc_encrypt.encrypt(pad(img_bytes, AES.block_size))

# Creando un nuevo objeto de cifrado para descifrar
cipher_ecb_decrypt = AES.new(clave, AES.MODE_ECB)
cipher_cbc_decrypt = AES.new(clave, AES.MODE_CBC, iv)

# Descifrando la imagen
img_descifrada_ecb = unpad(cipher_ecb_decrypt.decrypt(img_cifrada_ecb), AES.block_size)
img_descifrada_cbc = unpad(cipher_cbc_decrypt.decrypt(img_cifrada_cbc), AES.block_size)

# Convirtiendo los bytes descifrados a una imagen
img_ecb = Image.open(io.BytesIO(img_descifrada_ecb))
img_cbc = Image.open(io.BytesIO(img_descifrada_cbc))


img_ecb.save('img_descifrada_ecb.webp', 'WEBP')
img_cbc.save('img_descifrada_cbc.webp', 'WEBP')  

img_ecb.show()
img_cbc.show()

############################################################################################################

with Image.open('tux.ppm') as img:
    byte_arr = io.BytesIO()
    img.save(byte_arr, format='PPM')  # Cambia 'JPEG' a 'PPM'
    img_bytes = byte_arr.getvalue()

# Definiendo la clave y el vector de inicialización (IV)
clave = b'clavede16bytess_' 
iv = b'iv_de_16_bytes__'

# Creando el objeto de cifrado para cifrar
cipher_ecb_encrypt = AES.new(clave, AES.MODE_ECB)
cipher_cbc_encrypt = AES.new(clave, AES.MODE_CBC, iv)

# Cifrando la imagen
img_cifrada_ecb = cipher_ecb_encrypt.encrypt(pad(img_bytes, AES.block_size))
img_cifrada_cbc = cipher_cbc_encrypt.encrypt(pad(img_bytes, AES.block_size))

# Creando un nuevo objeto de cifrado para descifrar
cipher_ecb_decrypt = AES.new(clave, AES.MODE_ECB)
cipher_cbc_decrypt = AES.new(clave, AES.MODE_CBC, iv)

# Descifrando la imagen
img_descifrada_ecb = unpad(cipher_ecb_decrypt.decrypt(img_cifrada_ecb), AES.block_size)
img_descifrada_cbc = unpad(cipher_cbc_decrypt.decrypt(img_cifrada_cbc), AES.block_size)

img_ecb = Image.open(io.BytesIO(img_descifrada_ecb))
img_cbc = Image.open(io.BytesIO(img_descifrada_cbc))

img_ecb.save('img_descifrada_ecb.ppm', 'PPM')
img_cbc.save('img_descifrada_cbc.ppm', 'PPM')

img_ecb.show()
img_cbc.show()