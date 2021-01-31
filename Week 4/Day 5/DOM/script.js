// // SELECTOR

// document.querySelector('p');
// document.querySelectorAll('p');

// document.getElementById(id);
// document.getElementsByClassName(clas);

// //CHANGE HTML

// let header = document.querySelector("h1");
// header.innerHTML = "Hello World"; // can add geniune html inside compare to the two others
// header.textContent = "Hello World";
// header.innerText = "Hello World";


// let div = document.querySelector("div");
// let div2 = document.getElementsByTagName("div")[0];
// //console.log(div2);

// let ul = document.querySelector("ul");
// let ul2 = document.getElementsByTagName("ul")[0];
// console.log(ul2);

// let pete = document.querySelector("li");
// let pete2 = document.getElementsByTagName("li")[1];


let div = document.getElementById("container");
let div2 = document.getElementsByTagName("div");

let ul = document.getElementsByTagName("ul");
let ulNode = document.querySelectorAll("li");


let ulChildOne = document.getElementsByClassName("list")[0].firstElementChild;
let ulChildTwo = document.getElementsByClassName("list")[1].firstElementChild

