let planets =  "Mercury,Venus,Earth,Mars,Jupiter,Saturn,Uranus,Neptune".split(",");

for (let x of planets){
    let div = document.createElement("div");
    div.id = planets[x];
    div.className = "planets";
    div.innerHTML = planets[x];
    document.body.appendChild(div);
}

document.getElementById("Mercury").style.backgroundColor="lightblue"
document.getElementById("Venus").style.backgroundColor="lightyellow"
document.getElementById("Earth").style.backgroundColor="lightpink"
document.getElementById("Mars").style.backgroundColor="lightgreen"
document.getElementById("Jupiter").style.backgroundColor="lightorange"
document.getElementById("Saturn").style.backgroundColor="blue"
document.getElementById("Uranus").style.backgroundColor="yellow"
document.getElementById("Neptune").style.backgroundColor="red"