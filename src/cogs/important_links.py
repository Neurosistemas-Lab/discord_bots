"""
important_links.py
    A class for handling important links for the lab
"""
import discord
import yaml

from pathlib import Path

# path to important_links file
cur_dir = Path.cwd()
file_path = Path(cur_dir, "data", "important_links.yaml")
LINKS_PATH = file_path


def read_links(path=LINKS_PATH):
    """
    read links from yaml file
    """
    with open(path) as f:
        links = yaml.safe_load(f)
    return links


def add_link(yaml_obj, path=LINKS_PATH):
    """
    set a new link with yaml_obj info (dict)
    """
    with open(path, 'a') as f:
        yaml.safe_dump(yaml_obj, f)


def rm_link(name_link, current_links, path=LINKS_PATH):
    """
    remove a link
    """
    flag = 0  # Everything works well
    if name_link in current_links.keys():
        with open(path, 'w+') as f:
            current_links.pop(name_link)
            yaml.safe_dump(current_links, f)
    else:
        flag = 1
    return flag


class ImportantLinks(discord.ext.commands.Cog, name='ImportantLinks module'):
    def __init__(self, bot):
        self.bot = bot
        self.links = read_links(LINKS_PATH)

    @discord.ext.commands.command(name="link")
    async def link(self, ctx, *args):
        """
        get important links
        """
        mode = args[0]  # list or set
        if mode == "list":
            # list all links
            all_links = []
            for link_name in self.links.keys():
                all_links.append(link_name)
            response = f"{ctx.author.name} estos son los links disponibles: " \
                f"{all_links}"
        elif mode == "add":
            name_link = args[1]
            link = args[2]
            link_dict = {name_link: link}
            add_link(yaml_obj=link_dict)
            # update self.links
            self.links = read_links()
            response = f"{ctx.author.name}, link *{name_link}* " \
                "ha sido incluido a la lista"
        elif mode == "remove":
            name_link = args[1]
            fail = rm_link(name_link=name_link, current_links=self.links)
            if fail:
                response = f"{ctx.author.name}, link *{name_link}* " \
                    "no ha podido ser removido a la lista. " \
                    "Para remover un link escribe: " \
                    "**!list remove nombre_link**"
            else:
                self.links = read_links()
                response = f"{ctx.author.name}, link *{name_link}* " \
                    "ha sido removido a la lista"
        else:
            link_name = args[0]
            try:
                link = self.links[link_name]
                response = f"{ctx.author.name}, el link asociado" \
                    f"a *{link_name}* es: {link}"
            except Exception:
                response = f"{ctx.author.name}, no hay link asociado a " \
                    f"*{link_name}*. Escribe **!link list** para obtener " \
                    "una lista de links importantes"
        await ctx.send(response)
