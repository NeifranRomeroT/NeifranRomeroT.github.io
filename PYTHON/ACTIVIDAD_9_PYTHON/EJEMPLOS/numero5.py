#for: recorrer una lista de colotes
colores=["AZUL" , "ROJO" , "AMARILLO" , "VERDE" , "CAFE" , "NEGRO" , "BLANCO" , "MORADO"]

#añadimos otro elemento a la lista
colores.append("ROSADO")

#elimiar un elemeo de la lista
colores.pop(1)

#recorremos la listas
for x in colores:
    print(x)

#definimos la longitud
longitud=len(colores)
print("El tamaño de la lista es: ", longitud)
