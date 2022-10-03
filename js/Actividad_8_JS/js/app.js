function validacampos(){
    var formulario;
    formulario=document.formUser;


    if(formulario.user.value==""){
        document.getElementById("validaaUser").innerHTML="Por favor esciba su nombre de ususario";
        formulario.user.focus();
        return false;
    }else{
        document.getElementById("validaaUser").innerHTML="";
    }


    if(formulario.email.value==""){
        document.getElementById("validaEmail").innerHTML="Por favor esciba su EMAIL";
        formulario.email.focus();
        return false;
    }else{
        document.getElementById("validaEmail").innerHTML="";
    }

    if(formulario.password.value==""){
        document.getElementById("validaPassword").innerHTML="Por favor esciba su Contraseña";
        formulario.password.focus();
        return false;
    }else{
        document.getElementById("validaPassword").innerHTML="";
    }

    if(formulario.passwordC.value==""){
        document.getElementById("validaPasswordC").innerHTML="Por favor Confirme su CONTRASEÑA";
        formulario.passwordC.focus();
        return false;
    }else{
        document.getElementById("validaPasswordC").innerHTML="";
    }

    formulario.submit();

}