document.addEventListener("DOMContentLoaded", function() {
    const input_fields = document.querySelectorAll('input:not([type="submit"])');

    for (let i=0; i<input_fields.length; i++) {
        input_fields[i].style.backgroundImage = 'none';
        input_fields[i].classList.remove("is-invalid");
    }
});
