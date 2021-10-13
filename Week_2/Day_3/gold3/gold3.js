let building = {
    numberLevels : 4,
    numberOfAptByLevel : {
        "1": 3,
        "2": 4,
        "3": 9,
        "4": 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        "Sarah": [3, 990],
        "Dan":  [4, 1000],
        "David": [1, 500],
    },
}
console.log(building["numberLevels"]);
console.log(building["numberOfAptByLevel"]["1"]);
console.log(building["numberOfRoomsAndRent"]["Dan"][0]);

let key = Object.keys(building["numberOfRoomsAndRent"]);
rentDan= rent.slice(1, 2);
for ("dan" in 

if (rentDan < rent) {
    rentDan += 500;
}

console.log(rentDan);

// const student = prompt('please enter your name:').toLowerCase();
// const keys = Object.keys(guestList), index = keys.indexOf(student);
// console.log(index === -1 ? `Hi! I'm a guest.` :
//   `Hi! I'm ${keys[index]}, and I'm from ${guestList[student]}.`);