def texto_a_binario(texto):
    return ['{:08b}'.format(ord(c)) for c in texto]

def binario_a_texto(binario):
    return ''.join(chr(int(b, 2)) for b in binario)