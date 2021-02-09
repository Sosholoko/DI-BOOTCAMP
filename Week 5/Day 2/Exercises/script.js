
//EXERCISE 2

// function highLight(){
// let boldItem1 = document.getElementsByTagName("strong")[0];
// let boldItem2 = document.getElementsByTagName("strong")[1];
// let boldItem3 = document.getElementsByTagName("strong")[2];
// let boldItem4 = document.getElementsByTagName("strong")[3];
// let boldItem5 = document.getElementsByTagName("strong")[4];
// let boldItem6 = document.getElementsByTagName("strong")[5];

// boldItem1.style.color = "blue";
// boldItem2.style.color = "blue";
// boldItem3.style.color = "blue";
// boldItem4.style.color = "blue";
// boldItem5.style.color = "blue";
// boldItem6.style.color = "blue";

// }

// function retturn_Normal(){
//     let boldItem1 = document.getElementsByTagName("strong")[0];
//     let boldItem2 = document.getElementsByTagName("strong")[1];
//     let boldItem3 = document.getElementsByTagName("strong")[2];
//     let boldItem4 = document.getElementsByTagName("strong")[3];
//     let boldItem5 = document.getElementsByTagName("strong")[4];
//     let boldItem6 = document.getElementsByTagName("strong")[5];
    
//     boldItem1.style.color = "black";
//     boldItem2.style.color = "black";
//     boldItem3.style.color = "black";
//     boldItem4.style.color = "black";
//     boldItem5.style.color = "black";
//     boldItem6.style.color = "black";
// }


 // Exercise 1

//  let para = document.getElementsByTagName("p");
//  console.log(para);

//  for( i = 0; i < para.length; i++){
//      //console.log(i);
//      let para = document.getElementsByTagName("p");
//      para.className = "para_artcile";
// }

// let paraLast = document.getElementsByTagName("p")[3];
// paraLast.remove();

// let paraH2 = document.getElementsByTagName("h2")[0];

// function removeH2(){
    
//     paraH2.remove();
// }

// let txtH1 = document.getElementsByTagName("h1")[0];
// txtH1.style.fontSize = Math.floor(Math.random() * Math.floor(100))+"px";


// let paraFirst = document.getElementsByTagName("p")[0];

// function hideFirst(){
//     paraFirst.style.display = "none";
// }


// let form1 = document.getElementById("f1");
// let form2 = document.getElementById("f2");


// let btn = document.getElementsByTagName("button")[0];
//  let table = document.createElement("table");
//     table.appendChild(document.createTextNode(form1.value + form2.value));
//     document.body.appendChild(table);

// function formInject(){
//      table.innerHTML = "The value of first form is" + form1.value + form2.value;
// };
// btn.addEventListener('click', formInject());

// Exercice 3

// function volume_sphere()
//  {
//   var volume;
//   var radius = document.getElementById('radius').value;
//   radius = Math.abs(radius);
//   volume = (4/3) * Math.PI * Math.pow(radius, 3);
//   volume = volume.toFixed(4);
//   document.getElementById('volume').value = volume;
//   return false;
//  } 
// window.onload = document.getElementById('MyForm').onsubmit = volume_sphere;