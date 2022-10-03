// Aplicacion para evaluar un nota si es aprobado o no aprobado

var t;

// Capturar la entrada
t=parseInt(prompt("digite el numero entero "));

if ( t >=3){
 document.write("la nota " +t+ " es aprobado <img src=img/comprobado.png height='45px'> ");
} else {
document.write("la nota " +t+ " no es aprobado <img src=img/bloquear.png height='45px'>");  
}