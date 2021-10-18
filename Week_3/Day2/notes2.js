// let buttonRed = document.getElementById("red")
// let buttonBlue = document.getElementById("blue")


// red.addEventListener("click", function () {
//     document.getElementById("btn").style.color="red"
// }
// blue.addEventListener("click", function (){
//     document.getElementById("title").style.color="blue"
// }

// buttonBlue.addEventListener("click", function(event){
//     let color = event.target.textContent.toLowerCase();
//     document.body.style.backgroundColor=color
// })

// function changeColor(event) {
//     let color=event.target.textContent.toLowerCase();
//     document.body.style.backgroundColor=color
// }

// buttonBlue.addEventListener("click", changeColor);
// buttonRed.addEventListener("click", changeColor);
let colors = ["blue", "yellow", "green", "pink"];
let bodyElement =document.body

function createButton(event) {
    for (let x of colors){
        let button=document.createElement("button")
        button.id=x
        button.classList.add("button")
        button.style.backgroundColor=x;
        button.addEventListener("click", changeColor)
        button.innerHTML=x
        document.getElementById("container").appendChild(button)
    }
}
createButton()

function changeColor(event) {
    let colorButton=event.target.textContent.toLowerCase();
    bodyElement.style.backgroundColor = colorButton
}

//version
// let colors = ["blue", "yellow", "green", "pink"];

// let div = document.getElementById("container")
// let bodyElement = document.body

// function createButtons (){

// 	for(let color of colors){
// 		let btn = document.createElement("button");
// 		let text = document.createTextNode(color);
// 		btn.classList.add("btn")
// 		btn.addEventListener('click', changeColor)
// 		btn.appendChild(text);
// 		div.appendChild(btn);
// 	}

// }

// createButtons()


// // callback function
// function changeColor(event){
// 	// console.log(event.target)
// 	let colorButton = event.target.textContent.toLowerCase();
// 	bodyElement.style.backgroundColor = colorButton;
// }