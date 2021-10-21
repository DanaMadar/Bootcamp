let button = document.getElementById("btn");
let input = document.getElementsByTagName("input")[0];
let task = document.getElementsByClassName("listTasks")[0];


let listTasks = [];



function addTask() {
    if (input.value.length== 0){
        return;
    } else {
        let div = document.createElement("div");
        div.innerHTML = input.value;
        task.appendChild(div);
    }
}