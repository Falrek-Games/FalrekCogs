import logging
import discord
from redbot.core import Config, commands

log = logging.getLogger("red.falrekcogs.collector")


class Kill(commands.Cog):
    """
    Kill people in interesting ways

    More detailed docs: <https://cogs.yamikaitou.dev/kill.html>
    """

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1190143401371385917, force_registration=True)