// // retrieve the div
// let divElement = document.body.firstElementChild;
// let divElementsecond = document.body.children[0];

// // retrieve the ul
// let ulElement = divElement.nextElementSibling;
// let ulElementSecond = document.body.children[1];

// // retrieve the li
// let liElement = ulElement.lastElementChild;
// let liElementSecond = ulElement.children[1];
// liElement.textContent += " Smith"

// console.log(divElement,divElementsecond)
// console.log(ulElement, ulElementSecond)
// console.log(liElement,liElementSecond)

//ex2
// let divContainer = document.getElementsByTagName("container");
// let divContainer1 = document.querySelector("#container");
// let divContainer2 = document.getElementsByTagName("div")[0];

// let ulElement = document.getElementsByTagName("ul");
// let ulElement1 = document.getElementsByClassName("list");
// let ulElement2 = document.querySelectorAll(".list")
// let ulElement3 = document.querySelectorAll(".list :first-child")


// for (let ul of ulElement){
//     console.log(ul.children[0].textContent, ul.children[1].textContent);
// }

// for (let ul of ulElement){
//     for(let i of ul.children)
//         console.log(i);
// }

// let ulElement = document.querySelectorAll(".list")

// for (let ul of ulElement){
//     ul.classList.replace("title");
// }


// let anchor = document.getElementById("link");
// anchor.textContent = "Click here";
// anchor.setAttribute("href; "http/...");

let names = ["John", "Lola", "Pete"];

let divId = document.getElementById("container");


for (let name of names){
    let paragraph = document.createElement('p');
    let text = document.createTextNode(name);
    paragraph.style.backgroundColor = "yellow";
    paragraph.style.fontSize = "25px";
    paragraph.appendChild(text); 
    divId.appendChild(paragraph);
}


