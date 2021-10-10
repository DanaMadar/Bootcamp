let pets = ["cat", "dog", "fish", "rabbit", "cow"];
let userPet = prompt("give me a new pet");
pets.push(userPet)
console.log("the last pet is: ", pets[pets.length-1])


let age = parseInt(prompt("what is your age"));

let pets = ['cat', 'dog', 'fish', 'rabbit'];
pets.splice(2, 0, 'dolphin', 'rats')
console.log(pets)