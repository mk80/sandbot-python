#!/usr/bin/python3

import discord
import re
from chatty import sendNameandMessage

token_file = 'token.txt'
token = ''

with open(token_file,'r') as data:
    token = data.read().replace('\n','')

client = discord.Client()  # starts the discord client.

#greetings = ("hello", "Hello", "hello!", "Hello!", "hi", "Hi", "hi!", "Hi!", "hola", "Hola", "hola!", "Hola!")
greetings = (r'h.*\ssandbot.*')
bot_name = (r'.*sandbot.*')

@client.event  # event decorator/wrapper. More on decorators here: https://pythonprogramming.net/decorators-intermediate-python-tutorial/
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {client.user}')  # notification of login.

@client.event
async def on_message(message):  # event that happens per any message.
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    found_match = re.match(bot_name,message.content.lower())
    if found_match and str(message.author) != "sandbot#0621":
        found_match = re.match(greetings,message.content.lower())
        if found_match:
          reply = ('Hi! ' + str(message.author))
          await message.channel.send(reply)
        else:
          reply = sendNameandMessage(str(message.author),message.content.lower())
          await message.channel.send(reply)

client.run(token)
