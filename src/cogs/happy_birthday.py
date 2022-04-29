import discord
import numpy as np
import datetime

from discord.ext import tasks
from pathlib import Path

# path to birthdays file
cur_dir = Path.cwd()
file_path = Path(cur_dir, "data", "birthdays.txt")
BIRTHDAYS_FILE = file_path

class HappyBirthday(discord.ext.commands.Cog, name='HappyBirthday module'):
    def __init__(self, bot):
        self.bot = bot
        self.birthdays = np.genfromtxt(BIRTHDAYS_FILE, delimiter=",")
        # maybe using a JSON its easier?
        print(self.birthdays)

    @discord.ext.commands.command(name="add_birth")
    async def add_birth(self, ctx, *args):

        await ctx.send("Please enter your birthday in _day.month_ format")

        # TODO: check same member answer to the bot
        def check(msg):
            return True

        def find_date(msg):
            """
            find date information inside message object
            """
            pass

        message = await self.bot.wait_for('message', check=check)
        # TODO: find date inside message
        date = find_date(message)
        self.birthdays.append([ctx.author.name, date])


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
