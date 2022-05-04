import discord
import json
import os
import numpy as np
import pandas as pd
import datetime as dt
from datetime import datetime, timedelta
from dotenv import load_dotenv
import asyncio

from discord.ext import tasks

load_dotenv()
BIRTHDAY_CHANNEL = os.getenv("BIRTHDAY_CHANNEL")
# path to birthdays file
BIRTHDAYS_FILE = os.path.join(os.getcwd(), "data", "birthdays.csv")

def seconds_until(hours, minutes):
    """
    Seconds until desired hours and minutes
    """
    now = datetime.now()
    target = now.replace(hour=hours, minute=minutes, second=0, microsecond=0)
    if target < now:
        target += timedelta(days=1)
    return (target - now).total_seconds()
class HappyBirthday(discord.ext.commands.Cog, name='HappyBirthday module'):
    def __init__(self, bot):
        self.bot = bot
        self.birthdays = pd.read_csv(BIRTHDAYS_FILE, 
                                    delimiter=';', 
                                    names=["id", "birth", "name"], 
                                    header=None, 
                                    index_col="id"
        )
        self.birthdays["birth"] = pd.to_datetime(self.birthdays["birth"], dayfirst=True)
        print(self.birthdays)
        self.check_birth.start()

    @discord.ext.commands.command(name="add_birth")
    async def add_birth(self, ctx, message, *args):
        try:
            date = pd.to_datetime(message, dayfirst=True)
            self.birthdays.loc[ctx.message.author.id] = [date, ctx.message.author.display_name]
            await ctx.send("Birthday added!")
            print(self.birthdays)
        except:
            await ctx.send("Something went wrong with your birthday format. Please enter your birthday in dd/mm/yy format")

    @discord.ext.commands.command(name="list_birth")
    async def list_birth(self, ctx, *args):
        """
        list all birthdays
        """
        await ctx.send(self.birthdays)

    @discord.ext.commands.command(name="remove_birth")
    async def remove_birth(self, ctx, message, *args):
        """
        remove birthday from name
        """
        if not self.birthdays[self.birthdays["name"] == message].empty:
            self.birthdays = self.birthdays[self.birthdays["name"] != message]
            await ctx.send("Birthday removed!")
            print(self.birthdays)
        else:
            await ctx.send("Something went wrong with the name. Please enter the name of the person you want to remove and try again.")

    @discord.ext.commands.command(name="get_birth_from_name")
    async def get_birth_from_name(self, ctx, message, *args):
        """
        get birthday from name
        """
        await ctx.send(self.birthdays[self.birthdays["name"] == message])

    @discord.ext.commands.command(name="get_birth_from_date")
    async def get_birth_from_date(self, ctx, message, *args):
        """
        get birthday from date
        """
        await ctx.send(self.birthdays[self.birthdays["birth"] == pd.to_datetime(message, dayfirst=True)])

    @discord.ext.commands.command(name="get_channel")
    async def get_channel(self, ctx, *args):
        """
        get channel
        """
        await ctx.send(ctx.channel)

    @tasks.loop(hours=24)
    async def check_birth(self, *args):
        """
        check if there is a birthday today
        """
        channel = await self.bot.fetch_channel(BIRTHDAY_CHANNEL)
        today = datetime.now()
        today = today.replace(hour=0, minute=0, second=0, microsecond=0)
        today = today.strftime("%d/%m/%Y")
        if not self.birthdays[self.birthdays["birth"] == pd.to_datetime(today, dayfirst=True)].empty:
            await channel.send(self.birthdays[self.birthdays["birth"] == pd.to_datetime(today, dayfirst=True)])
            await channel.send("Happy birthday! :partying_face:")
        else:
            await channel.send("No birthday today")

    @check_birth.before_loop
    async def before_check_birth(self):
        print('Waiting Alancito to connect...')
        await self.bot.wait_until_ready()
        print("Waiting cycle")
        await asyncio.sleep(seconds_until(0, 0))

    @discord.ext.commands.command(name="check_birth")
    async def check_birth(self, *args):
        """
        check if there is a birthday today
        """
        channel = await self.bot.fetch_channel(BIRTHDAY_CHANNEL)
        today = datetime.now()
        today = today.replace(hour=0, minute=0, second=0, microsecond=0)
        today = today.strftime("%d/%m/%Y")
        if not self.birthdays[self.birthdays["birth"] == pd.to_datetime(today, dayfirst=True)].empty:
            await channel.send(self.birthdays[self.birthdays["birth"] == pd.to_datetime(today, dayfirst=True)])
            await channel.send("Happy birthday! :partying_face:")
        else:
            await channel.send("No birthday today")
