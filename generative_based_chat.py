#!/usr/bin/python3

# based off codecademy lessons

import os
import requests
import json

class SandBot:
  def __init__(self):
    self.chat_payload = {
      "model": "llama2-uncensored",
      "prompt": "why are we here?",
      "stream": False,
      "keep_alive": "24h"
    }

  def chat(self, name, message):
    self.chat_payload["prompt"] = message
    chat_payload_json = json.dumps(self.chat_payload)

    try:
      llm_response = requests.post("http://localhost:11434/api/generate", data=chat_payload_json)
      llm_response.raise_for_status()
      
      llm_response_json = llm_response.json()

      chat_response = llm_response_json["response"]
      return(chat_response)
    except requests.exceptions.RequestException as err:
      chat_response = "my little local llm is having issues... " + str(err)
      return(chat_response)

# example chat payload and url
#curl http://localhost:11435/api/generate -d '{
#    "model": "llama2-uncensored",
#    "prompt": "why is the sky blue?",
#    "format": "json",
#    "stream": false
#}'

#initialize ChatBot instance below:

#call .chat() method below for testing:
#sandbot = SandBot()
#sandbot.chat("fake_user", "if the universe is so big are we alone ")

# interaction with discord program sandbot.py
def sendToGenerative(name, message):
  sandy = SandBot()
  message = message.lower()
  message = message.replace("sandbot", "chatbot").replace("Sandbot", "Chatbot")
  reply = sandy.chat(name, message)
  if len(reply) > 2000:
    reply = "sorry but i got a little long winded with that response and discord rejected it for being over 2000 chars... to have better luck please rephrase your question.. thanks.."
  return reply
