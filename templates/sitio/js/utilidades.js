function llenarcaratula(){
var selector=document.getElementsByName("txtcaratula").files[0];
alert(selector);
var contenedor=document.getElementsByName("txtcaratula2").innerText;
contenedor=selector;
alert(contenedor);
//


}

// 

function mostrarSeleccion(){
    //const output1 = document.getElementsByName('txtcaratula2');
    const muestraArchivo = document.querySelector('.caratula2');
    const selectorArchivos = document.querySelector('#caratula');
    //const output = document.querySelector('.output');
    //const fileInput = document.querySelector("#myfiles");
    
    //fileInput.addEventListener("change", () => {
    /*  for(const file of fileInput.files){
        output.value += `\n${file.name}`;
      }*/
    //});
 muestraArchivo.value="";     
 muestraArchivo.value += `\n${selectorArchivos.files[0].name}`;


}