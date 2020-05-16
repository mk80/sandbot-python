#!/usr/bin/python3

import os
import discord
import re
from rule_based_chat import sendNameandMessage

# get present working dir
pwd = os.getcwd()

# define file that has the token and store in token var
token_file = 'token.txt'
token = ''

with open(token_file,'r') as data:
  token = data.read().replace('\n','')

# define log file to use
log_file = pwd + '/' + 'chat.log'

# start discord client
client = discord.Client()

# regex definitions
greetings = (r'h.*\ssandbot.*')
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
    reply = sendNameandMessage(str(message.author.name),message.content.lower())
    await message.channel.send(reply)

client.run(token)
