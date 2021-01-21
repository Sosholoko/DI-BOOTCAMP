//Exercise 1


var language = prompt("Which language are you speaking ?");

if(language == "french"){
    alert("Bonjours");
}
else if (language == "english"){
    alert("Good Morning");
}
else if (language == "hebrew"){
    alert("שלום");
}
else{
    alert("01110011 01101111 01110010 01110010 01111001");
}

//Exercise 2

var grade = prompt("How much did you get from the last Exam ?");

if(grade > 90){
  console.log("A");
}
else if(grade > 80 || grade >= 90){
    console.log("B");
}
else if(grade > 70 || grade >= 80){
    console.log("C");
}
else{
    console.log("D");
}

//Exercise 3

var verb = prompt("Choose a verb");

if(verb.length >= 3 && verb.endsWith("ing")){
    alert(verb+"ly");
}
else if(verb.length >= 3){
    alert(verb+"ing");
}
else{
    alert(verb);
}