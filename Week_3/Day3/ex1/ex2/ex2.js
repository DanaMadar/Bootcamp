let item = document.getElementsByClassName("draggedItem")[0];
console.log(item);

item.addEventListener("dragstart", startDragging);

function startDragging(event) {
    event.target.classList.add("startDragging");
    event.dataTransfer.setData("text/plain",event.target.id);
}

let dropzone = document.getElementsByClassName("dropzone")[0];
dropzone.addEventListener("dragover", draggingOver)
dropzone.addEventListener("drop", dropping)


function draggingOver (event) {
	event.preventDefault();
}

function dropping(event){
    event.preventDefault();
	let elementToDrop = event.dataTransfer.getData("text/plain")
	let elemNode = document.getElementById(elementToDrop)
	event.target.appendChild(elemNode)
}