from Crypto.Cipher import DES, DES3, AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Generando la clave
clave = get_random_bytes(8) # DES necesita una clave de 8 bytes

# Creando del cifrado DES
cifrado = DES.new(clave, DES.MODE_ECB)

mensaje = b'Universidad'

# Cifrando del mensaje
mensaje_cifrado = cifrado.encrypt(pad(mensaje, DES.block_size))

print("Mensaje cifrado con DES:", mensaje_cifrado)

# Descifrado del mensaje
mensaje_descifrado = unpad(cifrado.decrypt(mensaje_cifrado), DES.block_size)

print("Mensaje descifrado con DES:", mensaje_descifrado)

# Generando la clave
clave = get_random_bytes(24) # 3DES necesita una clave de 24 bytes

# Creando del cifrado 3DES
cifrado = DES3.new(clave, DES3.MODE_ECB)

mensaje = b'Universidad'

# Cifrado del mensaje
mensaje_cifrado = cifrado.encrypt(pad(mensaje, DES3.block_size))

print("Mensaje cifrado con DES3:", mensaje_cifrado)

# Descifrado del mensaje
mensaje_descifrado = unpad(cifrado.decrypt(mensaje_cifrado), DES3.block_size)

print("Mensaje descifrado con DES3:", mensaje_descifrado)

# Generación de la clave
clave = get_random_bytes(32) # AES necesita una clave de 16, 24 o 32 bytes

# Creación del cifrado AES
cifrado = AES.new(clave, AES.MODE_ECB)

# Mensaje que se va a cifrar
mensaje = b'Hola Mundo!'

# Cifrado del mensaje
mensaje_cifrado = cifrado.encrypt(pad(mensaje, AES.block_size))

print("Mensaje cifrado con AES:", mensaje_cifrado)

# Descifrado del mensaje
mensaje_descifrado = unpad(cifrado.decrypt(mensaje_cifrado), AES.block_size)

print("Mensaje descifrado con AES:", mensaje_descifrado)