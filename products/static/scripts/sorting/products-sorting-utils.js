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