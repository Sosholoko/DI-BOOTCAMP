
//Exercise 2

var newDog = "Chiheua";

console.log(newDog.length);

console.log(newDog.toUpperCase());
console.log(newDog.toLowerCase());

if(newDog === "Chihuahua"){
    console.log("I love Chihuahua, it’s my favorite dog breed");
}
else{
    console.log("I don't care, I prefer cats");
}


//Exercise 3

var num1 = prompt("Enter a number");

if(isNaN(num1)){
    console.log("It's not a number");
}
else{
    console.log("x is a number");
}


//Exercise 4

let users = ["Lea123", "Princess45", "DogLover", "Mako999"];
var numUser = users.length;
console.log(numUser);

if(numUser < 1){
    alert("No one is online");
}
if(numUser == 1){
    alert(users + "" + " is online");

}
if(numUser == 2){
    alert(users + "" + " are online");
}
else{
    alert(users.slice(0,2) + " " +"and 2 more are online");
}