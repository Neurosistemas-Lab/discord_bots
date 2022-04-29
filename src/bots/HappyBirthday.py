import os

#from discord import client
import numpy as np
from discord.ext import commands

dispatcher = [
    "add": add_birth
]

class HappyBirthday:
    def __init__(self) -> None:
        self.birthdays = np.genfromtext("", delimiter=",")

    def add_birth(self, ctx, *args):
        self.birthdays.append([args["name"], args["date"]])

    def list_birth(self, ctx, *args):
        pass

    def remove_birth(self, ctx, *args):
        pass

    def get_birth(self, ctx, *args):
        pass

    def check_birth(self, ctx, *args):
        pass
    

    def _dispatcher(hb: str, *args):
        dispatcher[hb](*args)