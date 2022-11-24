"""Diseñar una App que resiva una lista vacia; dicha lista el usuario define su tamaño y los valores de cada elmento
la App debe mostrar
-los valores de la lista actualizada"""

#Creamos listas (vacias al comienzo)
nombres=[]
identificacion=[]
correo=[]
telefono=[]
direccion=[]
nacimiento=[]
lugarnacimiento=[]
#definimos un tamaño para las listas
#lo puedes cambiar si quieres
tamaño=int(input("Tamaño de lista? :"))
#Recorremos la lista hasta el tamaño definido
for i in range(tamaño):
    print("Ingrese los datos del aprendiz ", i + 1)
    nombre=input("Nombre del aprendiz: ")
    id=input("N° de Identificacion: ")
    c=input("Ingresar Correo: ")
    celular=input("Numero de Telefono: ")
    d=input("Ingresar Direccion: ")
    n=input("Fecha de Nacimiento: ")
    ln=input("Lugar de Nacimiento:  ")
    nombres.append(nombre)
    identificacion.append(id)
    correo.append(c)
    telefono.append(celular)
    direccion.append(d)
    nacimiento.append(n)
    lugarnacimiento.append(ln)
print("Informacion del aprendiz :")
#Ahora mostramos las listas
for i in range(tamaño):
    print("--------------------------------------- ")
    print(">>Nombre:", nombres[i])
    print(">>Identificacion: ", identificacion[i])
    print(">>correo:", correo[i])
    print(">>N° de Celular:", telefono[i])
    print(">>Direccion:", direccion[i])
    print(">>Fecha de Nacimiento:", nacimiento[i])
    print(">>Lugar de Nacimiento:", lugarnacimiento[i])

   