function sugerirUsuario() {
    const correo = document.getElementById('email').value.trim();
    let usuario = correo.split('@')[0];
    document.getElementById('usuario').value = usuario;
}

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("registroForm");
    const mensaje = document.getElementById("mensaje");

    form.addEventListener("submit", async function(e) {
        e.preventDefault(); // evita recargar la página

        const data = {
            Nombre: document.getElementById("nombre").value,
            Paterno: document.getElementById("ap_pat").value,
            Materno: document.getElementById("ap_mat").value,
            Usuario: document.getElementById("usuario").value,
            Email: document.getElementById("email").value,
            Password: document.getElementById("password").value,
            Id_Unidad_Academica: parseInt(document.getElementById("id_unidad_academica").value),
            Id_Rol: parseInt(document.getElementById("id_rol").value),
            Id_Estatus: 1,
        };

        try {
            const response = await fetch("/registro", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();

            if (response.ok) {
                mensaje.innerHTML =
                    `<p class="status ok">✅ Usuario registrado con ID ${result.Id_Usuario}</p>`;
            } else {
                mensaje.innerHTML =
                    `<p class="status fail">❌ Error: ${result.detail}</p>`;
            }
        } catch (err) {
            mensaje.innerHTML =
                `<p class="status fail">⚠️ Error de conexión: ${err.message}</p>`;
        }
    });
});
