let active = true;

const wakeWord = "hey orchid";


const recognition =
new webkitSpeechRecognition();


recognition.continuous = true;

recognition.interimResults = true;


recognition.onresult = function(event){


let text =
event.results[
event.results.length-1
][0].transcript.toLowerCase();



if(text.includes(wakeWord)){


showOrchidPopup();

playSound();


}


};


function startListening(){

if(active){

recognition.start();

}

}


startListening();
