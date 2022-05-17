import discord
import json
import os
import numpy as np
import pandas as pd
import datetime as dt
from datetime import datetime, timedelta
from dotenv import load_dotenv
import asyncio
import psycopg2

from discord.ext import tasks

load_dotenv()
BIRTHDAY_CHANNEL = os.getenv("BIRTHDAY_CHANNEL")
DATABASE_URL = os.getenv("DATABASE_URL")

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
        self.conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        self.check_loop_birth.start()

    @discord.ext.commands.command(name="add_birth")
    async def add_birth(self, ctx, message, *args):
        try:
            cur = self.conn.cursor()
            date = pd.to_datetime(message, dayfirst=True).to_pydatetime().strftime("%Y-%m-%d")
            cur.execute(
                """INSERT INTO birthdays (birth, member_name) VALUES(%s, %s);""", 
                (date, ctx.message.author.display_name)
            )
            self.conn.commit()
            cur.close()
            await ctx.send("Birthday added!")
        except:
            await ctx.send("Something went wrong with your birthday format. Please enter your birthday in dd/mm/yy format")

    @discord.ext.commands.command(name="add_birth_by_name")
    async def add_birth_by_name(self, ctx, message, *args):
        try:
            cur = self.conn.cursor()
            date = pd.to_datetime(message, dayfirst=True).to_pydatetime().strftime("%Y-%m-%d")
            cur.execute(
                """INSERT INTO birthdays (birth, member_name) VALUES(%s, %s);""", 
                (date, args[0])
            )
            self.conn.commit()
            cur.close()
            await ctx.send("Birthday added!")
        except:
            await ctx.send("Something went wrong with your birthday format. Please enter your birthday in dd/mm/yy format")

    @discord.ext.commands.command(name="list_birth")
    async def list_birth(self, ctx, *args):
        """
        list all birthdays
        """
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM birthdays;")
        await ctx.send(cur.fetchall())
        self.conn.commit()
        cur.close()

    @discord.ext.commands.command(name="remove_birth")
    async def remove_birth(self, ctx, message, *args):
        """
        remove birthday from name
        """
        try:
            cur = self.conn.cursor()
            cur.execute(
                """DELETE FROM birthdays WHERE member_name = %s;""",
                (message,)
            )
            self.conn.commit()
            cur.close()
            await ctx.send("Birthday removed!")
        except:
            await ctx.send("Something went wrong with the name. Please enter the name of the person you want to remove and try again.")

    @discord.ext.commands.command(name="get_birth_from_name")
    async def get_birth_from_name(self, ctx, message, *args):
        """
        get birthday from name
        """
        try:
            cur = self.conn.cursor()
            cur.execute(
                """SELECT birth, member_name FROM birthdays WHERE member_name = %s;""",
                (message,)
            )
            await ctx.send(cur.fetchall())
            self.conn.commit()
            cur.close()
        except:
            await ctx.send("Something went wrong with the name. Please enter the name of the person you want to get birth.")

    @discord.ext.commands.command(name="get_birth_from_date")
    async def get_birth_from_date(self, ctx, message, *args):
        """
        get birthday from date
        """
        try:
            cur = self.conn.cursor()
            cur.execute(
                """SELECT birth, member_name FROM birthdays WHERE birth = %s;""",
                (message,)
            )
            await ctx.send(cur.fetchall())
            self.conn.commit()
            cur.close()
        except:
            await ctx.send("Something went wrong with the date. Please enter the date you want to get birth.")

    @discord.ext.commands.command(name="get_birth_from_month")
    async def get_birth_from_month(self, ctx, message, *args):
        """
        get birthday from month
        """
        try:
            cur = self.conn.cursor()
            cur.execute(
                """SELECT birth, member_name FROM birthdays WHERE EXTRACT(MONTH FROM birth) = %s;""",
                (message,)
            )
            await ctx.send(cur.fetchall())
            self.conn.commit()
            cur.close()
        except:
            await ctx.send("Something went wrong with the month. Please enter the month you want to get birth.")


    @discord.ext.commands.command(name="get_channel")
    async def get_channel(self, ctx, *args):
        """
        get channel
        """
        await ctx.send(ctx.channel)

    @discord.ext.commands.command(name="get_time")
    async def get_time(self, ctx, *args):
        """
        get time
        """
        timestamp = datetime.now()
        await ctx.send(timestamp.strftime(r"%I:%M %p"))

    @discord.ext.commands.command(name="seconds_until")
    async def seconds_until(self, ctx, *args):
        """
        get time until hour and minutes
        """
        await ctx.send(seconds_until(int(args[0]), int(args[1])))

    @tasks.loop(hours=24)
    async def check_loop_birth(self, *args):
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

    @check_loop_birth.before_loop
    async def before_check_loop_birth(self):
        print('Waiting Alancito to connect...')
        await self.bot.wait_until_ready()
        print("Waiting cycle")
        await asyncio.sleep(seconds_until(4, 1))

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
