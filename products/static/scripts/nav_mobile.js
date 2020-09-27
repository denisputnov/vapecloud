let navbar = document.getElementById('navbar');
let contentBlock = document.getElementById('contentBlock');

let logo = document.getElementById('logo');
let vapecloud = document.getElementById('vapecloud');
let searchform = document.getElementById('searchform');
let cart = document.getElementById('cart');
let rounder = document.getElementById('rounder'); 
let search = document.getElementById('search');
let submit = document.getElementById('submit');

async function controllNavbarView() {
    let timer = setInterval(function changeViewMode() {
        let width = window.innerWidth;
            
        if(width <= 767) {
            navbar.classList.add('nav_bar_mobile');
            navbar.classList.remove('nav_bar');
            navbar.style.flexDirection = 'column';
            logo.classList.add('logo_mobile');
            logo.classList.remove('logo');
            vapecloud.classList.add('vapecloud_mobile');
            vapecloud.classList.remove('vapecloud');
            searchform.classList.add('search_form_mobile');
            searchform.classList.remove('search_form');
            search.classList.add('search_mobile');
            search.classList.remove('search');
            submit.classList.add('submit_mobile');
            submit.classList.remove('submit');
            cart.classList.add('cart_mobile');
            cart.classList.remove('cart');
            rounder.classList.add('nav_bar_rounder_mobile');
            rounder.classList.remove('nav_bar_rounder');
        } else {
            navbar.classList.remove('nav_bar_mobile');
            navbar.classList.add('nav_bar');
            logo.classList.remove('logo_mobile');
            logo.classList.add('logo');
            vapecloud.classList.remove('vapecloud_mobile');
            vapecloud.classList.add('vapecloud');
            searchform.classList.remove('search_form_mobile');
            searchform.classList.add('search_form');
            search.classList.remove('search_mobile');
            search.classList.add('search');
            submit.classList.remove('submit_mobile');
            submit.classList.add('submit');
            cart.classList.remove('cart_mobile');
            cart.classList.add('cart');
            rounder.classList.remove('nav_bar_rounder_mobile');
            rounder.classList.add('nav_bar_rounder');
        }
    }, 300);
};

controllNavbarView();