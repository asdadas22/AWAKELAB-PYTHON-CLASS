// Variables Hardcodeadas para login
// Variables constantes para el login dummy
const username = "admin"
const password = "123456"

// Funcion verificadora del login
document.getElementById('login-btn').addEventListener('click', function(){
  var tmpUsuario = document.getElementById('username').value;
  var tmpPassword = document.getElementById('password').value;
  if (tmpUsuario === username && tmpPassword === password) {
    location.replace('despacho.html')
  } 
  else{
    document.querySelector('.login-alert').style.display = 'inherit'
  }
})