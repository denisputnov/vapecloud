let mode = document.querySelector("#mode").textContent;
let $productsSortingContent = document.querySelector(
  ".products-sorting-content"
);

$productsSortingContent.innerHTML = sortingTemplates[mode];

let $products = document.querySelectorAll(".product");
let $parent = document.querySelector(".products");

let products = [];

class Product {
  constructor(product) {
    this.display = true;
    this.mode = product.getAttribute("data-mode");
    this.title = product.getAttribute("data-title");
    this.brand = product.getAttribute("data-brand");
    this.price = parseFloat(product.getAttribute("data-price"));
    this.sale = parseFloat(product.getAttribute("data-sale"));
    this.category = product.getAttribute("data-category");
    this.taste = product.getAttribute("data-taste");
    this.volume = parseFloat(product.getAttribute("data-volume"));
    this.salt = product.getAttribute("data-salt") === "NO" ? "Нет" : "Да";
    this.vg_to_pg = product.getAttribute("data-vg_to_pg");
    this.nicotine = parseFloat(product.getAttribute("data-nicotine"));
    this.country = product.getAttribute("data-country");
    this.image = product.querySelector(".product_image").getAttribute("src");
    this.link = product.querySelector(".show_item").getAttribute("href");
  }
}

function parseProducts() {
  $products.forEach(($product) => {
    products.push(new Product($product));
  });
}

parseProducts();

function _clearProducts() {
  $parent.innerHTML = "";
}

function render(products) {
  _clearProducts();
  $parent.innerHTML = generateProductHTML(products);
}

function generateProductHTML(products) {
  tmp = "";
  products.forEach((obj) => {
    if (obj.display) {
      tmp += `
      <div class="product" data-mode="${obj.mode}" data-title="${obj.title}" data-brand="${obj.brand}" data-price="${obj.price}" data-sale="${obj.sale}" data-category="${obj.category}" data-taste="${obj.taste}" data-volume="${obj.volume}" data-salt="${obj.salt}" data-vg_to_pg="${obj.vg_to_pg}" data-nicotine="${obj.nicotine}" data-country="${obj.country}">
        <a href="${obj.link}" class="show_item"></a>
        <div class="price_block">
          <h3 class="price">${obj.price}<span class="rub">Р</span></h3>
        </div>
        <p class="label">${obj.title}</p>
        <img src="/static/images/shadow.png" alt="" class="shadow">
        <img src="${obj.image}" alt="" class="product_image gradient">
      </div>`;
    }
  });
  return tmp;
}

function sortByPrice(mode) {
  let tmp = [...products];
  let $button = document.querySelector(".sort-by-price");

  function _sort(tmp, mode) {
    if (mode === "increment") {
      tmp.sort((a, b) => (a.price > b.price ? 1 : -1));
      $button.setAttribute("onclick", "sortByPrice(`decrement`)");
    } else {
      tmp.sort((a, b) => (a.price < b.price ? 1 : -1));
      $button.setAttribute("onclick", "sortByPrice(`increment`)");
    }
  }
  _sort(tmp, mode);
  render(tmp);
}

function sortByAlphabet(mode) {
  let tmp = [...products];
  let $button = document.querySelector(".sort-by-alphabet");

  function _sort(tmp, mode) {
    if (mode === "a-z") {
      tmp.sort((a, b) =>
        a.title.toLowerCase() > b.title.toLowerCase() ? 1 : -1
      );
      $button.setAttribute("onclick", 'sortByAlphabet("z-a")');
    } else {
      tmp.sort((a, b) =>
        a.title.toLowerCase() < b.title.toLowerCase() ? 1 : -1
      );
      $button.setAttribute("onclick", 'sortByAlphabet("a-z")');
    }
  }
  _sort(tmp, mode);
  render(tmp);
}

function sortByNicotine(mode) {
  let tmp = [...products];
  let $button = document.querySelector(".sort-by-nicotine");

  function _sort(tmp, mode) {
    if (mode === "increment") {
      tmp.sort((a, b) => (a.nicotine > b.nicotine ? 1 : -1));
      $button.setAttribute("onclick", 'sortByNicotine("decrement")');
    } else {
      tmp.sort((a, b) => (a.nicotine < b.nicotine ? 1 : -1));
      $button.setAttribute("onclick", 'sortByNicotine("increment")');
    }
  }
  _sort(tmp, mode);
  render(tmp);
}

function sortByVolume(mode) {
  let tmp = [...products];
  let $button = document.querySelector(".sort-by-volume");
  function _sort(tmp, mode) {
    if (mode === "increment") {
      tmp.sort((a, b) => (a.volume > b.volume ? 1 : -1));
      $button.setAttribute("onclick", "sortByVolume(`decrement`)");
    } else {
      tmp.sort((a, b) => (a.volume < b.volume ? 1 : -1));
      $button.setAttribute("onclick", "sortByVolume(`increment`)");
    }
  }
  _sort(tmp, mode);
  render(tmp);
}

