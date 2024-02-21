import random
from xor_cadenas import *
from binarios import *

def generar_keystream(longitud):
    keystream = ''
    for _ in range(longitud):
        keystream += chr(random.randint(0, 255))
    return keystream

def cifrar_mensaje(mensaje, keystream):
    mensaje_binario = texto_a_binario(mensaje)
    keystream_binario = texto_a_binario(keystream)
    return xor_cadenas(mensaje_binario, keystream_binario)


def descifrar_mensaje(mensaje_cifrado, keystream):
    keystream_binario = texto_a_binario(keystream)
    mensaje_descifrado_binario = xor_cadenas(mensaje_cifrado, keystream_binario)
    return binario_a_texto(mensaje_descifrado_binario)


# Uso de la función de encriptado
mensaje = "Hola mundo"
keystream = generar_keystream(len(mensaje))

print("Keystream: ")
print(keystream)

mensaje_cifrado = cifrar_mensaje(mensaje, keystream)
print(mensaje_cifrado)

# Uso de la función para decriptar.
mensaje_descifrado = descifrar_mensaje(mensaje_cifrado, keystream)
print(mensaje_descifrado)