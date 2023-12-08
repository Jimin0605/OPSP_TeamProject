/*!
    * Start Bootstrap - SB Admin v7.0.7 (https://startbootstrap.com/template/sb-admin)
    * Copyright 2013-2023 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-sb-admin/blob/master/LICENSE)
    */
    // 
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }


    document.querySelectorAll('input[type="checkbox"]').forEach(function (checkbox) {
        checkbox.addEventListener('change', function () {
            document.querySelectorAll('input[name="' + this.name + '"]').forEach(function (otherCheckbox) {
                if (otherCheckbox !== checkbox) {
                    otherCheckbox.checked = false;
                }
            });
        });
    });

});

var handle = document.getElementById("ageHandle");
  var slider = document.getElementById("ageSlider");

// Get the handle and slider elements
var handle = document.getElementById("ageHandle");
var slider = document.getElementById("ageSlider");

// Set the initial age value
var age = 25;
document.getElementById("ageValue").innerText = age;

// Event listener for mouse down on the handle
handle.onmousedown = function (event) {
  // Prevent the default browser action
  event.preventDefault();

  // Calculate the mouse position at startup
  var offsetX = event.clientX - handle.offsetLeft;

  // Move the handle based on mouse movement
  document.onmousemove = function (event) {
    // Calculate the new handle position
    var newLeft = event.clientX - offsetX;

    // Ensure the handle stays within the slider bounds
    if (newLeft >= 0 && newLeft <= slider.offsetWidth - handle.offsetWidth) {
      handle.style.left = newLeft + "px";

      // Update the selected age based on the handle position
      age = Math.round((newLeft / (slider.offsetWidth - handle.offsetWidth)) * 100);
      document.getElementById("ageValue").innerText = age;
    }
  };

  // Stop moving when mouse button is released
  document.onmouseup = function () {
    document.onmousemove = null;
    document.onmouseup = null;
  };
};