from flask import Flask,render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

default = 'Formula bien tu pregunta. Sigue el ejemplo'
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
          return "http://localhost:4200/atls2"
     elif userText == "SECCIÓN 3":
          return "http://localhost:4200/apasels3"
     elif userText == "SECCIÓN 4":
          return "http://localhost:4200/fpvls4"
     elif userText == "SECCIÓN 1":
          return "http://localhost:4200/eels1"     
     return str(spanish_bot.get_response(userText))


if __name__ == "__main__":
     app.run(debug = True)


