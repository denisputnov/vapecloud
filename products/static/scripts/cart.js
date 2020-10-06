let storage = window.localStorage;

class Product {
    constructor(product) {
        this.a = product.querySelector('#product-href').getAttribute('href')
        this.img = product.querySelector('#product-image').getAttribute('src')
        this.name = product.querySelector('#product-name').textContent
        this.category = product.querySelector('#product-category').textContent
        this.quantity = parseFloat(product.querySelector('#product-quantity').textContent)
        this.price = parseFloat(product.querySelector('#product-price').textContent)
        this.defPrice = this.price / this.quantity 
    }
}

function defineCartContent() {
    let $emptyCartContent = document.querySelector('.not-funded-wrapper');
    let $products = document.querySelector('.products-wrapper');
    let $cartSum = document.querySelector('.cart-sum');
    let $orderButton = document.querySelector('.make-an-order');
    if (_isCartEmpty()) {
        $emptyCartContent.style.display = 'block';
        $products.style.display = 'none';
        $cartSum.style.display = 'none';
        $orderButton.style.display = 'none';
    } else {
        $emptyCartContent.style.display = 'none';
        $products.style.display = 'block';
        $cartSum.style.display = 'block';
        $orderButton.style.display = 'block';
        generateCart(_getCart());
    }
}
try {
    defineCartContent();
} catch(e) {
    if (storage.getItem('cart') === null) storage.setItem('cart', ' ');
    let $infoMessage = document.querySelector('.info-message-wrapper');
    document.querySelector('.add-to-card').addEventListener('click', () => {
        $infoMessage.classList.add('visible-message');
        setTimeout(() => $infoMessage.classList.remove('visible-message'), 1500);
    });
}

function _isCartEmpty() {
    if (_getCart() === []) return true
    return false
}

function _isProductInLocalStorage(product) {
    let localStorage = _getCart()
    for (let id = 0; id < localStorage.length; id++) {
        if (localStorage[id].name === product.name) return id;
    }
    return false;
}

function addToCart() {
    let $productWrapper = document.querySelector('.product-info-wrapper');
    _addProductToLocalStorage(new Product($productWrapper));
}

function _addProductToLocalStorage(product) {
    let cart = _getCart();
    let isRes = _isProductInLocalStorage(product);
    // if prod in cart -> update cart and resave,
    // else -> save new prod in cart 
    if (isRes === false) {
        cart.push(product)
    } else {
        cart[isRes].quantity += product.quantity
    }
    _updateStorage(cart)
}

function _getCart() {
    let cart = storage.getItem('cart');
    // if localstorage isn't has 'cart' key:
    if(cart === ' ') return [];
    // else
    return JSON.parse(cart)
}

function _updateStorage(update) {
    storage.setItem('cart', JSON.stringify(update))
}

function _updateProductQuantity(prodName, mode) {
    let cart = _getCart();
    cart.forEach(product => {
        if (product.name === prodName) {
            mode === '+' ? product.quantity += 1 : product.quantity -= 1; 
        } 
    })
    _updateStorage(cart);
}

function _deleteProductFromCart(prodName) {
    let cart = _getCart();
    for (let id = 0; id < cart.length; id++) {
        if (cart[id].name === prodName) cart.splice(id, 1)
    }
    _updateStorage(cart);
}

function generateCart(products) {
    clearCartHTML();
    let productCartHTML = ' ';
    let $productsWrapper = document.querySelector('.products-wrapper');

    products.forEach(product => {
        productCartHTML += `
            <div class="product">
                <a id="product-href" href="${product.a}">
                    <div class="cart-product-image-wrapper">
                        <img id="product-image" src="${product.img}" alt="" class="cart-product-image">
                    </div>
                </a>
                <div class="cart-product-info-wrapper">
                    <h2 id="product-name" class="cart-product-name">${product.name}</h2>
                    <p id="product-category" class="cart-product-category">${product.category}</p>
                    <p class="cart-product-price"><span id="product-price" class="price-number">${product.price}</span> руб</p>
                    <div class='controller-wrapper'>
                        <div class="counter-wrapper">
                            <button class='increment'><p>+</p></button>
                            <div class='counter'>
                                <p id="product-quantity" class='counter-value'>${product.quantity}</p>
                            </div>
                            <button class='decrement'><p>-</p></button>
                        </div>
                    </div>
                </div>
                <button class="delete-item">Удалить из корзины</button>
            </div>`
    });

    $productsWrapper.insertAdjacentHTML('afterbegin', productCartHTML);
    setEvents();
}

function clearCartHTML() {
    document.querySelector('.products-wrapper').innerHTML = '';
}

function setEvents() {
    let cartProducts = document.querySelectorAll('.product');
    let cartSum = document.querySelector('.cart-sum-value');

    cartProducts.forEach((el) => {
        let defPrice = parseInt(el.querySelector('.price-number').textContent) / parseInt(el.querySelector('.counter-value').textContent); 
        
        let price = el.querySelector('.price-number');
        let count = el.querySelector('.counter-value');

        let prodName = el.querySelector('#product-name').textContent;

        cartSum.textContent = parseInt(cartSum.textContent) + defPrice * parseInt(count.textContent);

        // actipns for +/- for every prod
        el.querySelector('.increment').addEventListener('click', (e) => {
            count.textContent = parseInt(count.textContent) + 1;
            price.textContent = defPrice * parseInt(count.textContent);
            cartSum.textContent = parseInt(cartSum.textContent) + defPrice;
            _updateProductQuantity(prodName, '+');
        });
        el.querySelector('.decrement').addEventListener('click', (e) => {
            if(parseInt(count.textContent) != 1) {
                count.textContent = parseInt(count.textContent) - 1;
                price.textContent = defPrice * parseInt(count.textContent);
                cartSum.textContent = parseInt(cartSum.textContent) - defPrice;
                _updateProductQuantity(prodName, '-');
            }
        });

        // delete prod from cart
        el.querySelector('.delete-item').addEventListener('click', () => {
            el.remove();
            cartSum.textContent = parseInt(cartSum.textContent) - defPrice * parseInt(count.textContent);    
            _deleteProductFromCart(prodName);    
        });
    });

    cartProducts.forEach( (el) => {
        let title = el.querySelector('.cart-product-name');
        if(title.textContent.length > 25 && window.innerWidth < 993) {
            title.style.fontSize = '20px';
        }
    });
}

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
try {
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
} catch(e) {}

