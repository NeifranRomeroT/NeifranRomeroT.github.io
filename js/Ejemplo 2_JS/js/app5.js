// Aplicacion para evaluar la edad

var t;

// Capturar la entrada
t=parseInt(prompt("digite el numero entero "));

if ( t >10){
 document.write("la nota " +t+ " es aprobado <img src=img/comprobado.png height='45px'>  ");
} else {
document.write("la nota " +t+ " no es aprobado  <img src=img/bloquear.png height='45px'>");  
}