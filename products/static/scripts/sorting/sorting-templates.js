let sortingTemplates = {
    liquids: `
        <header class="products-sorting-header">
            <button class="product-sorting-button sort-by-price point" onclick="sortByPrice(\`increment\`)">Сортировать по цене</button>
            <button class="product-sorting-button sort-by-alphabet point" onclick="sortByAlphabet(\`a-z\`)">Сортировать А-я</button>
            <button class="product-sorting-button sort-by-volume point" onclick="sortByVolume(\`increment\`)">Сортировать по объёму</button>
            <button class="product-sorting-button sort-by-nicotine point" onclick="sortByNicotine(\`increment\`)">Сортировать по количеству никотина</button>
        </header>
        <div class='products-sorting-body'>
            <div class="product-sorting-select sort-by-country">
                <label for="countrySelect">Страна:</label>
                <select id="countrySelect" name="country" size="1" onchange="sortByCountry(\`\${this.options[this.selectedIndex].value}\`)">
                    <option value="NI" class='select' selected>Не важно</option>
                </select>
            </div>
            <div class="product-sorting-select sort-by-brand">
                <label for="brandSelect">Бренд:</label>
                <select id="brandSelect" name="brand" size="1" onchange="sortByBrand(\`\${this.options[this.selectedIndex].value}\`)">
                    <option value="NI" class='select' selected>Не важно</option>
                </select>
            </div>
            <div class="product-sorting-select sort-by-salt">
                <label for="saltSelect">SALT:</label>
                <select id="saltSelect" name="salt" size="1" onchange="sortBySalt(\`\${this.options[this.selectedIndex].value}\`)">
                    <option value="NI" class='select' selected>Не важно</option>
                    <option value="Да" class='select'>Да</option>
                    <option value="Нет" class='select'>Нет</option>
                </select>
            </div>
            <div class="product-sorting-select sort-by-sale">
                <label for="saleSelect">Скидка:</label>
                <select id="saleSelect" name="sale" size="1" onchange="sortBySale(\`\${this.options[this.selectedIndex].value}\`)">
                    <option value="NI" class='select' selected>Не важно</option>
                    <option value="somethink" class='select'>Есть</option>
                    <option value="0" class='select'>Нет</option>
                </select>
            </div>
            <div class="product-sorting-select sort-by-taste">
                <label for="tasteSelect">Вкус:</label>
                <select id="tasteSelect" name="taste" size="1" onchange="sortByTaste(\`\${this.options[this.selectedIndex].value}\`)">
                    <option value="NI" class='select' selected>Не важно</option>
                </select>
            </div>
            <div class="product-sorting-select sort-by-vgpg">
                <label for="vgpgSelect">Соотношение VG/PG:</label>
                <select id="vgpgSelect" name="vgpg" size="1" onchange="sortByVgpg(\`\${this.options[this.selectedIndex].value}\`)">
                    <option value="NI" class='select' selected>Не важно</option>
                </select>
            </div>
        </div>`
}