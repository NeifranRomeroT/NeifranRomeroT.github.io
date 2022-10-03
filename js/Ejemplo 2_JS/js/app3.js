// Aplicacion para evaluar un numero si es positivo o negativo

var numero;

// Capturar la entrada
numero=parseInt(prompt("digite el numero entero "));

if (numero>0) {
 document.write("El numero: " + numero + " Si es un numero positivo <img src=img/signo-positivo.png height='45px'>");
} else {
document.write("El numero: " + numero + "  Es un numero negativo <img src=img/signo-menos.png height='45px'>");  
}
