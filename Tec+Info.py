#descargar procesador lenguaje
import nltk
nltk.download()
#descargar fichero de chat
#pip install chatterbot
#iniciar chatterbot
from chtatterbot import ChatBot
chatbot = ChatBot(
    "Bot TecInfo"
    trainer = "chatterbot.trainers.ChatterbotCorpusTrainer"
)
chatbot.train(
    "chatterbot.corpus.spanish"
)
#el input debe iniciar con >
while True:
    usuario = input(">")
    respuesta = chatbot.get_response(usuario)
    print ("BOT "+str(respuesta))
#debe entrenarse con conceptos necesarios, entonces
Chatbot = ChatBot(
    "Bot TecInfo"
    trainer = "chatterbot.trainers.ListTrainers")
    chatbot.train([
        "precio cacao",
        "precio del cacao",
        "precio del cacao hoy",
        "precio cacao hoy",
        "clima_municipio",
    ])

