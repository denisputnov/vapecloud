let menu = `<div class="sort-wrapper">
<div class="menu">
    <div class="menu-list">
        <li>
            <a href="/zhidkosti" class="menu-link">Жидкости</a>
            <div class="color"></div>
        </li>
        <li>
            <a href="/accessories" class="menu-link">Комплектующие</a>
            <div class="color"></div>
            <ul class="sub-menu-list">
                <li>
                    <a href="/accessories/isparitel" class="sub-menu-link">Испарители</a>
                </li>
                <li>
                    <a href="/accessories/kartridzh" class="sub-menu-link">Картриджи</a>
                </li>
                <li>
                    <a href="/accessories/mundshtuki" class="sub-menu-link">Мундштуки</a>
                </li>
                <li>
                    <a href="/accessories/vata" class="sub-menu-link">Спирали</a>
                </li>
                <li>
                    <a href="/accessories/vata" class="sub-menu-link">Вата</a>
                </li>
            </ul>
        </li>
        <li>
            <a href="/item/cloud" class="menu-link">Cloud</a>
            <div class="color"></div>
            <ul class="sub-menu-list">
                <li>
                    <a href="/item/cloud/zhidkosti" class="sub-menu-link">Жидкости</a>
                </li>
            </ul>
        </li>
        <li>
            <a href="/sales" class="menu-link">Скидки</a>
            <div class="color"></div>
        </li>
        <li>
            <a href="/other" class="menu-link">Прочее</a>
            <div class="color"></div>
        </li>
    </div>
</div>
</div>`

document.querySelector('.products').insertAdjacentHTML('beforebegin', menu);

function controllMenuClickEvents() {
    let delay = 1000;
    let timer = setInterval(() => {
        let width = window.innerWidth;
        let buttons = document.querySelector('.menu-list').querySelectorAll('.menu-link');

        if(width <= 992) {
            buttons.forEach(button => {
                button.setAttribute('onclick', 'return false');
                button.addEventListener('click', () => {
                    button.removeAttribute('onclick');
                    setTimeout(() => {
                        button.setAttribute('onclick', 'return false');
                    }, delay)
                })
            })
        }
    }, delay);
}

controllMenuClickEvents();