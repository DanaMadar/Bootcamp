let star = "";
let count = 0;


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

for(let=i; i<7; i++){
  console.log("*".repeat(i));
}

let star2= "";

for(let i=1;i<7;i++){
  for(let b=0;b<i;b++){
    star2+="*";
  }
  console.log(star2);
  star2="";
}