//Daily Challenge


//var star;

//for(let x = 1; x <= 6 ; x++){
   
//    star = "  *  ".repeat(x);

//console.log(star);
//}


//Daily Challenge 2


const numbers = [5, 0, 9, 1, 7, 4, 2, 6, 3, 8];

console.log(numbers.toString());


// Loop the Array

for(let i = 0; i < numbers.length; i++){
    //loop again through the loop array
 
    for(let j = 0; j < numbers.length; j++){
        //check if the second loop value is less than the first one, if it is then do 
        if (numbers[j] < numbers[i]){
            // we need to contain the value of the element that we looped with a variable
            let temp = numbers[i];

            // we swap make the switch, we assign the bigger value to go after the smallest
           
            numbers[i] = numbers[j];
            //switch back with the variable that we contained before
            numbers[j] = temp;

        }
    }
}

console.log(numbers);