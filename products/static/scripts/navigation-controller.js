let menu = document.querySelector('.menu');
let menuCategories = menu.querySelectorAll('.menu-list');

menuCategories.forEach((el) => {
    el.addEventListener('click', () => {
        el.classList.toggle = 'display-block';
    });
});