const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');
const $password = document.querySelector('input');
const $toggler = document.querySelector('i');

const showHidePassword = () => {
    if ($password.type == 'password'){
        $password.setAttribute('type','text');
    } else {
        $password.setAttribute('type','password')
    }

    $toggler.classList.toggle('fa-eye');
    $toggler.classList.toggle('fa-eye-slash');    
};


registerBtn.addEventListener('click', () => {
    container.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    container.classList.remove("active")
});

$toggler.addEventListener('click', showHidePassword);