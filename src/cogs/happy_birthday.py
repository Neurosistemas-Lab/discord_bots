import discord
from discord.ext import tasks
import numpy as np

class HappyBirthday(discord.ext.commands.Cog, name='HappyBirthday module'):
    def __init__(self, bot):
        self.bot = bot
        #self.birthdays = np.genfromtxt("", delimiter=",")

    @discord.ext.commands.command(name="add_birth")
    async def add_birth(self, ctx, *args):
        self.birthdays.append([args["name"], args["date"]])


    @discord.ext.commands.command(name="list_birth")
    async def list_birth(self, ctx, *args):
        pass

    @discord.ext.commands.command(name="remove_birth")
    async def remove_birth(self, ctx, *args):
        pass

    @discord.ext.commands.command(name="get_birth")
    async def get_birth(self, ctx, *args):
        pass

    # is there a specific decorator for checking time??
    #https://discordpy.readthedocs.io/en/stable/ext/tasks/index.html
    @tasks.loop(minutes=1440)
    #@discord.ext.commands.command(name="check_birth")
    async def check_birth(self, ctx, *args):
        pass
