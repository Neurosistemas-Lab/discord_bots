"""
run.py
    main code for running bots
"""
import discord
import os

from dotenv import load_dotenv

from bots.alancito import Alancito

from cogs.command_err_handler import CommandErrHandler
from cogs.greetings import Greetings
from cogs.happy_birthday import HappyBirthday
from cogs.test import Test

COMMAND_PREFIX = "!"

def main():
    load_dotenv()
    TOKEN = os.getenv('ALANCITO_TOKEN')
    GUILD = os.getenv('NEUROSISTEMAS_GUILD')

    intents = discord.Intents.default()
    intents.members = True

    bot = Alancito(
            command_prefix=COMMAND_PREFIX,
            intents=intents
            )

    bot.add_cog(CommandErrHandler(bot))
    bot.add_cog(Greetings(bot))
    bot.add_cog(HappyBirthday(bot))
    bot.add_cog(Test(bot))

    bot.run(TOKEN)

if __name__ == '__main__':
    main()
