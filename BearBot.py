import os

import discord

# bots discord token
TOKEN = 'NjkyOTk1OTkzNDMxNDQxNDA4.Xn21-g.tJi1CiT6zwXS0ak8yiJ-XKLEPl8'

client = discord.Client()

# inital event, notifies user once bot is online and ready further events
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    author = message.author
    if message.content == 'Whats up mothafucka':
        await message.channel.send('Ah SHIT, hows it hangin {}!'.format(author))

client.run(TOKEN)
