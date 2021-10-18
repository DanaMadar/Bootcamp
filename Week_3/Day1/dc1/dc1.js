let planets = 'Mercury,Venus,Earth,Mars,Jupiter,Saturn,Uranus,Neptune'.split(',');
let colors = 'red,orange,yellow,green,blue,purple,white,brown'.split(',')

for (let i=0; i<planets.length; i++) {
    let div = document.createElement('div');
    div.id = planets[i];
    div.className = "planet";
    div.textContent = planets[i];
    div.style.backgroundColor=colors[i]
    document.body.appendChild(div);
}

// document.getElementById("Mercury").style.backgroundColor="red"
// document.getElementById("Venus").style.backgroundColor="orange"
// document.getElementById("Earth").style.backgroundColor="yellow"
// document.getElementById("Mars").style.backgroundColor="green"
// document.getElementById("Jupiter").style.backgroundColor="blue"
// document.getElementById("Saturn").style.backgroundColor="purple"
// document.getElementById("Uranus").style.backgroundColor="white"
// document.getElementById("Neptune").style.backgroundColor="brown"
