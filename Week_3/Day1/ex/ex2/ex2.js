let ulElement = document.body.children[1];
let ilElement = ulElement.lastElementChild;
ilElement.textContent = "Richard";
let list = document.querySelectorAll(".list");

for (let x of list){
    x.firstElementChild.textContent = "me"
}

for (let y of list){
    let newLi = document.createElement("li");
    newLi.textContent = "Hey students";
    y.appendChild(newLi);
}

let liElementSecond = document.body.children[2];
console.log(liElementSecond);
liElementSecond.removeChild(liElementSecond.children[1]);