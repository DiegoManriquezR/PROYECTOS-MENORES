function marcarNavActivo() {
  const path = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('nav a').forEach(link => {
    link.classList.toggle('active', link.getAttribute('href') === path);
  });
}

function iniciarCuentaRegresiva(fechaEventoISO, idElemento) {
  const cuenta = document.getElementById(idElemento);
  if (!cuenta) return;
  const fechaEvento = new Date(fechaEventoISO).getTime();

  const timer = setInterval(() => {
    const ahora = Date.now();
    const diff = fechaEvento - ahora;
    if (diff < 0) {
      clearInterval(timer);
      cuenta.textContent = '¡El evento ha comenzado!';
      return;
    }
    const d = Math.floor(diff / (1000 * 60 * 60 * 24));
    const h = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const m = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    const s = Math.floor((diff % (1000 * 60)) / 1000);
    cuenta.textContent = `${d}d ${h}h ${m}m ${s}s`;
  }, 1000);
}

function filtrarGaleria(categoria) {
  document.querySelectorAll('.galeria-foto').forEach(img => {
    img.style.display = categoria === 'todos' || img.dataset.categoria === categoria ? 'block' : 'none';
  });
}

function iniciarComentarios() {
  const form = document.getElementById('form-comentario');
  const lista = document.getElementById('lista-comentarios');
  if (!form || !lista) return;

  let comentarios = JSON.parse(localStorage.getItem('comentarios')) || [];

  function mostrar() {
    lista.innerHTML = '';
    comentarios.forEach(c => {
      const li = document.createElement('li');
      li.className = 'mb-3 p-3 bg-black neon-border rounded';
      li.innerHTML = `
        <p>${c.texto}</p>
        <button class="btn btn-sm btn-outline-success me-2" onclick="votarComentario(${c.id}, 1)">👍</button>
        <button class="btn btn-sm btn-outline-danger me-2" onclick="votarComentario(${c.id}, -1)">👎</button>
        <span>Puntuación: ${c.votos}</span>
      `;
      lista.appendChild(li);
    });
  }

  window.votarComentario = function (id, valor) {
    const votosUsuario = JSON.parse(localStorage.getItem('votosUsuario')) || {};
    if (votosUsuario[id]) {
      alert('Ya has votado este comentario.');
      return;
    }
    const c = comentarios.find(c => c.id === id);
    if (!c) return;
    c.votos += valor;
    if (c.votos < 0) c.votos = 0;
    votosUsuario[id] = true;
    localStorage.setItem('votosUsuario', JSON.stringify(votosUsuario));
    localStorage.setItem('comentarios', JSON.stringify(comentarios));
    mostrar();
  };

  form.addEventListener('submit', e => {
    e.preventDefault();
    const texto = form.elements['comentario'].value.trim();
    if (!texto) return alert('Comentario vacío');
    comentarios.push({ id: Date.now(), texto, votos: 0 });
    localStorage.setItem('comentarios', JSON.stringify(comentarios));
    form.reset();
    mostrar();
  });

  mostrar();
}

function validarReserva() {
  const forms = document.querySelectorAll('.form-reserva');
  forms.forEach(form => {
    form.addEventListener('submit', e => {
      e.preventDefault();
      if (!form.checkValidity()) {
        form.classList.add('was-validated');
        return;
      }
      let reservas = JSON.parse(localStorage.getItem('reservas')) || [];
      const reserva = {
        id: Date.now(),
        nombre: form.nombre.value.trim(),
        email: form.email.value.trim(),
        evento: form.getAttribute('data-evento') || 'Evento desconocido',
        entradas: form.personas.value.trim()
      };
      reservas.push(reserva);
      localStorage.setItem('reservas', JSON.stringify(reservas));
      alert(`Reserva confirmada para "${reserva.evento}"\nNombre: ${reserva.nombre}\nCorreo: ${reserva.email}\nEntradas: ${reserva.entradas}`);
      form.reset();
      form.classList.remove('was-validated');
      const collapseEl = form.closest('.collapse');
      if (collapseEl) {
        const bsCollapse = bootstrap.Collapse.getInstance(collapseEl);
        if (bsCollapse) bsCollapse.hide();
      }
    });
  });
}

