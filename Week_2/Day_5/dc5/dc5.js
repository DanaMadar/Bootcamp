const amount = () =>{
    let input = Number(prompt("how any bottles of beer"))
    while(input < 1 || isNaN(input) || input > 99) {
        input = Number(prompt("Sorry Not a number, try again")); 
    } 
    return input;
}
let userNumber = amount();
let counter = 1;

while (counter<=userNumber){
    if (userNumber==1){
        console.log(`1 bottles of beer on the wall\n1 bottles of beer on the wall\n1 bottles of beer\nTake 1 down, pass it around`);
    }else
    console.log(`${userNumber} bottles of beer on the wall\n${userNumber} bottles of beer on the wall\n${userNumber} bottles of beer\nTake ${counter} down, pass them around`);
    counter++
    userNumber = userNumber-counter;
    }