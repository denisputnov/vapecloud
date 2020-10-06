let count = document.querySelector('.counter-value'); 
let priceSpan = document.querySelector('#product-price');
let defPrice = parseFloat(priceSpan.textContent);

document.querySelector('.increment').addEventListener('click', (e) => {
    count.textContent = parseInt(count.textContent) + 1;
    priceSpan.textContent = defPrice * parseInt(count.textContent)
});
document.querySelector('.decrement').addEventListener('click', (e) => {
    if(parseInt(count.textContent) != 1) {
        count.textContent = parseInt(count.textContent) - 1;
        priceSpan.textContent = defPrice * parseInt(count.textContent)
    }
});