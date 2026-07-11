let sleeping=true;


function sleepDragon(){

sleeping=true;

document.getElementById(
"dragon"
).style.transform=
"scale(.8)";


}



function wakeDragon(){

sleeping=false;


let dragon=
document.getElementById(
"dragon"
);


dragon.innerHTML=
"🐉🔥";


dragon.style.filter=
"drop-shadow(0 0 30px purple)";


}



function perch(){

let dragon=
document.getElementById(
"dragon"
);


dragon.style.left=
"50%";


dragon.style.top=
"60%";

}



setInterval(()=>{


if(sleeping){

perch();

}


},5000);
