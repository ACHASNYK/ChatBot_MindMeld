# ChatBot_MindMeld
Hi to everyone!

It was a test task to build a conversational chatbot for Telegram messenger based on the MindMeld ConversationalAI work frame by Cisco.

In particular, a chatbot is capable to recognize greets and exit words or phrases in 2 languages: English and Ukrainian. And after recognition answer greets and exits words in a related language. Chatbot to be linked with Telegram messenger.

A basic dialog flow is to be designed, however, a work frame is capable to make a dialog much deeper and rich in accordance with the customer's request.

Only 2 functions from build-in NLP pipeline was engaged: Domain Recognition and Intent Recognition. A train and test text files was created and a model was trained used logreg classificator and a bag-of-words.

In order to accomplish this task, an instance was raised on AWS EC2 on UBUNTU 18 machine with 4Gb and 2 CPUs as a MindMeld and its dependencies (Elascticsearch) requirements.

The project was built on Python3.6, Flask, and MindMeld. Elasticsearch, Telegram API, and other libraries.

A simple but capable interface with Telegram was built with HTTP requests to telegram`s web API interface engaged Webhook, JSON created by Responses library.

This project can be run on-line on-demand to test it - please send me a request via Telegram or WhatsUp, since an instance on EC2 engaged is not on the free-tier of billing )).

P.S. (Should you decide to install this project on remote instance - make sure you meet the hardware requirements of Elasticsearch)
