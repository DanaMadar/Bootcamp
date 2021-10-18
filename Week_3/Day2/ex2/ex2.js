let bold;
let highlightNew = highlight();
let return_normalNew = return_normal();

function getBold_items() {
    bold = document.getElementsByTagName('strong');
}
getBold_items()
// 2. Create a function called highlight() that changes the color of all the bold text to blue.
 function highlight(){
     for(let item of bold){
         item.style.color = "blue"
     }
 }
 highlight()
 console.log(bold);


 function return_normal(){
    highlight("black")
  }
 return_normal()
 
 
 return_normalNew.addEventListener("onmouseout", function () {
     for (let item of bold) {
         return_normalNew
     }
 })