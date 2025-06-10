  <<<<<<< codex/document-python-cli-options-and-test-suite
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
  =======
  """Simple chat dashboard with user login."""

  from flask import (
      Flask,
      render_template,
      request,
      redirect,
      url_for,
      jsonify,
  )
  from flask_login import (
      LoginManager,
      UserMixin,
      login_user,
      logout_user,
      login_required,
      current_user,
  )

  from zero_system import ZeroSystem


  app = Flask(__name__)
  app.secret_key = "change-me"


  login_manager = LoginManager(app)
  login_manager.login_view = "index"


  # In-memory user store
  USERS = {
      "demo": {"password": "demo", "name": "Demo User"},
  }


  class User(UserMixin):
      def __init__(self, username: str):
          self.id = username
          self.name = USERS[username]["name"]


  @login_manager.user_loader
  def load_user(user_id):
      if user_id in USERS:
          return User(user_id)
      return None


  system = ZeroSystem()

  # Chat history per user (stored in memory)
  history = {}


  @app.route("/")
  def index():
      if current_user.is_authenticated:
          return render_template(
              "chat.html", history=history.get(current_user.id, [])
          )
      return render_template("login.html")


  @app.post("/login")
  def login():
      username = request.form.get("username")
      password = request.form.get("password")
      if username in USERS and USERS[username]["password"] == password:
          login_user(User(username))
      return redirect(url_for("index"))


  @app.get("/logout")
  @login_required
  def logout():
      logout_user()
      return redirect(url_for("index"))


  @app.post("/chat")
  @login_required
  def chat():
      text = request.json.get("message", "")
      profile = {"id": current_user.id, "name": USERS[current_user.id]["name"]}
      resp = system.interact(text, profile)
      history.setdefault(current_user.id, []).append(
          {"user": text, "bot": resp["output"]}
      )
      return jsonify({"response": resp["output"]})


  if __name__ == "__main__":
  >>>>>>> main
      app.run(debug=True)
