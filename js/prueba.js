const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');
const registerBtn1 = document.getElementById('registarBtn1');

registerBtn.addEventListener('click', () => {
    container.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
});

registerBtn1.addEventListener('click', () => {
    container.classList.remove("active");
});

registerBtn1.addEventListener('click', (e) => {
    e.preventDefault();
  });