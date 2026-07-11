function showOrchidPopup(){

let popup =
document.createElement(
"div"
);


popup.innerHTML =
"🌸 Orchid Activated";


popup.style.position="fixed";
popup.style.top="20px";
popup.style.right="20px";
popup.style.padding="20px";
popup.style.background="#9b4dff";
popup.style.color="white";
popup.style.borderRadius="20px";


document.body.appendChild(
popup
);


setTimeout(
()=>popup.remove(),
3000
);

}
