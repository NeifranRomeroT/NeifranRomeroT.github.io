var peso,estatura,imc

peso=parseFloat(prompt("Digite el peso en Kg:"))

estatura=parseFloat(prompt("Digite la estatura en Mts:"))
//Proceso--Calculamos

imc=peso/(estatura*estatura)

if (imc <18.5) {

    document.write("Tu peso esta Bajo <img src='img/bajo de peso.png'heith='50px'>El término peso bajo se refiere a un humano cuyo peso se encuentra por debajo de un valor saludable. En general la definición se refiere al índice de masa corporal (IMC). Un IMC inferior a 18.5 es por lo general identificado como un peso bajo.");
    
    

}else if (imc>=18.5 && imc<=24.9) {

    document.write("Tu Peso es Normal <img src='img/normal.png'heith='50px'>Se considera un peso saludable aquel que nos permite mantenernos en un buen estado de salud y calidad de vida. También se entiende como los valores de peso, dentro de los cuales, no existe riesgo para la salud de la persona.");
    
    

}else if (imc>=25 && imc<=29.9) {

    document.write("Estas en Sobrepeso <img src='img/sobre peso.png'heith='50px'>El sobrepeso es el aumento de peso corporal por encima de un patrón dado y para evaluar si una persona presenta sobrepeso, los expertos emplean una fórmula llamada índice de masa corporal (IMC), que calcula el nivel de grasa corporal en relación con el peso y estatura.");
    
    
    
}else if (imc>=30 && imc<=34.9) {

    document.write(" Estas en Obesidad I <img src='img/obesidad 1.png'heith='50px'> La obesidad es una enfermedad crónica que se caracteriza por la acumulación excesiva del tejido adiposo en el cuerpo  es decir, cuando la reserva natural de energía de los seres humanos y de otros animales mamíferos almacenada en forma de grasa corporal se incrementa hasta un punto en que pone en riesgo la salud o la vida. ");
 

}else if (imc>=35 && imc<=39.9) {

    document.write("Estas en Obesidad II<img src='img/obesidad 2.png'heith='50px'> La obesidad es una enfermedad crónica que se caracteriza por la acumulación excesiva del tejido adiposo en el cuerpo  es decir, cuando la reserva natural de energía de los seres humanos y de otros animales mamíferos almacenada en forma de grasa corporal se incrementa hasta un punto en que pone en riesgo la salud o la vida. ");
   

}else if (imc>=40 && imc<=49.9) {

    document.write("Estas en Obesidad III <img src='img/obesidad 3.png'heith='50px'> La obesidad es una enfermedad crónica que se caracteriza por la acumulación excesiva del tejido adiposo en el cuerpo  es decir, cuando la reserva natural de energía de los seres humanos y de otros animales mamíferos almacenada en forma de grasa corporal se incrementa hasta un punto en que pone en riesgo la salud o la vida. ");


}else if (imc>=50) {

    document.write("Estas en Obesidad IV <img src='img/obesidad 4.png 'heith='50px'>La obesidad es una enfermedad crónica que se caracteriza por la acumulación excesiva del tejido adiposo en el cuerpo  es decir, cuando la reserva natural de energía de los seres humanos y de otros animales mamíferos almacenada en forma de grasa corporal se incrementa hasta un punto en que pone en riesgo la salud o la vida. ");

   
}else{

     document.write("Escriba los valores numericos esperado.....")

}    
        