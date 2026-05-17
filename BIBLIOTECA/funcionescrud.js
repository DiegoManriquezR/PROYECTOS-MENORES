let libros = JSON.parse(localStorage.getItem("libros")) || [];

// Al cargar la página
document.addEventListener("DOMContentLoaded", () => {
  renderTabla();

  const formLibro = document.getElementById("formLibro");
  if (formLibro) {
    formLibro.addEventListener("submit", guardarLibro);
    document.getElementById("buscarInput").addEventListener("input", renderTabla);
    document.getElementById("filtroGenero").addEventListener("change", renderTabla);
  }

  const formContacto = document.getElementById("formContacto");
  if (formContacto) {
    formContacto.addEventListener("submit", enviarContacto);
  }
});

// Guardar libro
function guardarLibro(e) {
  e.preventDefault();
  const id = document.getElementById("idLibro").value;
  const titulo = document.getElementById("titulo").value.trim();
  const autor = document.getElementById("autor").value.trim();
  const genero = document.getElementById("genero").value;
  const anio = parseInt(document.getElementById("anio").value);

  if (titulo.length < 3 || autor.length < 3 || !genero || anio < 1900 || anio > new Date().getFullYear()) {
    alert("Todos los campos deben ser válidos.");
    return;
  }

  if (id) {
    const index = libros.findIndex(libro => libro.id === id);
    libros[index] = { id, titulo, autor, genero, anio };
  } else {
    libros.push({ id: crypto.randomUUID(), titulo, autor, genero, anio });
  }

  localStorage.setItem("libros", JSON.stringify(libros));
  renderTabla();
  e.target.reset();
  const modal = bootstrap.Modal.getInstance(document.getElementById("modalLibro"));
  modal.hide();
}

// Mostrar libros
function renderTabla() {
  const tbody = document.getElementById("tablaLibros");
  if (!tbody) return;

  const buscar = document.getElementById("buscarInput").value.toLowerCase();
  const filtro = document.getElementById("filtroGenero").value;

  tbody.innerHTML = "";
  libros
    .filter(libro =>
      (libro.titulo.toLowerCase().includes(buscar) || libro.autor.toLowerCase().includes(buscar)) &&
      (filtro === "" || libro.genero === filtro)
    )
    .forEach(libro => {
      const tr = document.createElement("tr");
      tr.innerHTML = `
        <td>${libro.titulo}</td>
        <td>${libro.autor}</td>
        <td>${libro.genero}</td>
        <td>${libro.anio}</td>
        <td>
          <button class="btn btn-sm btn-warning me-1" onclick="editarLibro('${libro.id}')">Editar</button>
          <button class="btn btn-sm btn-danger" onclick="eliminarLibro('${libro.id}')">Eliminar</button>
        </td>
      `;
      tbody.appendChild(tr);
    });
}

// Editar libro
function editarLibro(id) {
  const libro = libros.find(libro => libro.id === id);
  document.getElementById("idLibro").value = libro.id;
  document.getElementById("titulo").value = libro.titulo;
  document.getElementById("autor").value = libro.autor;
  document.getElementById("genero").value = libro.genero;
  document.getElementById("anio").value = libro.anio;
  new bootstrap.Modal(document.getElementById("modalLibro")).show();
}

// Eliminar libro
function eliminarLibro(id) {
  if (confirm("¿Deseas eliminar este libro?")) {
    libros = libros.filter(libro => libro.id !== id);
    localStorage.setItem("libros", JSON.stringify(libros));
    renderTabla();
  }
}

// Formulario de contacto
function enviarContacto(e) {
  e.preventDefault();
  const nombre = document.getElementById("nombreContacto").value.trim();
  const email = document.getElementById("emailContacto").value.trim();
  const mensaje = document.getElementById("mensajeContacto").value.trim();

  if (nombre.length < 3 || !/^[^@]+@[^@]+\.[a-zA-Z]{2,}$/.test(email) || mensaje.length < 5) {
    alert("Por favor completa todos los campos correctamente.");
    return;
  }

  const mensajeObj = { nombre, email, mensaje, fecha: new Date().toISOString() };
  const mensajes = JSON.parse(localStorage.getItem("mensajes")) || [];
  mensajes.push(mensajeObj);
  localStorage.setItem("mensajes", JSON.stringify(mensajes));

  alert("Mensaje enviado correctamente. ¡Gracias!");
  e.target.reset();
}
