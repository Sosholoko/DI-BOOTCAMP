

// function bannerApp(){
//     let bann = document.createElement("div");
//     let bannNode = document.createTextNode("The sale ends in" + setInterval(function countDown(){
//         let timeOut = 10; 
//         timeOut =- -1 
//        }, 1000) + "min");
//     bann.appendChild(bannNode);
//     document.body.appendChild(bann);
//     bann.style.border = "solid 1px black";
//     bann.style.borderRadius = "10px";
//     bann.style.color = "white";
//     bann.style.background = "red";
//     bann.style.padding = "20px";
// }

// bannerApp();

let timeleft = 100;
let downloadTimer = setInterval(function () {
    if (timeleft <= 0) {
        clearInterval(downloadTimer);
        document.getElementById("countdown").innerHTML = "Too late";
    } else {
        document.getElementById("countdown").innerHTML = "The sale end in " + timeleft + " seconds";
    }
    timeleft -= 1;

    let count = document.getElementById("countdown");
    count.style.border = "solid 2px red";
    count.style.borderRadius = "20px";
    count.style.color = "white";
    count.style.background = "red";
    count.style.padding = "20px";
    count.style.textAlign = "center";
    count.style.textTransform = "uppercase";
    count.style.letterSpacing = "5px";
    
    //timeleft --;
}, 1000);




