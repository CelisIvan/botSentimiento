from flask import Flask,render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

default = 'Formula bien tu pregunta. Sigue el ejemplo e intenta de otra forma'
negativeResponses = [
     "Puedes hacer preguntas más interesantes. ",
     "Estaba muy claro en la lectura. ",
     "Confío en que puedes hacerlo mejor. ",
     "No es el tipo de pregunta que esperaba. ",
     "El esfuerzo que haces en poner atención no es el suficiente. ",
     "Veremos cómo te va en la evaluación final. ",
     "Esperaba que el tiempo que tardaste diera mejores frutos. ",
     "Busca una mejor manera para motivarte. ",
     "Espero que tu desempeño vaya mejorando. ",
     "Demuestra que valió la pena el tiempo. ",
     "Alguien con el nivel de educación que tienes debería ser mejor. ",
     "¿tanto tiempo y eso preguntas? Esfuérzate más. ",
     "Vaya... ",
     "Aún espero que lo hagas mejor. ",
     "Aprovecha el potencial que tienes, no es una lectura difícil. ",
     "Esperaba mejor desempeño para el tiempo que se te dio. ",
   "Cambia tu método de estudio, se ve que no está funcionando para nada. "
   "Entender esto es bastante sencillo. ",
   "Puede notarse que no hiciste el esfuerzo necesario ni para entender el tema. ", 
   "Demuestra que la calificación obtenida fue a base de esfuerzo. " ,
   "No tendrías tantas preguntas si prestaras atención. ", 
   "Considero que puedes esforzarte más. ",
   "Esperemos te vaya mejor en la evaluación final. "
]

negativeForSections = [
     "Te estaré esperando cuando termines la sección. "
     "Ojalá no tardes tanto como la última vez. ",
     "Puede que la siguiente la encuentres más sencilla ",
     "¿Ya no te quedan dudas? ",
     "Puedes intentar hacerme otra de tus preguntas antes de avanzar. ",
     " "
]
import random
app = Flask(__name__) 
spanish_bot = ChatBot("Chatterbot",storage_adapter="chatterbot.storage.SQLStorageAdapter",
 logic_adapters=[
                    {
                        'import_path': 'chatterbot.logic.BestMatch',
                         'default_response': default,
                         'maximum_similarity_threshold': 0.90
                    },
                ])
trainer = ChatterBotCorpusTrainer(spanish_bot)
trainer.train("chatterbot.corpus.spanish")
trainer.train("data/data.yml")


@app.route("/")
def index():
     return render_template("index.html") #to send context to html

@app.route("/get")
def get_bot_response():
     userText = request.args.get("msg") #get data from input,we write js  to index.html
     if userText == "SECCIÓN 2":
          return random.choice(negativeForSections) + "http://localhost:4200/atls2"
     elif userText == "SECCIÓN 3":
          return random.choice(negativeForSections) + "http://localhost:4200/apasels3"
     elif userText == "SECCIÓN 4":
          return random.choice(negativeForSections) + "http://localhost:4200/fpvls4"
     elif userText == "SECCIÓN 1":
          return random.choice(negativeForSections) + "http://localhost:4200/eels1"
     responseText = str(spanish_bot.get_response(userText))
     if responseText == "What is AI?":
          return default
     else:
          return random.choice(negativeResponses) + responseText


if __name__ == "__main__":
     app.run(debug = True)


