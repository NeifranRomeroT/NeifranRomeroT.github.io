#for: recorrer una lista de lenguaje programacion
lenguaje_programacion=["JAVA" , "PHP" , "PHYTHON" , "C/C++" , "JAVASCRIPT"]

#añadimos otro elemento a la lista
lenguaje_programacion.append("OBJECTIVE-C")

#elimiar un elemeo de la lista
lenguaje_programacion.pop(1)

#recorremos la listas
for x in lenguaje_programacion:
    print(x)

#definimos la longitud
longitud=len(lenguaje_programacion)
print("El tamaño de la lista es: ", longitud)