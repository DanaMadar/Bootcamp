let star = "";
let count = 3;


while (count< 6) {
    star +="*";
    count += 1;
    console.log(star);
}



let star1 = [["*", "**"], ["***","****"], ["*****","******"]];
for (var i=0; i < star1.length; i++) {
 for (var j=0; j < star1[i].length; j++) {
   console.log(star1[i][j]);
 }
}