let sale = document.querySelector('.sale').textContent;
let $defPrice = document.querySelector('.price');
let $priceSpan = document.querySelector('#product-price');

if (sale !== '0') {
    let price = (defPrice - (defPrice * sale/100)).toFixed(2);
    $defPrice.insertAdjacentHTML('beforebegin', `<p class="item-def-price">${defPrice} руб.</p>`)
    $priceSpan.textContent = price;
}
