for (let counter = 1; counter <= 15; counter++) {
    if (counter % 2 == 0) {
    console.log(counter + " is even");
    } else {
    console.log(counter + " is odd");
    }
}

let shopping = ["apple", "pear", "melon", "banana"]

for (let i = 0; i < shopping.length; i++) {
    shopping[i] += "s";
}
console.log(shopping);

for ( let index in shopping.length) {
    console.log(shopping [index]);
}


let prices = [23, 15, 34, 20];
let sum = 0;

for (let i = 0; i < prices.length; i++) {
    sum += prices[i];
}
console.log(sum);


let person = {
    fname : "John",
    lname : "Smith",
    age : 25
}

for (let element in person) {
    console.log(person[element]);
}


let count = 1;

while (count < 10) {
    count += 2;
}
console.log(count);