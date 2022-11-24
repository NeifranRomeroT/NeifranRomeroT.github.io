#for: recorrer una lista frutas
frutas=["apple","banana","cherry"]

#añadimos otro elemento a la lista
frutas.append("lemon")

#elimiar un elemeo de la lista
frutas.pop(1)

#recorremos la listas
for x in frutas:
    print(x)



#definimos la longitud
longitud=len(frutas)
print("El tamaño de la lista es: ", longitud)