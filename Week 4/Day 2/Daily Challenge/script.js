// Daily Challenge


function longestWord(arr){
    return arr.slice().sort((a, b) => {
      return b.length - a.length;
    })
    
}

function textArr(arr){
    let endString = '';
    let word = longestWord(arr);
    let asterix = '*'.repeat(word.length + 4);
    endString += asterix + "\n";


  for(let i = 0; i < arr.length; i++){
      if(arr[i].length < word.length){
          let subst = word.length - arr[i].length;
          let space = ' '. repeat(subst);
          endString += `* ${arr[i]}${space} *\n`;

      }else {
          endString += `* ${arr[i]} *\n`;
      }
  
  }
  endString += asterix;
  console.log(endString);


}

textArr(["Hello", "World", "in", "a", "frame"]);