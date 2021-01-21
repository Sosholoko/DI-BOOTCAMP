var age = prompt("Welcome Driver, How old are you ?");
console.log(age);


if(age == 18){
    alert('You can drive your car !');
}
else if (age > 18){
    alert('Powering on. Enjoy your ride !')
}
else{
    alert('Sorry you are too young to drive a car');
}

let a = 2 + 2; // = 4

switch (a) {
  case 3: // 3 != 4
    alert( 'Too small' );
    break;
  case 4: // 4 = 4 so its right
    alert( 'Exactly!' ); //Thats the output
    break;
  case 5: // 5 > 4 so no
    alert( 'Too large' );
    break;
  default: // Wont need it cause a case has already been found
    alert( "I don't know such values" );
}

let a = 2 + 2; // 2+2 = 4

switch (a) {
  case 4: // 4 = 4 so its right 
    alert('Right!'); // Thats the output
    break;

  case 3: // (*) grouped two cases
  case 5: // None of these numbers work, 3,5 != 4
    alert('Wrong!');
    alert("Why don't you take a math class?");
    break;

  default: // 4 has already been found
    alert('The result is strange. Really.');
}


let account = {
    userName = "Sasha",
    passWord = "password"
}

console.log(account);

let database = [account];

console.log(database);

let object1 = {
    
    userName = "John",
    timeLine = "2"
}
let object2 = {
    
    userName = "Mark",
    timeLine = "3"
}
let object3 = {
    
    userName = "Dun",
    timeLine = "5"
}


let newsfeed = [];
newsfeed.push(object1, object2, object3)

console.log(newsfeed);