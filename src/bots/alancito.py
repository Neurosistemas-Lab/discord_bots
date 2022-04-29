"""
alancito.py
    Alancito's script
"""
from discord.ext import commands

class Alancito(commands.Bot):
    
    async def on_ready(self):
        print(f'{self.user.name} has connected to Discord!')

