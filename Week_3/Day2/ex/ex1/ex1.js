let p = document.getElementsByTagName("p")[3]
p.remove(p)

let h2 = document.getElementsByTagName("h2")[0];
function changeColor(event){
	h2.style.backgroundColor= "red"
}
h2.addEventListener("click", changeColor)

let h3 = document.getElementsByTagName("h3")[0];
function hideTag(event){
    h2.style.display="none"
}

h3.addEventListener("click", hideTag)

let button = document.createElement("button");
button.innerHTML="bold"

let ps = document.querySelectorAll("p")
function bold(event) {
    for (let x of ps){
    x.style.fontWeight="bold"
    }
}
button.addEventListener("click", bold)
document.body.appendChild(button)

let submit = document.getElementById("submit")
let sub = document.querySelector(".usersAnswer")
console.log(submit);

submit.addEventListener ("click", function (event) {
	event.preventDefault();
	let inputFirstName = document.getElementById("fname")
	let inputLastName = document.getElementById("lname")

	let fNameValue = inputFirstName.value;
	let lNameValue = inputLastName.value;


	let pOne = document.createElement("p")
	let pTwo = document.createElement("p")
	let textOne = document.createTextNode(fNameValue)
	let textTwo = document.createTextNode(lNameValue)


	pOne.appendChild(textOne)
	pTwo.appendChild(textTwo)

    sub.appendChild(pOne)
    sub.appendChild(pTwo)


	inputFirstName.value = "";
	inputLastName.value = ""
	 
})

let paragraph = document.getElementsByTagName("p")[1]
console.log(paragraph);
    paragraph.addEventListener("mouseover",function() {
    this.style.opacity= "0.2";
    this.style.transition="opacity 1000ms"
})