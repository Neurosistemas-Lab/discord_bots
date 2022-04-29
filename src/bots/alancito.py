"""
alancito.py
    Alancito's script
"""
import os
import random

#from discord import client

from discord.ext import commands
from dotenv import load_dotenv
#from HappyBirthday import HappyBirthday

load_dotenv()
TOKEN = os.getenv('ALANCITO_TOKEN')
GUILD = os.getenv('NEUROSISTEMAS_GUILD')
class Alancito(commands):
    def __init__(self):
        self.bot = commands.Bot(command_prefix='!')
        print(self.bot)
        pass
        #self.happy_birthday = HappyBirthday()

    def run(self):
        bot.run(TOKEN)

    def check_bd(self):
        bot.happy_birthday.check_birth()

    @bot.event
    async def on_ready(self):
        print(f'{bot.user.name} has connected to Discord!')

    @bot.event
    async def on_member_join(self, member):
        """
        say hito new memebers
        """
        await member.create_dm()
        await member.dm_channel.send(
            f'Hi {member.name}, welcome to my Neurosistemas lab server!'
        )

    @bot.command()
    async def test(self, ctx, *args):
        await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))

    @bot.command(name='Alancito')
    async def on_alancito(self, ctx):
        possible_response = [
                f"A sus servicios Sr(a) {ctx.author.server_name}.",
                "yes, commander?"
                ]
        response = random.choice(possible_response) 
        await ctx.send(response)

    @bot.command(name="hb")
    async def hb_commands(self, ctx, *args):
        pass
        


#if __name__ == '__main__':
#    alancito = Alancito()
#    alancito.run()