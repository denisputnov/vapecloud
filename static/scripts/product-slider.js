const slider = document.querySelector('.product-slider-container');

let mySwiper = new Swiper(slider, {
    slidesPerView: 1,
    pagination: {
        el: '.swiper-pagination',
        type: 'bullets',
        clickable: true,
      },
})