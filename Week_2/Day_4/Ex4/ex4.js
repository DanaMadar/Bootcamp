//ex1
// function infoAboutMe(){
//     let details = {
//         Name: "Dana",
//         Age: 33,
//         Hobbies: ["meeting with firends", "gardening", "building things"]
//     };
//     return details;
// }
// console.log(infoAboutMe());


// function infoAboutPerson(personName, personAge, personFavoriteColor, personHobbies) {
//     let name = personName;
//     let Age = personAge;
//     let color = personFavoriteColor;
//     let hobby = personHobbies;

//     for (i = 0; i<hobby.length; i++){
//        let HobbyList = hobby[i].length;
//     }
//     console.log(`My ${name} is, I'm ${Age} old and my favorit colour is ${color} and my hobbies are: ${hobby}`);
// }

// infoAboutPerson("David", 45, "blue", ["tennis", "painting"])
// infoAboutPerson("Josh", 12, "yellow", ["videoGame", "hanging out with friends", "playing cards"])

//ex2
//let userAge = parseInt(prompt("Whats your age"));

// function checkDriverAge(userAge) {
//     if (userAge < 18){
//         alert("Sorry, you are too young to drive this car. Powering off");
//     } else if (userAge > 18){
//         alert("You are old enough to drive, Powering On. Enjoy the ride!");
//     } else {
//         alert("Congratulations on your first year of driving. Enjoy the")
//     }
// };
// checkDriverAge(19);


//ex3
function checkNumber() {
    let num = 0;
    for (let i = 0; i<100; i++){
        num += 1;
        if (num%2 == 0){
            console.log(`The number ${num} is even`);
        }else {
            console.log(`The number ${num} is odd`);
        }
    }
};

checkNumber();