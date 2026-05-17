const formulario = document.getElementById('formulario');
const alerta = document.getElementById('alerta');
const tabla = document.getElementById('tabla-productos')
const modal = new bootstrap.Modal(document.getElementById('modalProductos'));// Inicializar el modal

//escuchar el evento de inicio dle modal
formulario.addEventListener('submit', (e) =>{
    const nombre = document.getElementById('nombre').value;
    const precio = document.getElementById('precio').value;
    const formulario = document.getElementById('formulario').value;
    const categoria = document.getElementById('categoria').value;
    const descripcion = document.getElementById('descripcion').value;
    const filaEditando = document.getElementById('filaEditando').value;

    // validar los datos
    if(!validarFormulario(nombre,precio,categoria,descripcion)){
        alert.classList.remove('d-none'); //mostrar la alerta si los datos no son vaslidos
    }

    alerta.classList.add('d-none'); //ocultar la alerta si los datos son validos

    //verificar si esamos agregando o editando
    if(filaEditando){
        //actualizar el producto
        editarFila(filaEditando, nombre, precio, categoria, descripcion);
    }else{
        //agregar producto
        agregarFila(nombre, precio, categoria, descripcion);
    }

    //resetear formulario
    formulario.reset();
    document.getElementById('filaEditando').value = "";
    modal.hide(); //cerrar el modal
});



function validarFormulario(nombre, precio, categoria, descripcion){
    //validar que los campios no esten vacios
    return nombre.length >= 3 && precio.length >= 0 && categoria.length !== "" && descripcion.length !=="";
}

function agregarFila(nombre, precio, categoria, descripcion){
    const fila = document.createElement('tr');
    const id = Date.now(); //generar un id unicvo para cada fila.
    fila.setAttribute('data-id', id); //asignar el id a la fila

    fila.innerHTML = `
         <td>${nombre}</td>
         <td>${precio}</td>
         <td>${categoria}</td>
         <td>${descripcion}</td>
         <td>
            <button class="btn btn-sm btn-warning me-1" onclick="cargarEdicion(${id})">Editar</button>
            <button class="btn btn-sm btn-danger" onclick="eliminarFila(${id})">Eliminar</button>
        </td>
     `
     tabla.appendChild(fila);
}

function abrirFormulario(){
    formulario.reset();
    alerta.classList.add('d-none');
    document.getElementById('filaEditando').value = ""; //limpiar el input oculto que contiene el id de la fila a editar.
}