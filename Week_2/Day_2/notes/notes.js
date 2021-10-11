let shopping = {
    apples: 2,
    pears: 4,
    banana: 5,
};

//console.log(shopping.apples);       
//console.log(shopping["apples"]);    //recomanded

shopping["apples"] = 10;        //change
shopping["chocolate"] = 2;      //add


let family = {
    lastname: "Smith",
    member: 4,
    hasADog: true,
    nameOfMembers: ["Lea", "David", "Mom", "Dad"],
    friends: {
        name: "Jack",
        age: 12,
        favoriteColor: ["blue", "red"]
    }
};

console.log("the second member is: ", family["nameOfMembers"][1]);
console.log(family["friends"]["favoriteColor"][0]);

//Ex
let userCart = {
	username : "John",
	password: 1234,
	isUserSignedIn : true,
	cart : {
		apple : 2,
		banana : 1,
		pear : 5
	},
	prices : {
		apple : 0.5,
		banana : 0.8646466363,
		pear : 0.2
	}
};

userCart["Lastname: "] = "Smith";

userCart["prices"]["pear"] = userCart["prices"]["pear"] * 1.17;
userCart["prices"]["pear"] *= 1.17;     // recomanded
console.log(userCart["prices"]["pear"]);

let userFruit = prompt("Which fruit do you want").toLowerCase();
console.log(userCart["prices"][userFruit]);
console.log(`The price of the ${userFruit} is ${userCart["prices"][userFruit]}`);


//if
let bankAmount = parseInt(prompt("How much money do you have"));
let priceCar = 500;
let priceBike = 200;

if (bankAmount >= priceCar) {
    console.log("I can buy a car!");
    bankAmount -= priceCar;
} else if (bankAmount >= priceBike) {
    console.log("I can't buy a car, but a bike works as well")
    bankAmount-= priceBike;
} else {
    console.log("Don't buy it, you have no money!");
}

//ex


if (userCart["isUserSignedIn"]) {
    console.log(userCart["username"], userCart["password"]);
} else{
    console.log("you need to sign in");
}


if (userCart["username"] === "John" && userCart["password"] === 1245) {
    alert("You are signed in")
} else if (userCart["username"] === "John" || userCart["password"] === 1245) {
    alert("One condition is false")
} else{
    alert("you need to sign in")
}

switch(username) {
    case "John":
        console.log("Hello John")
        break;
    case "Lea":
        console.log("Hello Lea")
        break;
    case "Maria":
        console.log("Hello Maria")
        break;
    default:
        console.log("Sorry");
}