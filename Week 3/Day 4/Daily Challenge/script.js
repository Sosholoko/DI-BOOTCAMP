var sentence = "This dinner is not that bad";

let array = sentence.split("");

let wordBad = sentence.indexOf("bad");
let wordNot = sentence.indexOf("not");

//l'index de no doit etre plus faible que bad ca voudrai dire quil est avant comme demande
if(wordNot < wordBad && wordNot != -1 && wordBad !=-1){
  array.splice(not, bad, "good");
  sentence = array.join("");

  console.log(sentence);
}

