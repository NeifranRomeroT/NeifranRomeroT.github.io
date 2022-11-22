#for: recorrer una lista libros
libros=["Deseos encontrados" , "El psicólogo incompetente" , "Una luz de colores" , "Lo que la Oscuridad Oculta" , "Mi pequeño secreto" , "El Hijo del Alpha" , "En las redes del Amor"]

#añadimos otro elemento a la lista
libros.append("El principito")

#elimiar un elemeo de la lista
libros.pop(1)

#recorremos la listas
for x in libros:
    print(x)

#definimos la longitud
longitud=len(libros)
print("El tamaño de la lista es: ", longitud)