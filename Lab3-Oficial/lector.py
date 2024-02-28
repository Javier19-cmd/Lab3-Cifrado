def leer_imagen(ruta):
    try:
        with open(ruta, 'rb') as f:
            contenido = f.read()
            
        return contenido
    except IOError:
        print("El archivo no se pudo abrir. Puede estar corrupto o el archivo puede no existir.")

# ruta_imagen = "imagen1.png"
# contenido_imagen = leer_imagen(ruta_imagen)

# print(len(contenido_imagen))

# ruta_imagen = "imagen2.png"
# contenido_imagen = leer_imagen(ruta_imagen)
# print(len(contenido_imagen))