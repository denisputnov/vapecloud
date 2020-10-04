let count = document.querySelector('.counter-value'); 

document.querySelector('.increment').addEventListener('click', (e) => {
    count.textContent = parseInt(count.textContent) + 1;
});
document.querySelector('.decrement').addEventListener('click', (e) => {
    if(parseInt(count.textContent) != 1) {
        count.textContent = parseInt(count.textContent) - 1;
    }
});