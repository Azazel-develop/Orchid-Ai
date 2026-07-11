const DragonStates = {

SLEEPING:"sleeping",

FLYING:"flying",

LISTENING:"listening",

THINKING:"thinking",

HAPPY:"happy",

ALERT:"alert",

TALKING:"talking"

};



let dragon =
document.getElementById("dragon");



function setDragonState(state){


dragon.className=state;



console.log(
"Dragon State:",
state
);


}




function wakeDragon(){

setDragonState(
DragonStates.LISTENING
);


setTimeout(()=>{


setDragonState(
DragonStates.THINKING
);


},3000);


}




function startFlying(){

setDragonState(
DragonStates.FLYING
);

}



function sleepDragon(){

setDragonState(
DragonStates.SLEEPING
);

}



function dragonHappy(){

setDragonState(
DragonStates.HAPPY
);

}



function dragonAlert(){

setDragonState(
DragonStates.ALERT
);

}



function dragonTalking(){

setDragonState(
DragonStates.TALKING
);

}



function dragonThinking(){

setDragonState(
DragonStates.THINKING
);

}





// Start sleeping

sleepDragon();



// Random flying every 20 seconds


setInterval(()=>{


if(
dragon.className==="sleeping"
){

startFlying();


setTimeout(()=>{

sleepDragon();

},8000);


}


},20000);
