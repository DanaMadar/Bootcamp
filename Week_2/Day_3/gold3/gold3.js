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

let rent = Object.values(building["numberOfRoomsAndRent"]);
rentDan = rent[1].slice(1, 2);
rentSD = parseInt(rent[0].slice(1, 2))+parseInt(rent[2].slice(1, 2));
if (rentDan < rentSD) {
    rentDan = 1200;
}

console.log(rentDan);

