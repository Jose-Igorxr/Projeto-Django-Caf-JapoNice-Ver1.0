document.addEventListener("DOMContentLoaded", function() {
    const carousel = document.querySelector(".carousel");
    const images = carousel.querySelectorAll("img");
    
    images.forEach(function(image) {
      const clone = image.cloneNode(true);
      carousel.appendChild(clone);
    });
  });

function mostrarAlerta() {
  alert("Seus Dados foram Enviados!");}
