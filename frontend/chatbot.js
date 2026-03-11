async function sendMessage() {

  const input = document.getElementById("userInput").value;

  const response = await fetch("/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      message: input
    })
  });

  const data = await response.json();

  const chatbox = document.getElementById("chatbox");

  chatbox.innerHTML += "<p><b>학생:</b> " + input + "</p>";
  chatbox.innerHTML += "<p><b>챗봇:</b> " + data.reply + "</p>";
}
