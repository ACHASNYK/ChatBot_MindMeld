# -*- coding: utf-8 -*-
"""This module contains the Kwik-E-Mart MindMeld demo application"""
from mindmeld import Application
#from . import custom_features  # noqa: F401

app = Application(__name__)
#app.config['JSON_AS_ASCII'] = False
__all__ = ['app']



@app.handle(intent='greet_ua')
def welcome(request, responder):
    responder.reply(['Привіт!','Здоровеньки були!','Ну здорово!','Мої щирі вітання!','Дуже радий вас бачити!'])
    responder.listen()


@app.handle(intent='exit_ua')
def say_goodbye(request, responder):
    responder.reply(['Бувай!','На все добре!','Ну і пока','До нових зустрічей!','Всього найкращого!'])
    responder.listen()

@app.handle(intent='greet_en')
def welcome_en(request, responder):
    responder.reply(['HI!','How are you!','Glad to see you!','Hello!','Good day!'])
    responder.listen()

@app.handle(intent='exit_en')
def say_goodbye_en(request, responder):
    responder.reply(['Bye!','Have a nice day!','Good bye!','Farewell','It was a pleasure!'])
    responder.listen()

@app.handle(default=True)
def default(request, responder):
    
    responder.reply('Аб чьом це ви? Вибачте я розумію поки що тільки українські і англійські привітання і прощання. Спробуйте ще раз пліз.')
    responder.listen()


