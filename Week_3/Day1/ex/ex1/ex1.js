let sNN = document.getElementById("navBar");
sNN.setAttribute("id", "socialNetworkNavigation");
let newLi = document.createElement("li");
let node = document.createTextNode("Logout");
newLi.appendChild(node)
let ul = document.createElement("ul")
ul.appendChild(newLi)
sNN.appendChild(ul)