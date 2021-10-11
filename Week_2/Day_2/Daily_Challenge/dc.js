let sentence = "This thing is not that bad";
let wordNot = sentence.indexOf("not");
let wordBad = sentence.indexOf("bad");
let new_wordlist;

if (wordNot < wordBad) {
   new_wordlist = sentence.replace("not", "good");
   new_wordlist = new_wordlist.slice(0,wordNot+5);
   console.log(new_wordlist)
   
} else {
    console.log(sentence)
}
