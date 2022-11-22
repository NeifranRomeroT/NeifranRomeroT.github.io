"""Diseñe una App que almacene los datos de un vehiculo, para ello debe crear 
las siguiente listas vacias, alimentarlas y mostrar por pantalla.
- marca
- modelo
- color
- combustible
- cilindraje
- precio"""

#Creamos listas (vacias al comienzo)
marca=[]
modelo=[]
color=[]
combustible=[]
cilindraje=[]
precio=[]
#definimos un tamaño para las listas
tamaño=int(input("Tamaño de lista? :"))
#Recorremos la lista hasta el tamaño definido
for i in range(tamaño):
    print("Ingrese los datos del vehiculo ", i + 1)
    m=input("Marca del Vehiculo: ")
    mo=input("Modelo del Vehiculo: ")
    c=input("Color del Vehiculo: ")
    com=input("Combustible del Vehiculo: ")
    ci=input("Cilindraje del Vehiculo: ")
    p=input("Precio del Vehiculo: ")
    marca.append(m)
    modelo.append(mo)
    color.append(c)
    combustible.append(com)
    cilindraje.append(ci)
    precio.append(p)
    print("Informacion del Vehiculo :")
#Ahora mostramos las listas
for i in range(tamaño):
    print("--------------------------------------- ")
    print(">>Marca:", marca[i])
    print(">>Modelo:", modelo[i])
    print(">>Color:", color[i])
    print(">>Combustible:", combustible[i])
    print(">>Cilindraje:", cilindraje[i])
    print(">>Precio:", precio[i])