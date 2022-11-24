"""Diseñe una App que almacene los datos de una tienda de peliculas,
para ello debe crear las siguientes listas vacias:
-  de la pelicula
- genero de la pelicula
- duracion de la pelicula
- protagonista
- año de estreno
- precio de la pelicula
- idioma
"""
#Creamos listas (vacias al comienzo)
titulo=[]
genero=[]
duracion=[]
protagonista=[]
estreno=[]
precio=[]
idioma=[]
#definimos un tamaño para las listas
tamaño=int(input("Tamaño de lista? :"))
#Recorremos la lista hasta el tamaño definido
for i in range(tamaño):
    print("Ingrese los datos de la pelicula ", i + 1)
    t=input("Titulo de la Pelicula: ")
    g=input("Genero de la Pelicula: ")
    d=input("Duracion de la Pelicula: ")
    p=input("Protagonista de la Pelicula: ")
    e=input("Estreno de la Pelicula: ")
    pr=input("Precio de la Pelicula: ")
    i=input("Idioma de la Pelicula: ")
    
    titulo.append(t)
    genero.append(g)
    duracion.append(d)
    protagonista.append(p)
    estreno.append(e)
    precio.append(pr)
    idioma.append(i)
    #Ahora mostramos las listas
for i in range(tamaño):
    print("------------------------------------ ")
    print(">>Titulo:", titulo[i])
    print(">>Genero:", genero[i])
    print(">>Duracion:", duracion[i])
    print(">>Protagonista:", protagonista[i])
    print(">>Estreno:", estreno[i])
    print(">>Precio:", precio[i])
    print(">>Idioma:", idioma[i])