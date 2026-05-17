function mostrarAlerta(){
    const alerta = `<div class="alert alert-danger" role="alert">
    A simple danger alert—check it out!
    </div>`;
    document.getElementById("mostrar-alerta").innerHTML = alerta;
}

function validarFormulario(){
    let nombre = document.getElementById("nombre").value;
    let correo = document.getElementById("correo").value;

    if(nombre === "" || correo === ""){
        alert('Por favor completa todos los datos');

    }else{
        alert('Datos enviados. Don: ' + nombre + ' correo: ' + correo);
    }
}

function abrirModal(){
    const modal = new bootstrap.Modal(document.getElementById('miModal'));
    modal.show();
}

function contenido(){
    const div = document.getElementById("textoOculto");
    div.style.display = (div.style.display === "none") ? "block" : "none";

}