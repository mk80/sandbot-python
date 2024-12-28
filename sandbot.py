#!/usr/bin/python3

import os
import sys
import discord
import re
from rule_based_chat import sendToRule
from retrieval_based_chat import sendToRetrieval
from generative_based_chat import sendToGenerative

# get present working dir
pwd = os.getcwd()

# arg for bot type

bot_type_check = ("rule", "retrieval", "generative")
if len(sys.argv) == 1:
  print("please provide bot type:\nrule\nretrieval\n")
  sys.exit(1)
else:
  bot_type = sys.argv[1]

if bot_type not in bot_type_check:
  print("please provide bot type:\nrule\nretrieval\n")
  sys.exit(1)

# define file that has the token and store in token var
token_file = 'token.txt'
token = ''

with open(token_file,'r') as data:
  token = data.read().replace('\n','')

# define log file to use
log_file = pwd + '/' + 'chat.log'

# start discord client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# regex definitions
#greetings = (r'h.*\ssandbot.*')
bot_name = (r'.*sandbot.*')

@client.event  # event decorator/wrapper. More on decorators here: https://pythonprogramming.net/decorators-intermediate-python-tutorial/
async def on_ready():  # method expected by client. This runs once when connected
  with open(log_file,'a') as log:
    log.write(f'We have logged in as {client.user}\n')  # notification of login

@client.event
async def on_message(message):  # event that happens per any message.
  with open(log_file,'a') as log:
    log.write(f"{message.channel}: {message.author}: {message.author.name}: {message.content}\n")

  # regex match for sandbot name
  found_match = re.match(bot_name,message.content.lower())
  if found_match and str(message.author) != "sandbot#0621":

        # regex match for a greeting before sandbot name
        #found_match = re.match(greetings,message.content.lower())
        #if found_match:
        # simply reply with greeting response
        #  reply = ('Hi ' + str(message.author.name) + "!")
        #  await message.channel.send(reply)
        # entry into chatbot
        # else:
    if (bot_type == 'rule'):
      reply = sendToRule(str(message.author.name),message.content.lower())
      await message.channel.send(reply)
    elif (bot_type == 'retrieval'):
      reply = sendToRetrieval(str(message.author.name),message.content.lower())
      await message.channel.send(reply)
    elif (bot_type == 'generative'):
      reply = sendToGenerative(str(message.author.name),message.content.lower())
      await message.channel.send(reply)

client.run(token)
