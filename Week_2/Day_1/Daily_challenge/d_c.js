//Ex1
let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
fruits.shift();
fruits.push("Kiwi");
fruits.splice(0, 1);
console.log(fruits.reverse())


//Ex2
let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(moreFruits[1][1][0])