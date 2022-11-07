

// Al seleccionar un archivo del input de archivos rellena el campo caratula del formulario

function mostrarSeleccion(){

    const muestraArchivo = document.querySelector('.caratula2');
    const selectorArchivos = document.querySelector('#caratula');
    //const output = document.querySelector('.output');
    //const fileInput = document.querySelector("#myfiles");
    
    //fileInput.addEventListener("change", () => {
    /*  for(const file of fileInput.files){
        output.value += `\n${file.name}`;
      }*/
    //});

//Si hemos seleccionado un archivo completamos el input de archivo

 if (selectorArchivos.files[0]!=""){

     muestraArchivo.value="";     
     muestraArchivo.value =selectorArchivos.files[0].name;
    
    }
}

//Si se confirma el borrado del album (valor true) se retorna el valor para proceder con la operacion
// sino se retorna false para cancelarla.  

function advertenciaBorrado(){
    let confirmaBorrado= confirm('¿Esta seguro de eliminar los datos del album?');
    print (confirmaBorrado.value);
    if (confirmaBorrado==true){
        return true;

    }else{
        return false;
    }

}

