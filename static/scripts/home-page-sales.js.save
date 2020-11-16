class Product {
    constructor(product) {
        this.a = product.querySelector('.show_item').getAttribute('href')
        this.img = product.querySelector('.product_image').getAttribute('src')
        this.name = product.querySelector('.label').textContent
        this.defPrice = parseFloat(product.querySelector('.price').textContent)
        this.sale = parseInt(product.getAttribute('data-sale')) / 100
        if (this.sale > 0 && this.sale < 1) {
            this.price = (this.defPrice - (this.defPrice * this.sale)).toFixed(2)
        } else {
            this.price = this.defPrice
        }
    }
}

function parseProds() {
    let products = []
    let $products = document.querySelectorAll('.product')
    $products.forEach($product => {
        products.push(new Product($product))
    })
    return products 
}

function clearProds() {
    let $area = document.querySelector('.products')
    $area.innerHTML = '' 
}

function generateProducts(products) {
    let res = ''
    products.forEach((prod) => {

    prod.price == prod.defPrice ? res += `
    <div class="product">
        <a href="${prod.a}" class="show_item"></a>
        <div class="price_block">
          <h3 class="price">${prod.price}<span class="rub">Р</span></h3>
        </div>
        <p class="label">${prod.name}</p>
        <img src="/static/images/shadow.png" alt="" class="shadow">
        <img src="${prod.img}" alt="" class="product_image gradient">
      </div>
    `
    : res += `
    <div class="product">
        <a href="${prod.a}" class="show_item"></a>
        <div class="price_block">
          <h3 class="def-price">${prod.defPrice}<span class="rub-red">Р</span></h3>
          <h3 class="price">${prod.price}<span class="rub">Р</span></h3>
        </div>
        <p class="label">${prod.name}</p>
        <img src="/static/images/shadow.png" alt="" class="shadow">
        <img src="${prod.img}" alt="" class="product_image gradient">
      </div>
    `
        }
    )
    return res
}

function init() {
    let newProds = generateProducts(parseProds())
    clearProds()
    document.querySelector('.products').innerHTML = newProds
}

(() => {
    init()
})()
