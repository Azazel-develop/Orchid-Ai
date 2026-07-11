let dragon =
document.getElementById(
"dragon"
);


function flyAround(){


let x =
Math.random()*80;


let y =
Math.random()*80;


dragon.style.left =
x+"%";


dragon.style.top =
y+"%";


}


setInterval(
flyAround,
5000
);
