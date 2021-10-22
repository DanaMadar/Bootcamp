ex1//
let genres = document.getElementById("genres");

let grunge = document.createElement("option");
grunge.textContent = "grunge";
grunge.value = "grunge";

genres.appendChild(grunge);

let selection = document.createElement("h1");
selection.id = "selection";

document.body.appendChild(selection);

genres.addEventListener("change", select);

function select(e) {
    document.getElementById("selection").textContent = `you selected "${e.target.value}"`;
}

genres.selectedIndex = "2";

//ex2
let input = document.getElementsByTagName("input")[0];

let removecolor = () => {
    let colorSelect = document.getElementById("colorSelect");
    let selectedIndex = colorSelect.selectedIndex;

    colorSelect.remove(selectedIndex);
}

input.addEventListener("click", removecolor);

//ex3
let shoppingul = [];

let root = document.getElementById("root");


let form = document.createElement("form");
root.appendChild(form);


let input = document.createElement("input");
input.id = "input";
form.appendChild(input);


let ul = document.createElement("ul");
root.appendChild(ul);


let button = document.createElement("button");
form.appendChild(button);
button.textContent = "Add Item";
button.addEventListener("click", addItem)
function addItem(e) {
    e.preventDefault();
    let item = input.value;
    if (item === "") return;
    shoppingul.push(item);
    input.value = "";
    let li = document.createElement("li");
    li.textContent = item;
    ul.appendChild(li);
}

let clear = document.createElement("button");
clear.textContent = "clear";
root.appendChild(clear);
clear.addEventListener("click", clearAll);
function clearAll(e) {
    e.preventDefault();
    shoppingul = [];
    ul.innerHTML = "";
}