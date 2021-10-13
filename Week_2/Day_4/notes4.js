// --------------
// // EXERCISE
// --------------

// let pets = ["blue", "red", "yellow", "lightblue"]

// I want to go through the colors array, and print each letter of each color
// 1. Do I need one or more loops?
// 2. Which type of loop is needed?
// 3. What is the logic inside the loop?

// Output should be like this:
// "b"
// "l"
// "u"
// "e"


// "r"
// "e"
// "d"

// ect...


// // 1st question:

// // 1. I need a for loop - because we need to go trhough the array
// // 2. we have a start and an end point
// // 3. (for of)

// // 2nd question
// // 1. I need to go trhough each element 
// // 2. When i reach each element, I then need to go trhough every letters
// // 3. for loops

// // GET THE LETTERS OF OF STRING
// // let color = "blue";
// // console.log("the first letter : ", color[0]);
// // console.log("the second letter : ", color[1]);

// --------------
// // EXERCISE
// --------------

let pets = ["blue", "red", "yellow", "lightblue"]

// the first for loop goes over the array, and I reached every color
for (let index = 0; index<pet.length; index++ ) {
	console.log("IN THE FIRST FOR LOOP : ");
	console.log("index : ", index);
	console.log("color : ", colors[index]);
	console.log("color length: ", colors[index].length);

	// the second loop goes over EACH color
	for (let indexLetter=0; indexLetter < colors[index].length;indexLetter++){
		console.log("IN THE NESTED FOR LOOP : ");
		console.log(colors[index][indexLetter])
	}
}

// // STEPS

// // 1st: 
// // I entered the first for loop ONCE
// // I enter the nested for loop FOUR TIMES

// // 2nd
// // I entered the second for loop ONCE
// // I enter the nested for loop THREE TIMES

// // 3rd
// // I entered the third for loop ONCE
// // I enter the nested for loop SIX TIMES


// -----------------
// FUNCTION
// -----------------


// SYNTAX

// DECLARING
function nameOfTheFunction () {
	//statement
}


//INVOCATION - CALLING
nameOfTheFunction()


// CREATE THE FUNCTION
function welcomeUser (){
	console.log("Welcome User");
};

// // invoke the function
welcomeUser()
welcomeUser()
welcomeUser()
welcomeUser()


// -----------------
// EXAMPLE
// -----------------

function checkNumber (){
	for (let i = 0; i<14; i++){
		if (i%2===0){
			console.log("even")
		} else {
			console.log("odd")
		}
	}
}


// PARAMETERS AND ARGUMENTS

// SYNTAX
// DECLARING
function nameOfTheFunction (parameter) {
	//statement
}

//INVOCATION - CALLING
nameOfTheFunction(argument)

// -----------------
// EXAMPLE
// -----------------

function welcomeSpecificUser (username){
	console.log(`Welcome ${username}`)
}

// // passing an argument
welcomeSpecificUser("John");
welcomeSpecificUser("Lea");

// -----------------
// SEVERAL PARAMETERS AND ARGUMENTS
// -----------------

// DECLARATION
function welcomeSpecificUser (username, userage){
	console.log(`Welcome ${username} you are ${userage} years old`)
}

// // passing an argument
welcomeSpecificUser(25, "John");


// -----------------
// EXERCISES
// -----------------

//1st function
// 1. Create a function, that accepts 3 arguments:
// * name of pet
// * color of pet
// * breed of pet

// 2. The function will alert a sentence using the values

// 					parameters
function detailsPet (name, color, breed){
	console.log(`${name} is a ${color} ${breed}`)
}

detailsPet("Rex", "blue", "German Shepard");
detailsPet("Leo", "red", "cat");


// 2nd function
// 1. Create a function, that accepts 2 arguments:
// * your age
// * array of favorite colors

// 2. In the function, 
// * create a locl variable, that is equal to twice your age
// * go through the colors array, and console.log all the colors
// * try to call the local variable outide of the function, what happens

// local scope
function detailsAboutMe (age, colors){
	// LOCAL SCOPE
	let twiceMyAge = age * 2;
	for (let color of colors){
		console.log(color)
	}
}

detailsAboutMe(56, ["blue", "red", "green"])
detailsAboutMe(56, ["pink", "yellow", "black"])

// global scope
// CANNOT ACCESS IT
console.log("twiceMyAge is :", twiceMyAge)

// GLOBAL SCOPE
let twiceMyAge = age * 2;

function detailsAboutMe (age, colors){
	// LOCAL SCOPE
	for (let color of colors){
		console.log(color)
	}
}

detailsAboutMe(56, ["blue", "red", "green"])
detailsAboutMe(56, ["pink", "yellow", "black"])

// global scope
// CAN ACCESS IT
console.log("twiceMyAge is :", twiceMyAge)


// -----------------
// OTHER EXAMPLE
// -----------------

// global scope
// global variable

let myAge = 34;

// local scope
// can access variable declared in the global scope
function myMumAge (){
	//console the age of my mum
	//twice my age 
	console.log(`the age of my mum is ${myAge*2}`)

}

myMumAge()


// -----------------
// RETURN
// -----------------

function twiceMyAge (myage){
	let twice = myage*2;
	return twice;//twiceMyage(50) = twice
				 //twiceMyage(50) = 50*2 = 100
}

// The variable twice 
// is now the RESULT of the function

// The function is now EQUAL to the result

// global scope
console.log(twiceMyAge(50));
// meaning:
// console.log(twice)
// console.log(100)

console.log(twice) //undefined

// -----------------
// OTHER EXAMPLE
// -----------------

function dateInTenYears (year) {
	let newDate =  year + 10;
	return newDate;
}

let dateSoon = dateInTenYears(2000);
console.log(dateSoon) 
// value: 2010
// value : newDate


console.log(`The year in 10 years is ${dateSoon}`)

// -----------------
// EXERCISE
// -----------------

let prices = [20, 12, 30];

function pricesWithTaxes (){
	// 1. go inside the array
	// 2. get each price , multiply by 1.17
	for (let i = 0; i<prices.length; i++){
		prices[i] *= 1.17;
	}
}

pricesWithTaxes();

function getSum (currencyConversion) {
	let sum = 0;
	for (let i = 0; i<prices.length; i++){
		sum += prices[i];
	}
	// sum of all the meals
	sum = sum*currencyConversion;
	return sum;
}

// 1. function that gives us the amount of tip we need to give
// 2. sum * 0.1
function getAmountTip (){
	let question = parseFloat(prompt("what is the currency conversion"));
	let sumMeal = getSum(question)

	let tip = (sumMeal*0.1).toFixed(2)

	// 1; return the value 
	return tip;
}


// take the tip and divide it by the number of meals
function getAmountTipPerPerson () {
	// 2. create a new variable, 
	// make it equal to the value returned by the function
	let generalTip = getAmountTip();

	let tipPerPerson = (generalTip/prices.length).toFixed(2);
	console.log(tipPerPerson)
}

getAmountTipPerPerson()


