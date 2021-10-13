//ex1
function infoAboutMe(){
    let details = {
        Name: "Dana",
        Age: 33,
        Hobbies: ["meeting with firends", "gardening", "building things"]
    };
    return details;
}
console.log(infoAboutMe());


function infoAboutPerson(personName, personAge, personFavoriteColor, personHobbies) {
    let name = personName;
    let Age = personAge;
    let color = personFavoriteColor;
    let hobby = personHobbies;

    for (i = 0; i<hobby.length; i++){
       let HobbyList = hobby[i].length;
    }
    console.log(`My ${name} is, I'm ${Age} old and my favorit colour is ${color} and my hobbies are: ${hobby}`);
}

infoAboutPerson("David", 45, "blue", ["tennis", "painting"])
infoAboutPerson("Josh", 12, "yellow", ["videoGame", "hanging out with friends", "playing cards"])

//ex2
let userAge = parseInt(prompt("Whats your age"));

function checkDriverAge(userAge) {
    if (userAge < 18){
        alert("Sorry, you are too young to drive this car. Powering off");
    } else if (userAge > 18){
        alert("You are old enough to drive, Powering On. Enjoy the ride!");
    } else {
        alert("Congratulations on your first year of driving. Enjoy the")
    }
};
checkDriverAge(19);


//ex3
function checkNumber() {
    let num = 0;
    for (let i = 0; i<=100; i++){
        num += 1;
        if (num%2 == 0){
            console.log(`The number ${num} is even`);
        } else {
            console.log(`The number ${num} is odd`);
        }
    }
};

checkNumber();

//ex4
let sum = 0;
function isDivisible()
{
 for(let i= 0; i <500 ; i++)
 {
    if(i %23 === 0)
        sum += i;
        console.log(i);
    }
    console.log(sum)
}
isDivisible();

//ex5
let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
}

let item = prompt("Choose a item");

function checkBasket(item) {
    if (item in amazonBasket){ 
    alert("your item is in the basket");
    }
};

checkBasket(item);

//ex6
function changeEnough(arr, number){
    let sum = 0;
    for (let i=0; i<arr.length; i++){
        if (i == 0){
            sum += 0.25*arr[i];
        }
        if (i == 1){
            sum += 0.10*arr[i];
        }
        if (i == 2){
            sum += 0.05*arr[i];
        }
        if (i == 3){
            sum += 0.01*arr[i];
        }
    }
    if(sum > number){
        return true;
    }
    return false;
}

console.log(changeEnough([2, 100, 0, 0], 14.11))
console.log(changeEnough([0, 0, 20, 5], 0.75))


//ex7
let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

let shoppingList = ["banana", "orange","apple"]


function myBill() {
    for (let i = 0; i < shoppingList.length; i++) {
        if (stock[shoppingList[i]] > 0){
        console.log(shoppingList[i]),(prices[shoppingList[i]]);
         }
        
    }
    
}

myBill()

//Ex8
let bill = parseFloat(prompt("How much was the bill?"))

if (bill<50){
	billTip = bill*1.20;
} else if (bill<200){
    billTip = bill*1.15;
} else{
    billTip = bill*1.10;
}
let tip = billTip-bill;
alert(`your bill with tip is ${billTip} so the tip is ${tip}`);

//ex9
const hotelCost = () => {
    let nights = 0;
    while (nights < 1 || isNaN(nights)) {
        nights = Number(prompt('please enter number of nights:'));
    }
    return nights * 140;
};

console.log(hotelCost())


const planeRideCost = () => {
    let destination = '';
    while (destination === '' || destination === null || typeof destination !== 'string') {
        destination = prompt('please enter destination:');
    }
    switch (destination.toLowerCase()) {
        case 'london':
            return 183;
        case 'paris':
            return 220;
        default:
            return 300;
    }
};
console.log(planeRideCost());


const rentalCarCost = () => {
    let days = 0;
    while (days < 1 || isNaN(days)) {
        days = Number(prompt('please enter number of days to rent a car:'));
    }
    const val = days * 40;
    return days > 10 ? val * 0.95 : val;
};
console.log(rentalCarCost());


const totalVacationCost = () => {
    const hotel = hotelCost(), plane = planeRideCost(), car = rentalCarCost(), total = hotel + plane + car;
    alert(`The car cost: $${car}, the hotel cost: $${hotel}, the plane tickets cost: $${plane}, total of $${total}`);
}
totalVacationCost();