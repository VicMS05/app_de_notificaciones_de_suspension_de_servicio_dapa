    // Obtener los elementos del DOM
    const passwordInput = document.getElementById("password-input");
    const passwordButton = document.getElementById("password-button");
    const passwordInput1 = document.getElementById("password-input1");
    const passwordButton1 = document.getElementById("password-button1");
    const passwordIcon = document.getElementById("password-icon");
    const passwordIcon1 = document.getElementById("password-icon1");

    // Agregar un evento de click al botón
    passwordButton.addEventListener("click", function() {
      // Obtener el tipo actual del input
      const type = passwordInput.getAttribute("type");
      // Si es password, cambiar a text y mostrar el icono de ojo abierto
      if (type === "password") {
        passwordInput.setAttribute("type", "text");
        passwordIcon.classList.replace("fa-eye-slash", "fa-eye");
      } else {
        // Si es text, cambiar a password y mostrar el icono de ojo cerrado
        passwordInput.setAttribute("type", "password");
        passwordIcon.classList.replace("fa-eye", "fa-eye-slash");
      }
    });

        // Agregar un evento de click al botón
        passwordButton1.addEventListener("click", function() {
            // Obtener el tipo actual del input
            const type = passwordInput1.getAttribute("type");
            // Si es password, cambiar a text y mostrar el icono de ojo abierto
            if (type === "password") {
              passwordInput1.setAttribute("type", "text");
              passwordIcon1.classList.replace("fa-eye-slash", "fa-eye");
            } else {
              // Si es text, cambiar a password y mostrar el icono de ojo cerrado
              passwordInput1.setAttribute("type", "password");
              passwordIcon1.classList.replace("fa-eye", "fa-eye-slash");
            }
          });