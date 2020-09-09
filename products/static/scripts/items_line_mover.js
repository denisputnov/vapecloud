let btn_left = document.getElementById('btn_left');
let btn_right = document.getElementById('brn_right');
let items_line = document.getElementById('items_line');
let itemId0 = document.getElementById('item0');
let itemId1 = document.getElementById('item1');



let now_item0_posX = 0;
async function autoMoveObject() {
    let timer = setInterval(function move() {
        let items_line_width = items_line.offsetWidth;
        console.log(items_line_width);
        console.log('in');
        now_item0_posX = calculateMove(items_line_width, now_item0_posX);
        console.log(now_item0_posX);
        itemId0.style = `transition-duration: 300ms; transform: translateX(${now_item0_posX}px);`;
        itemId1.style = `transition-duration: 300ms; transform: translateX(${now_item0_posX}px);`;

    }, 3000)    
};

function calculateMove(ilw, now) {
    if(now == 0) {
        return -ilw;
    } else if(now < 0) {
        return 0;
    }
}

autoMoveObject();

// transition-duration: 300ms; transform: translateX(0px);