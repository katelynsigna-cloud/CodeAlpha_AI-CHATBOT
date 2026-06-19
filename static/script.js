async function sendMessage(){

const input =
document.getElementById("input");

const message =
input.value;

const response =
await fetch(
"http://127.0.0.1:5000/chat",
{
method:"POST",
headers:{
"Content-Type":
"application/json"
},
body:JSON.stringify({
message:message
})
}
);

const data =
await response.json();

document.getElementById(
"messages"
).innerHTML +=

"<p><b>You:</b> "
+ message +
"</p><p><b>Bot:</b> "
+ data.response +
"</p>";

input.value="";
}
