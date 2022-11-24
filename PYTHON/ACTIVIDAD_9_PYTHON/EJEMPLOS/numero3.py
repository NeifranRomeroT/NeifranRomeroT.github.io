#for: recorrer una lista plantas medicinales
plantas_medicinales=["Aloe vera" , "Valeriana" , "Alcachofa" , "Amapola" , "Eucalipto" , "Ginkgo" , "Lavanda" , "Tomillo" , "Espliego"]

#añadimos otro elemento a la lista
plantas_medicinales.append("Oregano")

#elimiar un elemeo de la lista
plantas_medicinales.pop(1)


#recorremos la listas
for x in plantas_medicinales:
    print(x)

#definimos la longitud
longitud=len(plantas_medicinales)
print("El tamaño de la lista es: ", longitud)