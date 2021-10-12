//Ex1
let age1 = parseInt(prompt("What is your age"));
let age2 = parseInt(prompt("What is someone elses age"));

if (age1 > age2) {
    console.log(("In year " + ((age1 - age2 * 2 ) + 2021)) + " your will be twice as old as the other person") ;
} else {
    console.log(("In year " + ((age2 - age1 * 2) + 2021)) + " your were half the age of the other person")
}

//Ex2
let zip = parseInt(prompt("What is your zip code (5 numbers)"));

if (zip.toString().length == 5) {
    console.log("success");
} else {
    console.log("error");
}

//Ex3
let word = prompt("Write any word you like").toLowerCase();

word = word.replace( /[aeiou]/ig, '' );
console.log("word without vowel: " + word);

 