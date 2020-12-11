// Funcion para abrir el modal.
document.getElementById("modal-btn").addEventListener("click", function () {
  document.querySelector(".bg-modal").style.display = "flex";
  countDownModal()
});

// Function para cerrar el modal.
function countDownModal() {
  // obtengo el elemento que lleva la cuenta
  var seconds = document.getElementById("countdown").textContent;
  //funcion que activa el contador.
  var countdown = setInterval(function () {

    seconds--;
    document.getElementById("countdown").textContent = seconds;

    //condicional que permite realizar x accion luego de que
    //el contador llegue a 0
    if (seconds <= 0){

      document.querySelector('.bg-modal').style.display = 'none';
      clearInterval(countdown)
      //TO DO: cambiar la redireccion a donde corresponda
      location.replace("index.html")

    };
  }, 500);
}

// con esto se cierra con un boton
/*
document.querySelector('.close-btn').addEventListener('click', function(){
  document.querySelector('.bg-modal').style.display = 'none';
});
*/
