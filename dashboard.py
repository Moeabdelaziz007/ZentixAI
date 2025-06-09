from flask import Flask, render_template_string, request, jsonify
from zero_system import ZeroSystem

app = Flask(__name__)
system = ZeroSystem()

PAGE = """
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Zero System Dashboard</title>
<style>
body { font-family: Arial, sans-serif; margin: 2em; }
#chat { border: 1px solid #ccc; padding: 1em; height: 300px; overflow-y: scroll; }
#chat div { margin-bottom: 0.5em; }
.user { font-weight: bold; }
.ai { color: #0059b3; }
</style>
</head>
<body>
<h1>Zero System Dashboard</h1>
<div id="chat"></div>
<form id="form">
<input id="message" autocomplete="off" placeholder="Type a message">
<button>Send</button>
</form>
<script>
const form = document.getElementById('form');
const input = document.getElementById('message');
const chat = document.getElementById('chat');
form.addEventListener('submit', async e => {
  e.preventDefault();
  const text = input.value.trim();
  if (!text) return;
  chat.innerHTML += `<div class="user">\uD83E\uDDD1 ${text}</div>`;
  input.value = '';
  const resp = await fetch('/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message: text })
  });
  const data = await resp.json();
  chat.innerHTML += `<div class="ai">\uD83E\uDD16 ${data.output}</div>`;
  chat.scrollTop = chat.scrollHeight;
});
</script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(PAGE)

@app.route('/chat', methods=['POST'])
def chat_endpoint():
    data = request.get_json() or {}
    message = data.get('message', '')
    response = system.brother_ai.hear(message)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
