
for (let i = 0; i < (120*48); i++) {
    let divContainer = document.createElement('div');
    document.getElementById('gridPad').appendChild(divContainer);
}           // Creating the grid-layout with a field size of 120*48

let colorList = ['blue', 'red', 'green', 'rgb(131, 131, 248)', 'crimson', 'lawngreen', 'purple', 'saddlebrown', 'sandybrown', 'springgreen', 'turquoise', 'yellow', 'violet', 'orange', 'indigo', 'khaki', 'lightcoral', 'lightgrey', 'rgb(82, 82, 82)', 'black', 'cornsilk'];

for (let j = 0; j < colorList.length; j++) {
    let divContainer = document.createElement('div');
    document.getElementById('sidebar').appendChild(divContainer);
    divContainer.style.backgroundColor = colorList[j];
} // Adding all the colors from colorList each to the created elements

let colorDiv = null; // Empty variable for color in div
let mousedown = false; // Boolean for mousedown event
let sidebar_color = 0; // initialising element for loop
let grid_fill = 0; // initialising element for loop
let clear = document.getElementById('button-reset');
let sidebar_colors = document.querySelectorAll('#sidebar > div');
let grid_fills = document.querySelectorAll('#gridPad > div');
let body = document.getElementsByTagName('body')[0];

clear.addEventListener("click", clearFunction); // clears the creen by clicking the button and calling the function bellow

function clearFunction () {
    for (grid_fill of grid_fills) {
        grid_fill.style.backgroundColor = "grey";
    }
}

body.addEventListener("mousedown", function(){
    mousedown = true;
}); // checks for boolean of mouse down status

body.addEventListener("mouseup", function(){
    mousedown = false;
}); // checks for boolean of mouse down status

for(sidebar_color of sidebar_colors) {
    sidebar_color.addEventListener("click", sideColorFunction);
} // selects the color of the sidebar

function sideColorFunction (e) {
    colorDiv = e.target.style.backgroundColor;
    console.log(colorDiv);
}


for(grid_fill of grid_fills) {
    grid_fill.addEventListener("mousedown", fillColorFunction_click);
    grid_fill.addEventListener("mouseover", fillColorFunction_move);
}

function fillColorFunction_click (e) {
    if (colorDiv != null) {
        e.target.style.backgroundColor = colorDiv;
    }
}

function fillColorFunction_move (e) {
    if(mousedown == true && colorDiv != null) {
        e.target.style.backgroundColor = colorDiv;
    }
}