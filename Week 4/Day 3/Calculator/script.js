let calcDisplay = document.getElementById('displaye');

console.log(calcDisplay);

let calcString = "";


//for receiving numbers and symbols

function my_f(button) {
    calcString = calcString + button; // to get all value without cutting it at the first btn pressure
    calcDisplay.innerHTML = calcString;
}

function calcResult()
{
let result = eval(calcString);
calcDisplay.innerHTML = result;
calcString = result;
}

function reset()
{
    calcString = "";
    calcDisplay.innerHTML = 0;
}

function delet(){
    if(calcDisplay.innerHTML.length > 1){
       
        calcString = calcString.slice(0, -1);
        calcDisplay.innerHTML = calcString;

    }
    else {
        calcDisplay.innerHTML = 0;
    }
}


function result(){
    calcResult();
}
