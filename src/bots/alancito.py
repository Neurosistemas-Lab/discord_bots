"""
alancito.py
    Alancito's script
"""
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('ALANCITO_TOKEN')
GUILD = os.getenv('NEUROSISTEMAS_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    """
    say hito new memebers
    """
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Neurosistemas lab server!'
    )

client.run(TOKEN)
