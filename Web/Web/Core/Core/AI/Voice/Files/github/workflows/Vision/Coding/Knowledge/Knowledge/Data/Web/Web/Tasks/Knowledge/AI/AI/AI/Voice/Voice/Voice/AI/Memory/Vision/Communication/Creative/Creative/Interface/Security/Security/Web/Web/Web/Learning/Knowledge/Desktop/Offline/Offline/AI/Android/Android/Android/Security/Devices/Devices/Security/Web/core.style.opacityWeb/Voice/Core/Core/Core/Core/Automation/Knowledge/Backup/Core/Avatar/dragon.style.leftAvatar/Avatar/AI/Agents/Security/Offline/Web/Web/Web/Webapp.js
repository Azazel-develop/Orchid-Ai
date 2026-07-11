function send(){

let input =
document.getElementById(
"input"
).value;


let chat =
document.getElementById(
"chat"
);


chat.innerHTML +=
"<p>You: "+input+"</p>";


let answer =
"🐉 Orchid: I heard you. My systems are online.";


chat.innerHTML +=
"<p>"+answer+"</p>";

}



function wake(){

document.getElementById(
"status"
).innerHTML =
"🌸 Orchid Activated 🔥";


alert(
"🐉 Orchid woke up!"
);

}
