def xor_cadenas(palabra, llave):
    
    if len (palabra) < len(llave):
        print("Las cadenas no son del mismo tamaño")
        return
    
    # Complementando la llave para llegar al mismo tamaño
    while len(llave) < len(palabra):
        llave += llave

    # Realizando la operación XOR bit a bit
    resultado = [format(int(a, 2) ^ int(b, 2), '08b') for a, b in zip(palabra, llave)]
    return resultado

# palabra = ['01001000', '01101111', '01101100']
# llave = ['01000001', '01100100', '01101001', '11110011', '01110011']

# print("Resultado: ")
# print(xor_cadenas(palabra, llave))