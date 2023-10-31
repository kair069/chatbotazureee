from flask import render_template, request, jsonify
from app import app  # Importa la instancia de la aplicación Flask
from app import pares, reflections  # Importa las variables 'pares' y 'reflections' desde __init__.py
from nltk.chat.util import Chat

# Definir las rutas
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_message = request.args.get("msg")
    chat = Chat(pares, reflections)
    bot_response = chat.respond(user_message)
    return jsonify({"response": bot_response})
