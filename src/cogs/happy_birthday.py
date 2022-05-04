import discord
import json
import os
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

from discord.ext import tasks

# path to birthdays file
BIRTHDAYS_FILE = os.path.join(os.getcwd(), "data", "birthdays.csv")



class HappyBirthday(discord.ext.commands.Cog, name='HappyBirthday module'):
    def __init__(self, bot):
        self.bot = bot
        self.birthdays = pd.read_csv(BIRTHDAYS_FILE, 
                                    delimiter=';', 
                                    names=["id", "birth", "name"], 
                                    header=None, 
                                    index_col="id"
        )
        print(self.birthdays)

    @discord.ext.commands.command(name="add_birth")
    async def add_birth(self, ctx, msg, *args):
        await ctx.send("Please enter your birthday in dd/mm/yy format")

        def check(msg):
            return msg.author == ctx.author
        print(msg.author, ctx.author)
        message = await self.bot.wait_for('message', check=check)
        print(message)
        try:
            date = pd.to_datetime(message, dayfirst=True)
            self.birthdays.loc[message.author.id] = [date, message.author.name]
            await ctx.send("Birthday added!")
        except:
            await ctx.send("Something went wrong with your birthday format")


    @discord.ext.commands.command(name="list_birth")
    async def list_birth(self, ctx, *args):
        """
        list all birthdays
        """
        await ctx.send(self.birthdays)

    @discord.ext.commands.command(name="remove_birth")
    async def remove_birth(self, ctx, *args):
        """
        remove birthday
        """
        await ctx.send("Please enter your birthday in _day.month_ format")
        message = await self.bot.wait_for('message', check=check)
        # TODO: find date inside message
        date = find_date(message)


    @discord.ext.commands.command(name="get_birth")
    async def get_birth(self, ctx, *args):
        """
        get birthday
        """
        await ctx.send("Please enter your birthday in _day.month_ format")


    # is there a specific decorator for checking time??
    #https://discordpy.readthedocs.io/en/stable/ext/tasks/index.html
    @tasks.loop(minutes=1440)
    #@discord.ext.commands.command(name="check_birth")
    async def check_birth(self, ctx, *args):
        pass
