let cartProducts = document.querySelectorAll('.product');
let cartSum = document.querySelector('.cart-sum-value');

cartProducts.forEach((el) => {
    let defPrice = parseInt(el.querySelector('.price-number').textContent) / parseInt(el.querySelector('.counter-value').textContent); 
    
    let price = el.querySelector('.price-number');
    let count = el.querySelector('.counter-value');

    cartSum.textContent = parseInt(cartSum.textContent) + defPrice * parseInt(count.textContent);

    // actipns for +/- for every prod
    el.querySelector('.increment').addEventListener('click', (e) => {
        count.textContent = parseInt(count.textContent) + 1;
        price.textContent = defPrice * parseInt(count.textContent);
        cartSum.textContent = parseInt(cartSum.textContent) + defPrice;
    });
    el.querySelector('.decrement').addEventListener('click', (e) => {
        if(parseInt(count.textContent) != 1) {
            count.textContent = parseInt(count.textContent) - 1;
            price.textContent = defPrice * parseInt(count.textContent);
            cartSum.textContent = parseInt(cartSum.textContent) - defPrice;
        }
    });

    // delete prod from cart
    el.querySelector('.delete-item').addEventListener('click', () => {
        el.remove();
        cartSum.textContent = parseInt(cartSum.textContent) - defPrice;        
    });
});

cartProducts.forEach( (el) => {
    let title = el.querySelector('.cart-product-name');
    if(title.textContent.length > 25 && window.innerWidth < 993) {
        title.style.fontSize = '20px';
    }
});


function _generateCartStat() {
    cartProducts = document.querySelectorAll('.product');
    let cartSum = 0;
    cartProducts.forEach((el) => {
        let defPrice = parseInt(el.querySelector('.price-number').textContent) / parseInt(el.querySelector('.counter-value').textContent); 
       
        count = el.querySelector('.counter-value');
        document.querySelector('.modal-cart-stat').insertAdjacentHTML("beforeEnd",
            `<p class="modal-cart-product">${count.textContent}x - ${el.querySelector('.cart-product-name').textContent}</p>`
        );

        cartSum += parseInt(el.querySelector('.counter-value').textContent) * defPrice;
        console.log(typeof cartSum);
    });
    document.querySelector('.modal-cart-stat').insertAdjacentHTML("beforeEnd",
        `<p class="modal-cart-sum">Итого: ${cartSum} руб</p>`
    );
}

function _clearCartStat() {
    let modalCartProducts = modal.querySelectorAll('.modal-cart-product');
    modalCartProducts.forEach((el) => el.remove());
    modal.querySelector('.modal-cart-sum').remove();
}

// modal window block
let modal = document.querySelector('.modal-wrapper');
let makeAnOrderBtn = document.querySelector('.make-an-order-button');

// actions
// close modal window
modal.querySelector('.modal-close').addEventListener('click', () => {
    modal.style.display = 'none';
    _clearCartStat();
});
modal.querySelector('.cancel-order').addEventListener('click', () => {
    modal.style.display = 'none';
    _clearCartStat();
})
// open modal window
makeAnOrderBtn.addEventListener('click', () => {
    modal.style.display = 'block';
    _generateCartStat();
})