function getCountries() {
  tmp = [];
  products.forEach((obj) => {
    let country = obj.country;
    tmp.push(country[0].toUpperCase() + country.slice(1));
  });
  return new Set(tmp);
}

try {
  let $countrySelect = document.getElementById("countrySelect");
  let countries = getCountries();
  countries.forEach((country) => {
    $countrySelect.insertAdjacentHTML(
      `beforeend`,
      `<option value="${country}" class='select'>${country}</option>`
    );
  });
} catch (e) {}

function sortByCountry(country) {
  let tmp = [...products];

  if (country === "NI") {
    tmp.forEach((product) => (product.display = true));
    render(tmp);
    return;
  }

  tmp.forEach((product) => {
    if (product.country.toLowerCase() !== country.toLowerCase()) {
      product.display = false;
    } else {
      product.display = true;
    }
  });
  render(tmp);
}

function getBrands() {
  tmp = [];
  products.forEach((obj) => {
    let brand = obj.brand;
    tmp.push(brand[0].toUpperCase() + brand.slice(1));
  });
  return new Set(tmp);
}

try {
  let $brandSelect = document.getElementById("brandSelect");
  let brands = getBrands();
  brands.forEach((brand) => {
    $brandSelect.insertAdjacentHTML(
      `beforeend`,
      `<option value="${brand}" class='select'>${brand}</option>`
    );
  });
} catch (e) {}

function sortByBrand(brand) {
  let tmp = [...products];

  if (brand === "NI") {
    tmp.forEach((product) => (product.display = true));
    render(tmp);
    return;
  }

  tmp.forEach((product) => {
    if (product.brand.toLowerCase() !== brand.toLowerCase()) {
      product.display = false;
    } else {
      product.display = true;
    }
  });
  render(tmp);
}

function sortBySalt(salt) {
  let tmp = [...products];

  if (salt === "NI") {
    tmp.forEach((product) => (product.display = true));
    render(tmp);
    return;
  }

  tmp.forEach((product) => {
    if (product.salt.toLowerCase() !== salt.toLowerCase()) {
      product.display = false;
    } else {
      product.display = true;
    }
  });
  render(tmp);
}

function sortBySale(sale) {
  let tmp = [...products];

  if (sale === "NI") {
    tmp.forEach((product) => (product.display = true));
    render(tmp);
    return;
  }

  tmp.forEach((product) => {
    if (
      (sale === "0" && product.sale === 0) ||
      (sale !== "0" && product.sale !== 0)
    ) {
      product.display = true;
    } else product.display = false;
  });
  render(tmp);
}

function getTastes() {
  tmp = [];
  products.forEach((obj) => {
    let taste = obj.taste;
    tmp.push(taste[0].toUpperCase() + taste.slice(1));
  });
  return new Set(tmp);
}

try {
  let $tasteSelect = document.getElementById("tasteSelect");
  let tastes = getTastes();
  tastes.forEach((taste) => {
    $tasteSelect.insertAdjacentHTML(
      `beforeend`,
      `<option value="${taste}" class='select'>${taste}</option>`
    );
  });
} catch (e) {}

function sortByTaste(taste) {
  let tmp = [...products];

  if (taste === "NI") {
    tmp.forEach((product) => (product.display = true));
    render(tmp);
    return;
  }

  tmp.forEach((product) => {
    if (product.taste.toLowerCase() !== taste.toLowerCase()) {
      product.display = false;
    } else {
      product.display = true;
    }
  });
  render(tmp);
}

function getVgpgs() {
  tmp = [];
  products.forEach((obj) => {
    let vgpg = obj.vg_to_pg;
    tmp.push(vgpg[0].toUpperCase() + vgpg.slice(1));
  });
  return new Set(tmp);
}

try {
  let $vgpgSelect = document.getElementById("vgpgSelect");
  let vgpgs = getVgpgs();
  vgpgs.forEach((vgpg) => {
    $vgpgSelect.insertAdjacentHTML(
      `beforeend`,
      `<option value="${vgpg}" class='select'>${vgpg}</option>`
    );
  });
} catch (e) {}

function sortByVgpg(vgpg) {
  let tmp = [...products];

  if (vgpg === "NI") {
    tmp.forEach((product) => (product.display = true));
    render(tmp);
    return;
  }

  tmp.forEach((product) => {
    if (product.vg_to_pg !== vgpg) {
      product.display = false;
    } else {
      product.display = true;
    }
  });
  render(tmp);
}
