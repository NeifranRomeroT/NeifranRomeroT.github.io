"""Diseñe una App que almacene los datos de un sistema de facturacion para ello 
se deben crear la siguente listas vacias, alimentarlas y mostrarlas:
- codigo de la factura
- codigo del cliente
- nombre del cliente
- fecha de factura
- descrpcion del producto
- precio unitario
- cantidad
- total"""
#Creamos listas (vacias al comienzo)
codigo=[]
codigocliente=[]
nombrecliente=[]
fechafactura=[]
descrpcionproducto=[]
preciounitario=[]
cantidad=[]
total=[]



#definimos un tamaño para las listas
tamaño=int(input("Tamaño de lista? :"))
#Recorremos la lista hasta el tamaño definido
for i in range(tamaño):
    print("Ingrese los datos del sistema de facturacion ", i + 1)
    c=input("Codigo de la Factura: ")
    co=input("Codigo del Cliente: ")
    n=input("Nombre del CLiente: ")
    f=input("Fecha de Factura: ")
    d=input("Descripcion del Producto: ")
    p=int(input("Precio unitario: "))
    can=int(input("Cantidad: "))

    codigo.append(c)
    codigocliente.append(co)
    nombrecliente.append(n)
    fechafactura.append(f)
    descrpcionproducto.append(d)
    preciounitario.append(p)
    cantidad.append(can)
    total.append(can*p)
    
    
    #Ahora mostramos las listas
for i in range(tamaño):
    print("------------------------------------ ")
    print(">>Codigo de la Factura:", codigo[i])
    print(">>Codigo del Cliente:", codigocliente[i])
    print(">>Nombre del CLiente:", nombrecliente[i])
    print(">>Fecha de Factura:", fechafactura[i])
    print(">>Descripcion del Producto:", descrpcionproducto[i])
    print(">>Precio unitario:", preciounitario[i])
    print(">>Cantidad:", cantidad[i])
    print(">>Total:", total[i])