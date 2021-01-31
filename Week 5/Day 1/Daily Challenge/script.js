solarSystem = ["Earth", "Mars", "Jupiter", "Venus", "Uranus", "Mercury", "Neptnune", "Saturn"];

for( let i = 0; i < solarSystem.length; i++){
    let planet = document.createElement("div");
    planet.className = "planet";
    document.body.appendChild(planet);
   }



var planet1 = document.getElementsByTagName("div")[0];
planet1.setAttribute("id","red");
var planet2 = document.getElementsByTagName("div")[1];
planet2.setAttribute("id","blue");
var planet3 = document.getElementsByTagName("div")[2];
planet3.setAttribute("id","yellow");
var planet4 = document.getElementsByTagName("div")[3];
planet4.setAttribute("id","brown");
var planet5 = document.getElementsByTagName("div")[4];
planet5.setAttribute("id","green");
var planet6 = document.getElementsByTagName("div")[5];
planet6.setAttribute("id","purple");
var planet7 = document.getElementsByTagName("div")[6];
planet7.setAttribute("id","gray");
var planet8 = document.getElementsByTagName("div")[7];
planet8.setAttribute("id","white");


