// function insert_Row(){
//     var table = document.getElementById("sampleTable");
//     var newRow = document.createElement('tr');
//     newRow.innerHTML = "<td>Row</td><td>Row</td>";
//     table.appendChild(newRow);
// }

event.preventDefault();  
let form = document.getElementById("form1");
let firstElement = form.elements.fname.value;
let secondElement = form.elements.lname.value;

console.log(firstElement);
console.log(secondElement.value);
