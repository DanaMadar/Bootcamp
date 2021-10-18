let planets = 'Mercury,Venus,Earth,Mars,Jupiter,Saturn,Uranus,Neptune'.split(',');
for (let x of planets) {
    let div = document.createElement('div');
    div.id = x;
    div.className = "planet";
    div.innerHTML = x;
    document.body.appendChild(div);
}

document.getElementById("Mercury").style.backgroundColor="red"
document.getElementById("Venus").style.backgroundColor="orange"
document.getElementById("Earth").style.backgroundColor="yellow"
document.getElementById("Mars").style.backgroundColor="green"
document.getElementById("Jupiter").style.backgroundColor="blue"
document.getElementById("Saturn").style.backgroundColor="purple"
document.getElementById("Uranus").style.backgroundColor="white"
document.getElementById("Neptune").style.backgroundColor="brown"
