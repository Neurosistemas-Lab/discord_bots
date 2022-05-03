import discord
import random

class Greetings(discord.ext.commands.Cog, name='Greetings module'):
    def __init__(self, bot):
        self.bot = bot

    @discord.ext.commands.command(name="alancito")
    async def on_alancito(self, ctx):
        possible_response = [
                f"A sus servicios Sr(a) {ctx.author.name}.",
                "yes, commander?"
                ]
        response = random.choice(possible_response) 
        await ctx.send(response)


    @discord.ext.commands.Cog.listener()
    async def on_member_join(self, member):
        """
        say hi to new memebers
        """
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'A wild {member.mention} has appeared! Welcome to Neurosistemas lab server :D')
