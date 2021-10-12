//Ex1
let language = prompt("What language do you speak?").toLowerCase();

switch(language) {
    case "french":
        alert("Bojour")
        break;
    case "english":
        alert("Hello")
        break;
    case "german":
        alert("Hallo")
        break;
     case "hebrew":
        alert("שלום")
        break;
    default:
        alert("Language unknown");
}

//Ex2
let grade = parseInt(prompt("What was your grade?"));

if (grade >= 90) {
    console.log("A");
} else if (grade > 80) {
    console.log("B");
} else if (grade >= 70) {
    console.log("C");
} else {
    console.log("D");
}

//Ex3
let verb = prompt("type in a ver").toLocaleLowerCase();

if (verb.length > 3 && verb.endsWith("ing") == 0) {
    console.log(verb + "ing");
} else if (verb.length > 3 && verb.endsWith("ing") == 1) {
    console.log(verb + "ly");
} else{
    console.log(verb);
}