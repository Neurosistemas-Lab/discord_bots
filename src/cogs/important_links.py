"""
important_links.py
    A class for handling important links for the lab
"""
import discord

class ImportantLinks(discord.ext.commands.Cog, name='ImportantLinks module'):
    def __init__(self, bot):
        self.bot = bot

    @discord.ext.commands.command(name="formulario_covid")
    async def formulario_covid(self, ctx):
        link = "http://formulariocovid.med.uchile.cl/index2.html " 
        response = f"{ctx.author.name} el link al formulario es: {link}" 
        await ctx.send(response)


    @discord.ext.commands.command(name="zoom_labmeeting")
    async def zoom_labmeeting(self, ctx):
        link = "https://uchile.zoom.us/j/85075112448?pwd=cnE3NGZjSUt6amZwT21rWUR6R050QT09" 
        response = f"{ctx.author.name} el link al zoom de la reunión del lab es: {link}" 
        await ctx.send(response)


    @discord.ext.commands.command(name="zoom_jc")
    async def zoom_jc(self, ctx):
        link = "https://uchile.zoom.us/j/86803112745?pwd=c090alNNRHc2QXZ0U3AwQ2ExNk5QUT09" 
        response = f"{ctx.author.name} el link al zoom del JC es: {link}" 
        await ctx.send(response)


    @discord.ext.commands.command(name="drive_jc")
    async def drive_jc(self, ctx):
        link = "https://drive.google.com/drive/folders/1XS1BL0wy0hdP9AG6TWtu-z1hybKsG-zG" 
        response = f"{ctx.author.name} el link al drive del JC es: {link}" 
        await ctx.send(response)
