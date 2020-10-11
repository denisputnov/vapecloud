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
let products = []
let $products = document.querySelectorAll('.product').forEach(prod => {
    products.push({
        a: prod.querySelector('.show_item').getAttribute('href'),
        price: parseInt(prod.querySelector('.price').textContent),
        label: prod.querySelector('.label').textContent,
        img: prod.querySelector('.product_image').getAttribute('src')
    })
})
