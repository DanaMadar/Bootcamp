//ex1
for (let i = 0; i<100; i++){
    let randomNum = Math.floor(Math.random() * 101) + 1;
    console.log(randomNum);
};

//ex2
let str = "abcdefg";
let newStr= "";
let letters = (str) =>{
    for (let x=0; x<str.length; x++){
        if (x%2== 0){
            newStr += str[x].toUpperCase();
        }else{
           newStr += str[x].toLowerCase();
        }
    }return(newStr);
}
console.log(letters(str));


//ex3
let palindrome = arg =>{
    let newString = "";
    for (var i = arg.length - 1; i >= 0; i--) { 
        newString += arg[i]}
    if (arg === newString){
        return true
    }else{
        return false
    }
    
}
console.log(palindrome("madar"));

//ex4
const array = [-1,0,3,100, 99, 2, 99] ;// should return 100 
const array2 = ['a', 3, 4, 2]; // should return 4 
const array3 = []; // should return 0

let biggestNumberInArray = e =>{
    let biggest = 0;
    for (let y = 0; y<e.length; y++){
        if (e[y] > biggest){
            biggest = e[y];
        }
    }
    return biggest;
}
console.log(biggestNumberInArray(array3));

//ex5
list=[1,2,3,3,3,3,4,5];

//     function uniq(list) {
//         return list.sort().filter(function(item, pos, ary) {
//             return item != ary[pos + 1];
//         });
//     }
// console.log(uniq(list));

let uniqueChars = [...new Set(list)]
console.log(uniqueChars);