//Aplicacion Para Evaluar la Fiebre de una Persona

var temp;

//Capturar los datos de entrada 
temp=parseFloat(prompt("Ingrese su temperatura en °C:"));

//Proceso para evaluar la Fiebre

if (temp >=38) {
document.write("La temperatura " +temp+ " °C Indica paciente con Fiebre  <img src='img/fiebre2.png'height='45px'>");

} else {
document.write("La temperatura " +temp+ " °C Indica paciente  sin Fiebre   <img src='img/fiebre3.png'height='45px'>");  
}   