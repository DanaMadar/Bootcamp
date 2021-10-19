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
	let place = inputValue.place.value
    let ing = "ing "
    let verb = inputValue.verb.value + ing
    let name = inputValue.person.value
	let noun = inputValue.noun.value
	let adj = inputValue.adjective.value
	


    let story = document.getElementById("story")
	story.innerHTML=`This is a story about ${name} who likes ${verb} in ${place} to find a ${adj} ${noun} behind buildins.`
    //story.innerHTML=`This is a story about ${name} and the ${adj} ${noun} that is ${verb} in ${place}`
})

let verbD = document.getElementById("verb").defaultValue="walk"
let nounD = document.getElementById("noun").defaultValue="cat"
let placeD = document.getElementById("place").defaultValue="Zurich"
let adjectiveD = document.getElementById("adjective").defaultValue="stinky"
let personD = document.getElementById("person").defaultValue="Ella"