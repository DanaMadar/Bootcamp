// about the green box

// 1. Retrieve the green box
let item = document.getElementById("item");
let item2 = document.getElementById("item2");

item.addEventListener("dragstart", startDragging);
item2.addEventListener("dragstart", startDragging);

function startDragging (event) {
	console.log("start dragging", event.target.id);
	event.target.classList.add("startDragging");
    event.target.classList.add("changeColor")
	// console.log(event.dataTransfer)
	// syntax
	// event.dataTransfer.setData("type of data", id of the elem)
	event.dataTransfer.setData("text/plain",event.target.id)
}


// the black target boxes

let allDropZones = document.getElementsByClassName("dropzone");
console.log(allDropZones)

function addTheListeners (){
	for (let zone of allDropZones){
		zone.addEventListener("dragover", draggingOver)
		zone.addEventListener("drop", dropping)
	}
}

addTheListeners()

// create the dragging Over function
function draggingOver (event) {
	event.preventDefault();
	// console.log(event.target)
}



// Create the dropping function
function dropping(event){
    event.preventDefault();
    event.target.classList.add("changeDropzone")
	// console.log(event.target)
	// 1. retrieve the element that we want to srop
	let elementToDrop = event.dataTransfer.getData("text/plain")
	// 2. append the element on the drop zone
	let elemNode = document.getElementById(elementToDrop)
	event.target.appendChild(elemNode)
}


// setTimeout
function welcome (){
	document.body.style.backgroundColor = "red";
	setTimeout(getWhite, 2000)
}

function getWhite(){
	document.body.style.backgroundColor = "blue";
}

setTimeout(welcome, 2000);


// setInterval
let section = document.getElementById("container")
let button = document.getElementById("btn")

button.addEventListener("click", stopAnimation)

function addDiv(){
	let div = document.createElement("div");
	let text = document.createTextNode("hello");
	div.appendChild(text);
	section.appendChild(div);
}

let timeId = setInterval(addDiv, 1000);

function stopAnimation(){
	clearInterval(timeId)
}