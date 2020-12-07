let sale = document.querySelector('.sale').textContent;
let $defPrice = document.querySelector('.price');
let $priceSpan = document.querySelector('#product-price');
priceSpan = document.querySelector('#product-price');
defPrice = parseFloat(priceSpan.textContent);

if (parseFloat(sale)) {
    let price = (defPrice - (defPrice * sale/100)).toFixed();
    $defPrice.insertAdjacentHTML('beforebegin', `<p class="item-def-price">${defPrice} руб.</p>`)
    $priceSpan.textContent = price;
}
