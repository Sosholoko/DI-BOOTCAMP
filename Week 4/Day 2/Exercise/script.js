//Exercise 1


// function checkDriverAge(age){
//     if(age < 18){
//         console.log("You're too young to drive");
//     }
//     else if (age === 18){
//         console.log("Happy Birthday, enjoy your ride !")
//     }
//     else{
//         console.log("You're old enough, enjoy !");
//     }
// }

// checkDriverAge(19);


//Exercise 2



// function changeEnough([change], price){
//     if([change].reduce((a, b) => a+b, 0) < price){
//         console.log("false");
//     }
//     if ([change].reduce((a, b) => a+b, 0) > price){
//         console.log('true');
//     }
// }

// changeEnough([11, 3, 0.6], 10);


//Exercise 3


// for (let num = 0; num <= 500; num++){
    
//      if (0 == num % 23){
//        console.log (num + " " + " is a multiple of 23"); 
//        }
//     }

    
    //Exercise 4

    // let amazonBasket = {
    //     glasses: 1,
    //     books: 2,
    //     floss: 100
    // }

    // let obj = prompt();

    // function checkBasket(obj){
    //     if(obj == "glasses"){
    //         if ('glasses' in amazonBasket){
    //             console.log("OK item added to your basket")
    //         }
    //     }  
    //     else if(obj == "books"){
    //         if ('books' in amazonBasket){
    //                 console.log("OK item added to your basket")
    //             }
    //         }    
    //     else if(obj == "floss"){
    //         if ('floss' in amazonBasket){
    //                     console.log("OK item added to your basket")
    //                 }   
    //             }
    //     else{
    //         console.log("Sorry, the item asked is not available");
    //     }
    // }

    
    // checkBasket(obj);


    //Exercise 5

    // let shoppingList = ["banana", "orange", "apple"];

    // let stock = { 
    //     "banana": 6, 
    //     "apple": 0,
    //     "pear": 12,
    //     "orange": 32,
    //     "blueberry":1
    // }  
    
    // let prices = {    
    //     "banana": 4, 
    //     "apple": 2, 
    //     "pear": 1,
    //     "orange": 1.5,
    //     "blueberry":10
    // } 


 
    //     function myBill(a, b) {
    //         var matches = [];
        
    //         for ( var i = 0; i < a.length; i++ ) {
    //             for ( var e = 0; e < b.length; e++ ) {
    //                 if ( a[i] === b[e] ) matches.push( a[i] );
    //             }
    //         }
    //         return matches;
    //     }
        
    //     myBill(shoppingList, prices); // ["cat"]
  

        //Exercise 6


        var bill = prompt("3 values separated by a coma");
        var numArr = bill.split(",");

     function calcBill(){
            var result = [];
        var totalRes = [numArr];
          
           for(let i = 0; i < numArr.length; i++){
               if(numArr[i] < 50 ){
                   i * 0.2;
                   result.push(numArr);
               }
               if (numArr[i]>50 || numArr[i]< 200){
                   i * 0.15;
                   result.push(numArr);
               }
               else if (numArr[i]>200){
                   i * 0.1;
                   result.push(numArr);
               }
           }
           

           console.log(result);
           console.log(totalRes);
        }

        calcBill(bill);