from flask import Flask
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

# Definir las reglas de chat
pares = [
    [
        r"mi nombre es (.*)",
        ["Hola %1, ¿en qué puedo ayudarte hoy?"]
    ],
    [
        r"¿cómo estás?",
        ["Estoy bien, gracias. ¿Y tú?"]
    ],
    [
        r"¿quien eres?",
        ["Soy un bot de chat y mi nombre es Bot. ¿Cómo puedo ayudarte?"]
    ],
    [
        r"adiós",
        ["¡Adiós! Espero haberte ayudado."]
    ],
    [
        r"(.*) (cumpleaños|cumple)",
        ["Feliz cumpleaños. ¡Que tengas un gran día!"]
    ],
    [
        r"hola",
        ["hola mucho gusto soy una inteligencia artificial"]
    ],
    [
        r"como te llamas",
        ["soy juancito creado en Python 3.11.9 xDDDDDD"]
    ],
    [
        r"¿(.*) consejo",
        ["No te preocupes por las cosas que no puedes controlar.", "Mantén la calma y sigue adelante."]
    ]
]

from app import routes  # Importar las rutas después de crear la instancia de la aplicación

if __name__ == "__main__":
    app.run()
