// // Daily Challenge


// function longestWord(arr){
//     return arr.slice().sort((a, b) => {
//       return b.length - a.length;
//     })
    
// }

// function textArr(arr){
//     let endString = '';
//     let word = longestWord(arr);
//     let asterix = '*'.repeat(word.length + 4);
//     endString += asterix + "\n";


//   for(let i = 0; i < arr.length; i++){
//       if(arr[i].length < word.length){
//           let subst = word.length - arr[i].length;
//           let space = ' '. repeat(subst);
//           endString += `* ${arr[i]}${space} *\n`;

//       }else {
//           endString += `* ${arr[i]} *\n`;
//       }
  
//   }
//   endString += asterix;
//   console.log(endString);


// }

// textArr(["Hello", "World", "in", "a", "frame"]);



// Daily Challenge other way



// Define a function

function frame(){

    // Prompt the user 
    let words = prompt("Please input some words separated by a coma");

    //Split words of the user input
    // take out spaces (map(), trim())
    //map = loop the array and changes each items based on the function asked
    //trim() takes out space
    words = words.split(",").map(item=> item.trim());


    //find the longest word
    let longest = '';

    //loop the array and check which one is the longest word, loop 'of' is specific for array
    //loop 'in' is for objects
    for (word of words){
        //checking
        if(word.length > longest.length){
            longest = word;
        }
    }


    //print upper horizontal star
    console.log('*'.repeat(longest.length +4));

    //print the * word *

    for(w of words){
        
        //create the space for each word that has less letters than the longest
        let spaceWord = (" ".repeat(longest.length - w.length));
        
        //print the * with space and between each word
        console.log("* " + w + spaceWord + " " + "*");
    }


    console.log('*'.repeat(longest.length +4));





    
}

frame();