#App que al ingresar el valor de compra 
#Si el valor de la compra es mayor a 100.000 mil pesos
#Entonces calcule el descuento(7%) y el total de la compra 

valor_compra=float(input("Digite el valor de la compra: "))
if valor_compra>100000: 
    descuento=valor_compra*0.07
    total=valor_compra-descuento
    print("Subtotal: ", valor_compra)
    print("Descuento: ", descuento)
    print("Total de compra: ", total)
else:
    descuento=valor_compra*0.0
    total=valor_compra-descuento
    print("Subtotal: ", valor_compra)
    print("Descuento: ", descuento)
    print("Total de compra: ", total)