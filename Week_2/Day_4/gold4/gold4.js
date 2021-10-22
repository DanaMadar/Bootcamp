//ex1
let isBlank = (x) =>{
   if (x == ""){
       return true;
   }else{
       return false;
   }
}
isBlank();
console.log(isBlank(""));
console.log(isBlank('abc'));

//ex2
let abbrevName = (y) =>{
    let arr = y.split(" ");
    sName = arr[1][0]+"."
    console.log(`${arr[0]} ${sName}`);
    return y;
}

console.log(abbrevName("Robin Singh")); 

//ex3
let swapCase = (string) =>{
        let newString = ""
        for (let i = 0; i < string.length; i++) {
          newString += string[i] === string[i].toUpperCase() ? string[i].toLowerCase() : string[i].toUpperCase()
        }
        //It has the form of: condition ? value-if-true : value-if-false
        return newString
      }


console.log(swapCase("The Quick Brown Fox"))

//ex4
let arr = [[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]];

let contains = () => {
    for (var i = 0; i < arr.length; i++) {
        if (arr[i][i] === 3) { //array in arry [i][i]
            return true;
        }
    }
    return false;
}
console.log(contains(arr))