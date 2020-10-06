function generateProduct(obj) { 
    return`
        <div class="product">
            <a href="${obj.a}" class="show_item"></a>
            <div class="price_block">
                <h3 class="price">${obj.price}<span class="rub">Р</span></h3>
            </div>
            <p class="label">${obj.label}</p>
            <img src="/static/images/shadow.png" alt="" class="shadow">
            <img src="${obj.img}" alt="" class="product_image gradient">
        </div>`
}


let $productsContainer = document.querySelector('.products');

try {
    let mode = document.querySelector('#mode').textContent || null;
} catch(e) {
    
}

let products = []
let $products = document.querySelectorAll('.product').forEach(prod => {
    products.push({
        a: prod.querySelector('.show_item').getAttribute('href'),
        price: parseInt(prod.querySelector('.price').textContent),
        label: prod.querySelector('.label').textContent,
        img: prod.querySelector('.product_image').getAttribute('src')
    })
})

console.log(products);

function clear() {
    $productsContainer.innerHTML = "";
}

function render(arr) {
    clear()
    let html = ''
    arr.forEach(el => {
        html += generateProduct(el)
    })
    $productsContainer.insertAdjacentHTML('afterbegin', html) // todos
}

function sortByPriceIncrease() {
    function _sort(arr) {
        arr.sort((a, b) => a.price > b.price ? 1 : -1)
    }
    
    _sort(products)
    render(products)
    document.querySelector('.sort-by-price').setAttribute('onclick', 'sortByPriceDecrese()')
}

function sortByPriceDecrese() {
    function _sort(arr) {
        arr.sort((a, b) => a.price < b.price ? 1 : -1)
    }
    
    _sort(products)
    render(products)
    document.querySelector('.sort-by-price').setAttribute('onclick', 'sortByPriceIncrease()')    
}

function sortByAlphabetA() {
    function _sort(arr) {
        arr.sort((a, b) => a.label.toLowerCase()[0] > b.label.toLowerCase()[0] ? 1 : -1)
    }

    _sort(products)
    render(products)
    document.querySelector('.sort-by-alphabet').setAttribute('onclick', 'sortByAlphabetZ()')
}

function sortByAlphabetZ() {
    function _sort(arr) {
        arr.sort((a, b) => a.label.toLowerCase()[0] < b.label.toLowerCase()[0] ? 1 : -1)
    }

    _sort(products)
    render(products)
    document.querySelector('.sort-by-alphabet').setAttribute('onclick', 'sortByAlphabetA()')
}

// $productsContainer.insertAdjacentHTML('beforebegin', model[mode]);