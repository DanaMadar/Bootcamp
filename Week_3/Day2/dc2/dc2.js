//1.Get the value of each of the inputs in the HTML file when the button is clicked.
let inputValue = document.getElementsByTagName("input");
let btn = document.getElementById("lib-button");

btn.addEventListener("click", function (){
	for(let x of inputValue){
		let arrInput = []
        arrInput.push(inputValue)
	}

	if (inputValue === ""){
		alert("your input is invalid")
	}
	let placeValue = inputValue.place.value
    let ing = "ing "
    let newVerb = inputValue.verb.value + ing
    let name = inputValue.person.value
	


    let story = document.getElementById("story")
    story.innerHTML=`This is the story of ${name} and the ${inputValue.adjective.value} ${inputValue.noun.value} that is ${newVerb} in ${placeValue}`
})

let verbD = document.getElementById("verb").defaultValue="walk"
let nounD = document.getElementById("noun").defaultValue="cat"
let placeD = document.getElementById("place").defaultValue="Zurich"
let adjectiveD = document.getElementById("adjective").defaultValue="brown"
let personD = document.getElementById("person").defaultValue="Ella"