//Ex1
let colors = ["blue", "yello", "red", "purple"];

for (let index in colors) {
    console.log(colors[index])
 }

for (let i of colors) {
    console.log(i);
}


 //Ex2
let people = ["Greg", "Mary", "Devon", "James"];
let peopleNew;
people.shift();
people.splice(2, 1,"Jason");
people.push("Dana");

for (let i of people) {
    console.log(i);
}

peopleNew = people.slice(1);
console.log(peopleNew.indexOf("Mary"));
console.log(peopleNew.indexOf("Foo"));

let last = peopleNew[peopleNew.length -1];
console.log(last);


//Ex3
 let userNumber = parseInt(prompt("Type in any number"));

while (userNumber < 10) {
    userNumber = parseInt(prompt("Type in another number"));
}
console.log(userNumber);

//Ex4
let guestList = {
    randy: "Germany",
    karla: "France",
    wendy: "Japan",
    norman: "England",
    sam: "Argentina"
  }


const student = prompt('please enter your name:').toLowerCase();
const keys = Object.keys(guestList), index = keys.indexOf(student);
console.log(index === -1 ? `Hi! I'm a guest.` :
  `Hi! I'm ${keys[index]}, and I'm from ${guestList[student]}.`);

  // Ex5
let x = {family: "Paris"};


for (let element in x) {
  console.log(x);
}
for (let element in x) {
  console.log(x[element]);
}


//Ex6
let details = {
  my: 'name',
  is: 'Rudolf',
  the: 'raindeer'
}

let arr = Object.entries(details);
let detail1 = arr.join(",");
detail1 = detail1.replaceAll(",", " ");
console.log(detail1);
