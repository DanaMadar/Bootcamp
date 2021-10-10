//ex_1
sentence_user = prompt("Write a sentence inclueding 'Nemo'");
sentence_array= sentence_user.split(" ");
console.log(sentence_array);
position = sentence_array.indexOf("Nemo");
console.log("I found Nemo at position ", position)


//ex2
// 1. 23, 2.undefined, 3. 75

//ex3
let num = prompt("Give me a list of 2 numbers and seperate them by ',' ");
let array = num.split(",");
sp_arr = parseInt((array[0]));
sp_arr2 = parseInt((array[1]));
let sum = sp_arr + sp_arr2
alert(sum);


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


