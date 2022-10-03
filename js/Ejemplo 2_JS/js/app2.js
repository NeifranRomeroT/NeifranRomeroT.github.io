//App para evaluar un numero entre 10 y 100

var n;

// Capturar la entrada
n=parseInt(prompt("Digite el numero entero:"));

// Evaluamos el proceso numerico

if ( n>=10 && n<=100) {

 document.write("El numero: " + n + " Si esta entre 10 y 100  <img src=img/es-igual-o-mayor-que-el-simbolo.png height='45px'"); 
} else {
document.write("El numero: " + n + " No esta entre 10 y 100  <img src='img/es-menor-o-igual-que-un-simbolo-matematico.png' height='45px'");
 
}
