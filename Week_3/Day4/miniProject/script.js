let container = document.getElementById("container");
let leftSide = document.getElementById("secLeft");
let btn = document.getElementById("btn");
let rightSide = document.getElementById("secRight");

let isMouseDown = false;

let colors = [];
while (colors.length < 21) {
    colors.push(`rgb(${rand(0, 255)}, ${rand(0, 255)}, ${rand(0, 255)})`);
}
// random number generator
function rand(frm, to) {
    return ~~(Math.random() * (to - frm)) + frm;
}

btn.addEventListener("click", clearAll)

function clearAll(event) {
    let all = document.querySelectorAll(".square")
    console.log(all);
    for (let i=0; i<1440; i++){
        all[i].style.backgroundColor="white"
    }
}


function colorPallet() {
    for (let i=0; i<colors.length;i++){       
        let div = document.createElement("div");
        div.style.backgroundColor=(colors[i]);
        div.style.border="1px solid black";
        div.style.margin="2px"
        
        div.addEventListener("click", getColor)
        leftSide.appendChild(div)
       }
}
colorPallet()

let myColor;

function getColor(event) {
    myColor = this.style.backgroundColor;
    console.log(myColor);
}


for (let i=0; i<1440; i++){
    let divR = document.createElement("div");
    divR.style.border="1px solid grey";
    divR.classList.add("square")
    rightSide.appendChild(divR);
    divR.addEventListener("mousedown", setColor);
    divR.addEventListener("mouseover", over);
    divR.addEventListener("mouseup", up);
   
}

function setColor(event) {
    isMouseDown = true
    this.style.backgroundColor = myColor;
    console.log(myColor);
}

function over(event) {
    if(isMouseDown){
      this.style.backgroundColor = myColor;
    console.log(myColor);  
    }
    
}
function up(event) {
   isMouseDown = false
}
