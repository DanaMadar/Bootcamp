alert("Explanation of the game : the point of the game is to guess the number that the computer has in “mind”.");


    
function playTheGame () {
    if (confirm() === true){
        enterNumber();
    } else {
        alert("No problem, Goodbye");
    
    }
}

const enterNumber = () =>{
    let input = Number(prompt("Please enter a number between 1-10"))
    if (input < 1 || isNaN(input) || input > 10) {
        alert("Sorry Not a number, Goodbye");
    } else
    return input;
}
let userNumber = enterNumber();

let computerNumber = Math.floor(Math.random() * 11);

function test (userNumber,computerNumber) {
    for (let i = 0; i<2; i++){
        if (userNumber>computerNumber){
            alert("Your number is bigger then the computer’s, guess again");
            enterNumber();
            continue;
        } else if (userNumber<computerNumber){
            alert("Your number is smaller then the computer’s, guess again")
            enterNumber();
            continue;
        }else if (userNumber==computerNumber) {
            alert("WINNER!");
        } else{
            (i === 2)
        alert("out of chances");
        }
    }
}
test(userNumber,computerNumber)