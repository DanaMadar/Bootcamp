//Ex1
let x = 5;
let y = 2;

if (x > y) {
    console.log("x is the biggest number")
} else {
    console.log("y is the biggest number")
}

//Ex2
newDog = "Chihuahua";
console.log(newDog.online);
console.log(newDog.toUpperCase());
console.log(newDog.toLowerCase());
if (newDog === "Chihuahua") {
    alert("I love Chihuahuas, it’s my favorite dog breed")
} else {
    console.log("I dont care, I prefer cats");
}

//Ex3
userNum = parseInt(prompt("Enter a number"));

if (userNum % 2 == 0){
    alert(userNum + " is an even number")
} else {
    alert(userNum + " is an odd number")
}

//Ex4
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]
let online = users.length;

switch (online) {
    case 0:
        console.log("no one is online");
        break;
    case 1:
        console.log(users[0] + "is online");
        break;
    case 2:
        console.log(`${users[0]} and ${users[1]} is online`);
        break;
    default:
        console.log(`${users[0]} ,  ${users[1]} and 3 more are online`);
        break;
}