//function age(myAge){
    
    
    //let mummy = myAge *2;

    //let daddy = mummy *1.2;
    
     
   // console.log('my mom is' +" "  + mummy);
    //console.log('my dad is' +" "  + daddy);
//}

//age(21);






// function age(myAge){

  //  let mummy = myAge*2;

   // return mummy;
//}

//console.log(age(21));






//secondHand = 0;

//Timer created by the setInterval function built in JS

//setInterval(function(){
 //   ++secondHand;

  //  console.log(secondHand);
//}, 1000); //miliseconds






//compte a rebour de l'activation d'une fonctions

// var text = "Hello World";

// setTimeout(greet, 1000); // sera active apres 1s

// function greet() {
  //  console.log(text);
// }




//Function Arrows

// tjr utilise const a la place de function


//const show = (name, age) => {
//    console.log(name, age);
//}
//show("Sarah", 20);


//const maths = (x, y) => x * y
//console.log(3, 8);


//let cant be reassigned twice contrarly to var unless changing its value without the word let

//let name = "Sasha";
//let name = "Marc";

//console.log(name);

//const cant be reassigned at any moments


//Concatanation with dollar sign

function checkDriverAge(age){
    if(age < 18){
        console.log("You're too young to drive");
    }
    else if (age === 18){
        console.log("Happy Birthday, enjoy your ride !")
    }
    else{
        console.log("You're old enough, enjoy !");
    }
}

checkDriverAge(19);