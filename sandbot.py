#!/usr/bin/python3

import discord

token_file = 'token.txt'
token = ''

with open(token_file,'r') as data:
    token = data.read().replace('\n','')

client = discord.Client()  # starts the discord client.

@client.event  # event decorator/wrapper. More on decorators here: https://pythonprogramming.net/decorators-intermediate-python-tutorial/
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {client.user}')  # notification of login.

@client.event
async def on_message(message):  # event that happens per any message.
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    if str(message.author) != "sandbot#0621" and "hello" in message.content.lower():
        await message.channel.send('Hi!')

client.run(token)
