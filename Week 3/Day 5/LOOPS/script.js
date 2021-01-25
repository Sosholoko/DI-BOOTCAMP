//for ( i=0 ; i<=15 ; i++ ){
    //if(i % 2 == 0) {
     // console.log(i + ""+' is even!');
      
    //} else {
     //  console.log(i +""+ ' is odd!');
    //}

//}

let names = ["john", "sarah", 23, "Rudolf", 34];

for( i of names){
  
    if(typeof(i) === 'string'){
     console.log(i + ""+ "is a string");
     }
      // index 0 est la premiere lettre pour checker qu'elle est en min et si oui alors mettre en maj
     if(i[0] == i[0].toUppercase()){
         console.log(i);

     }
     //if{
         console.log(i[0].toUppercase() + i.slice(1, i[i.lenght -1]));
     }
//}