function manejarAuth() {
  const formLogin = document.getElementById('form-login');
  const formRegistro = document.getElementById('form-registro');

  if (formRegistro) {
    formRegistro.addEventListener('submit', e => {
      e.preventDefault();
      const usuarios = JSON.parse(localStorage.getItem('usuarios')) || [];
      const email = formRegistro.email.value.trim();
      const pass = formRegistro.password.value;
      const pass2 = formRegistro.password2.value;
      if (pass !== pass2) return alert('Contraseñas no coinciden');
      if (usuarios.some(u => u.email === email)) return alert('Usuario ya existe');
      usuarios.push({ email, password: pass });
      localStorage.setItem('usuarios', JSON.stringify(usuarios));
      alert('Registro exitoso');
      formRegistro.reset();
    });
  }

  if (formLogin) {
    formLogin.addEventListener('submit', e => {
      e.preventDefault();
      const usuarios = JSON.parse(localStorage.getItem('usuarios')) || [];
      const email = formLogin.email.value.trim();
      const pass = formLogin.password.value;
      const usuario = usuarios.find(u => u.email === email && u.password === pass);
      if (!usuario) return alert('Usuario o contraseña incorrecta');
      alert('Login exitoso, bienvenido!');
      formLogin.reset();
    });
  }
}

function abrirModal(idModal) {
  const modal = document.getElementById(idModal);
  if (modal) modal.style.display = 'block';
}

function cerrarModal(idModal) {
  const modal = document.getElementById(idModal);
  if (modal) modal.style.display = 'none';
}

window.addEventListener('click', e => {
  document.querySelectorAll('.modal').forEach(modal => {
    if (e.target === modal) modal.style.display = 'none';
  });
});

document.addEventListener('DOMContentLoaded', () => {
  inicializarComentarios();
  inicializarBotonMute();
  marcarNavActivo();
});

function marcarNavActivo() {
  const path = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('nav a').forEach(link => {
    link.classList.toggle('active', link.getAttribute('href') === path);
  });
}

function inicializarBotonMute() {
  const btnMute = document.getElementById('btn-mute');
  const musica = document.getElementById('musica-fondo');

  if (!btnMute || !musica) return;

  btnMute.addEventListener('click', () => {
    musica.muted = !musica.muted;
    btnMute.textContent = musica.muted ? '🔇' : '🔊';
  });
}

function inicializarComentarios() {
  const formularios = document.querySelectorAll('.form-comentario');

  formularios.forEach(form => {
    const articuloId = form.dataset.articulo;
    if (!articuloId) return;

    const listaComentarios = form.nextElementSibling;
    if (!listaComentarios || !listaComentarios.classList.contains('lista-comentarios')) return;

    let comentarios = JSON.parse(localStorage.getItem(`comentarios_${articuloId}`)) || [];

    function mostrarComentarios() {
      listaComentarios.innerHTML = '';
      comentarios.forEach(c => {
        const li = document.createElement('li');
        li.className = 'mb-3 p-3 bg-black neon-border rounded';
        li.innerHTML = `
          <p>${c.texto}</p>
          <button class="btn btn-sm btn-outline-success me-2" onclick="votarComentario('${articuloId}', ${c.id}, 1)">👍</button>
          <button class="btn btn-sm btn-outline-danger me-2" onclick="votarComentario('${articuloId}', ${c.id}, -1)">👎</button>
          <span>Puntuación: ${c.votos}</span>
        `;
        listaComentarios.appendChild(li);
      });
    }

    form.addEventListener('submit', e => {
      e.preventDefault();
      const texto = form.elements['comentario'].value.trim();
      if (!texto) {
        alert('Comentario vacío');
        return;
      }
      comentarios.push({ id: Date.now(), texto, votos: 0 });
      localStorage.setItem(`comentarios_${articuloId}`, JSON.stringify(comentarios));
      form.reset();
      mostrarComentarios();
    });

    mostrarComentarios();
  });
}

window.votarComentario = function(articuloId, comentarioId, valor) {
  const comentariosKey = `comentarios_${articuloId}`;
  const votosUsuarioKey = `votosUsuario_${articuloId}`;

  let comentarios = JSON.parse(localStorage.getItem(comentariosKey)) || [];
  let votosUsuario = JSON.parse(localStorage.getItem(votosUsuarioKey)) || {};

  if (votosUsuario[comentarioId]) {
    alert('Ya has votado este comentario.');
    return;
  }

  const comentario = comentarios.find(c => c.id === comentarioId);
  if (!comentario) return;

  comentario.votos += valor;
  if (comentario.votos < 0) comentario.votos = 0;

  votosUsuario[comentarioId] = true;

  localStorage.setItem(comentariosKey, JSON.stringify(comentarios));
  localStorage.setItem(votosUsuarioKey, JSON.stringify(votosUsuario));

  const form = document.querySelector(`.form-comentario[data-articulo="${articuloId}"]`);
  if (!form) return;
  const listaComentarios = form.nextElementSibling;
  if (!listaComentarios) return;

  listaComentarios.innerHTML = '';
  comentarios.forEach(c => {
    const li = document.createElement('li');
    li.className = 'mb-3 p-3 bg-black neon-border rounded';
    li.innerHTML = `
      <p>${c.texto}</p>
      <button class="btn btn-sm btn-outline-success me-2" onclick="votarComentario('${articuloId}', ${c.id}, 1)">👍</button>
      <button class="btn btn-sm btn-outline-danger me-2" onclick="votarComentario('${articuloId}', ${c.id}, -1)">👎</button>
      <span>Puntuación: ${c.votos}</span>
    `;
    listaComentarios.appendChild(li);
  });
};

