"""
alancito.py
    Alancito's script
"""
import os
import random

#from discord import client

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('ALANCITO_TOKEN')
GUILD = os.getenv('NEUROSISTEMAS_GUILD')

#client = discord.Client()
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_member_join(member):
    """
    say hito new memebers
    """
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Neurosistemas lab server!'
    )


@bot.command()
async def test(ctx, *args):
    """
    simple test
    """
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))


@bot.command(name='Alancito')
async def on_alancito(ctx):
    """
    response if alancito is called
    """
    possible_response = [
            f"A sus servicios Sr(a) {ctx.author.name}.",
            "yes, commander?"
            ]
    response = random.choice(possible_response) 
    await ctx.send(response)


bot.run(TOKEN)
