// forEach()


let account = 10000;
let tax = 1.17;
let income = [900, 300, 1200, 17, -600, -13, -8];
let total = 0;


let newIncome = income.map((x)=>x*tax);
console.log(newIncome);

newIncome.forEach(function(n){
    total += n;
});
console.log(total);