function iniciarCuentaRegresiva(id, fechaEventoISO) {
  const cuenta = document.getElementById(id);
  if (!cuenta) return;
  const fechaEvento = new Date(fechaEventoISO).getTime();

  const timer = setInterval(() => {
    const ahora = Date.now();
    const diff = fechaEvento - ahora;
    if (diff < 0) {
      clearInterval(timer);
      cuenta.textContent = '¡El evento ha comenzado!';
      return;
    }
    const d = Math.floor(diff / (1000 * 60 * 60 * 24));
    const h = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const m = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    const s = Math.floor((diff % (1000 * 60)) / 1000);
    cuenta.textContent = `${d}d ${h}h ${m}m ${s}s`;
  }, 1000);
}

document.addEventListener('DOMContentLoaded', () => {
  iniciarCuentaRegresiva('countdown1', '2025-08-15T21:00:00');
  iniciarCuentaRegresiva('countdown2', '2025-08-28T22:00:00');
  iniciarCuentaRegresiva('countdown3', '2025-09-10T20:00:00');
  iniciarCuentaRegresiva('countdown4', '2025-09-25T22:30:00');
});

document.querySelectorAll('.img-click').forEach(img => {
  img.addEventListener('click', () => {
    const modalImg = document.getElementById('imagenAmpliada');
    modalImg.src = img.src;
    const modal = new bootstrap.Modal(document.getElementById('modalImagen'));
    modal.show();
  });
});

document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const filtro = btn.dataset.filter.toLowerCase();
    document.querySelectorAll('.galeria-item').forEach(item => {
      const categoria = item.dataset.categoria.toLowerCase();
      if (filtro === 'todos' || categoria.includes(filtro)) {
        item.style.display = 'block';
      } else {
        item.style.display = 'none';
      }
    });
  });
});

document.addEventListener('DOMContentLoaded', () => {
  const forms = document.querySelectorAll('.needs-validation');
  const usuarioActivoDiv = document.getElementById('usuario-activo');
  const nombreUsuarioSpan = document.getElementById('nombre-usuario');
  const btnLogout = document.getElementById('btn-logout');

  
  const usuarioActivoJSON = localStorage.getItem('usuarioActivo');
  if (usuarioActivoJSON && usuarioActivoDiv && nombreUsuarioSpan) {
    const usuarioActivo = JSON.parse(usuarioActivoJSON);
    mostrarUsuario(usuarioActivo.nombre);
    ocultarFormularios();
  }

  
  function obtenerUsuarios() {
    const usuariosJSON = localStorage.getItem('usuariosRegistrados');
    return usuariosJSON ? JSON.parse(usuariosJSON) : [];
  }

  
  function guardarUsuarios(usuarios) {
    localStorage.setItem('usuariosRegistrados', JSON.stringify(usuarios));
  }

  forms.forEach(form => {
    form.addEventListener('submit', event => {
      event.preventDefault();
      event.stopPropagation();

      if (form.id === 'form-register') {
        const nombre = form.querySelector('#reg-name').value.trim();
        const correo = form.querySelector('#reg-email').value.trim();
        const pass = form.querySelector('#reg-password').value;
        const passConfirm = form.querySelector('#reg-password-confirm').value;
        const errorDiv = document.getElementById('password-match-error');

        if (pass !== passConfirm) {
          form.querySelector('#reg-password-confirm').setCustomValidity('Las contraseñas no coinciden');
          errorDiv.style.display = 'block';
        } else {
          form.querySelector('#reg-password-confirm').setCustomValidity('');
          errorDiv.style.display = 'none';
        }

        if (form.checkValidity()) {
          
          const usuarios = obtenerUsuarios();
          
          if (usuarios.some(u => u.correo === correo)) {
            alert('Este correo ya está registrado.');
          } else {
            usuarios.push({ nombre, correo, pass });
            guardarUsuarios(usuarios);
            alert('¡Registro exitoso! Por favor inicia sesión.');
            form.reset();
            form.classList.remove('was-validated');
          }
        }

      } else if (form.id === 'form-login') {
        const correo = form.querySelector('#login-email').value.trim();
        const pass = form.querySelector('#login-password').value;

        if (form.checkValidity()) {
          const usuarios = obtenerUsuarios();
          const usuario = usuarios.find(u => u.correo === correo && u.pass === pass);
          if (usuario) {
            localStorage.setItem('usuarioActivo', JSON.stringify({ nombre: usuario.nombre, correo: usuario.correo }));
            mostrarUsuario(usuario.nombre);
            ocultarFormularios();
            alert('¡Login exitoso!');
            form.reset();
            form.classList.remove('was-validated');
          } else {
            alert('Correo o contraseña incorrectos.');
          }
        }
      }

      form.classList.add('was-validated');
    }, false);
  });

  if (btnLogout) {
    btnLogout.addEventListener('click', () => {
      localStorage.removeItem('usuarioActivo');
      location.reload();
    });
  }

  function mostrarUsuario(nombre) {
    nombreUsuarioSpan.textContent = `¡Hola, ${nombre}!`;
    usuarioActivoDiv.style.display = 'flex';
  }

  function ocultarFormularios() {
    const main = document.querySelector('main');
    if (main) main.style.display = 'none';
  }
});



