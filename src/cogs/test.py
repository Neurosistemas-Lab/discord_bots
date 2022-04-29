import discord

class Test(discord.ext.commands.Cog, name='Test module'):
    def __init__(self, bot):
        self.bot = bot

    @discord.ext.commands.command(name="test")
    async def test(self, ctx, *args):
        """
        simple test function for bot testing
        """
        await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))
        

    @discord.ext.commands.command(name="ping")
    async def ping(self, ctx, *args):
        """
        ping request
        """
        await ctx.send(f"pong! still working ;)")
