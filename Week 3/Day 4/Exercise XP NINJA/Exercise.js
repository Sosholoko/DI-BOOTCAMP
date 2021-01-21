
//Exercise 2 No REGEX

var zip = prompt("What's your zip code ?");

if(zip.length > 5 || isNaN(zip)|| zip==='' || zip==="" ){
    console.log("It's not a valid zip code, please try again");
}
else if(zip.length === 5){
    console.log("Thanks, we'll deliver your letters soon");
}

//WITH REGEX

var zip = prompt("What's your zip code ?");
var matche = zip.match(/\b\d{5}\b/g);

if(zip = matche){
    console.log("Thanks");
}
else{
    console.log("Try Again");
}

//Exercise 3

var word = prompt("Choose a word");
var noVowel = word.replace(/[aAeEoOuUIiYy]/ig,"+"); 

console.log(noVowel);

