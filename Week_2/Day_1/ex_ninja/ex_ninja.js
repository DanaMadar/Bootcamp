//ex_1
sentence_user = prompt("Write a sentence inclueding 'Nemo'");
sentence_user2 = sentence_user.indexOf("Nemo");

console.log("I found Nemo at position ", sentence_user2)

//ex4
let explosion = "boooooooooom";
let end = 0;

count = explosion.split("o").length - 1;
if (count % 2 == 0){
    end = explosion + "!"
} 
if (count % 5 == 0){
    end = end.toUpperCase()
}
alert(end)