document.addEventListener("DOMContentLoaded", function () {
  const cerrarSesionBtn = document.getElementById("cerrarSesion");

  
  const usuario = localStorage.getItem("usuarioLogueado");

  if (!usuario) {
    
    cerrarSesionBtn.style.display = "none";
  } else {
   
    cerrarSesionBtn.style.display = "inline-block";
  }
});


  document.addEventListener("DOMContentLoaded", () => {
    const formComentario = document.getElementById("form-comentario");
    const listaComentarios = document.getElementById("lista-comentarios");
    const comentariosGuardados = JSON.parse(localStorage.getItem("comentarios")) || [];

    comentariosGuardados.forEach(comentario => {
      agregarComentarioALista(comentario.nombre, comentario.texto);
    });

    formComentario.addEventListener("submit", function (e) {
      e.preventDefault();

      const nombre = document.getElementById("nombre").value.trim();
      const comentario = document.getElementById("comentario").value.trim();

      if (nombre && comentario) {

        agregarComentarioALista(nombre, comentario)
        comentariosGuardados.push({ nombre, texto: comentario });
        localStorage.setItem("comentarios", JSON.stringify(comentariosGuardados));

        formComentario.reset();
      }
    });

    function agregarComentarioALista(nombre, texto) {
      const nuevoComentario = document.createElement("li");
      nuevoComentario.classList.add("mb-3", "p-3", "bg-secondary", "rounded");

      nuevoComentario.innerHTML = `
        <strong class="text-neon">${nombre} dice:</strong><br />
        <span>${texto}</span>
      `;

      listaComentarios.appendChild(nuevoComentario);
    }
  });

  document.addEventListener('DOMContentLoaded', () => {
    const btnCerrarSesion = document.getElementById('btn-logout');
    const usuarioActivoJSON = localStorage.getItem('usuarioActivo');
  
    if (usuarioActivoJSON) {
      btnCerrarSesion.style.display = 'inline-block'; 
    } else {
      btnCerrarSesion.style.display = 'none'; 
    }
  
    btnCerrarSesion?.addEventListener('click', () => {
      localStorage.removeItem('usuarioActivo');
      location.reload();
    });
  });
  

  
  document.addEventListener('DOMContentLoaded', () => {
    const usuarioActivoJSON = localStorage.getItem('usuarioActivo');
    const divUsuarioActivo = document.getElementById('usuario-activo');
    const nombreUsuario = document.getElementById('nombre-usuario');
    const btnLogout = document.getElementById('btn-logout');
  
    if (usuarioActivoJSON) {
      
      const usuario = JSON.parse(usuarioActivoJSON);
      nombreUsuario.textContent = usuario.nombre || "Usuario";
      divUsuarioActivo.style.display = 'flex'; 
    } else {
      
      divUsuarioActivo.style.display = 'none';
    }
  
   
    btnLogout.addEventListener('click', () => {
      localStorage.removeItem('usuarioActivo');
      location.reload();
    });
  });
  