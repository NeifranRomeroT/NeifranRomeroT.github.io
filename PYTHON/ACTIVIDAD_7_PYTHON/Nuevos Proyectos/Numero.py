#	Diseñar una App que, al ingresar un nuero entero 
# positivo, muestre por pantalla todos los números impares, desde 1 hasta el numero ingresado, separado por comas.   

x=int(input("Digite un numero:"))

for i in  range(1,x+1,2):
    print (i)