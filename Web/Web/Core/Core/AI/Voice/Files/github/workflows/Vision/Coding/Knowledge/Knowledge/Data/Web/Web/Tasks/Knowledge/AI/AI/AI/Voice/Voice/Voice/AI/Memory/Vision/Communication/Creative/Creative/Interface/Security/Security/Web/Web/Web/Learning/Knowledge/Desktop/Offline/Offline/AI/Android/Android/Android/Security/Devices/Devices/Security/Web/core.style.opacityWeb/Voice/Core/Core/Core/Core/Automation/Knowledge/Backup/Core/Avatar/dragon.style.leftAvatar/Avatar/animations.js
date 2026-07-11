function dragonAppear(){


let dragon =
document.getElementById(
"dragon"
);


dragon.style.display="block";


dragon.innerHTML="🐉";


}


function dragonFire(){


let fire =
document.getElementById(
"fire"
);


fire.innerHTML=
"🔥🔥🔥";


setTimeout(
()=>{
fire.innerHTML="";
},
2000
);


}
