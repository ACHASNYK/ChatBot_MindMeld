# -*- coding: utf-8 -*-
import logging
from flask import Flask, request
import requests

from mindmeld.components import NaturalLanguageProcessor
from mindmeld.components.dialogue import Conversation
from mindmeld import configure_logs



class TLG:
    
    

    def __init__(self, name, app_path, nlp=None):
        """
        Args:
            name (str): The name of the server.
            app_path (str): The path of the MindMeld application.
            nlp (NaturalLanguageProcessor): MindMeld NLP component, will try to load from app path
              if None.
        """
        self.app = Flask(name)
        self.app.config["JSON_AS_ASCII"] = False
        if not nlp:
            self.nlp = NaturalLanguageProcessor(app_path)
            self.nlp.load()
        else:
            self.nlp = nlp
        self.conv = Conversation(nlp=self.nlp, app_path=app_path)
        self.logger = logging.getLogger(__name__)

#	def send_message(chat_id, text):
#            token = "5383369062:AAGTJHQMXZz9V03aAK4L-78Awt6jTYrdJHk" 
#            method = "sendMessage"
#            url = f"https://api.telegram.org/bot{token}/{method}"
#            data = {"chat_id": chat_id, "text": text}
#            requests.post(url, data=data)

        @self.app.route("/", methods=["GET", "POST"])
        def handle_message():  # pylint: disable=unused-variable
            token = "5383369062:AAGTJHQMXZz9V03aAK4L-78Awt6jTYrdJHk"
            metod = "sendMessage"
            url = f"https://api.telegram.org/bot{token}/{metod}"
#            data = {"chat_id": chat_id, "text": response_text}
            if request.method == "POST":
                 incoming_msg = request.json["message"]["text"]
                 print(incoming_msg)
                 chat_id = request.json["message"]["chat"]["id"]
#                 data = {"chat_id": chat_id, "text": response_text}
                 response_text = self.conv.say(incoming_msg)[0]
                 data = {"chat_id": chat_id, "text": response_text}
                 print(response_text)
                 requests.post(url, data=data)
            return {"ok": True}

    def run(self, host="localhost", port=7150):
        self.app.run(host=host, port=port)


if __name__ == '__main__':
    app = Flask(__name__)
    app.config["JSON_AS_ASCII"] = False
    configure_logs()
    nlp = NaturalLanguageProcessor('.')
    nlp.load()
    server =   TLG(name='tlg', app_path='.', nlp=nlp)
    port_number = 5000 
    print('Running server on port {}...'.format(port_number))
    server.run(host='localhost', port=port_number)
