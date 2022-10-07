import discord
from discord.ext import commands
from poll_commands.components.views import MakerButtons
from api.api import BackendClient


class MakerCommands(commands.Cog):
    ctx_parse = discord.ApplicationContext

    def __init__(self, bot: discord.Bot):
        self.bot = bot
        self.question_dict = {}

    @commands.slash_command(name="makepoll", guild_id=[1021553449210499133], description="makes a poll")
    async def make_poll(self, ctx: ctx_parse, poll_name: str):
        if (ctx.guild_id, poll_name) in self.question_dict.keys() or BackendClient().check_if_poll_exists(guild_id=ctx.guild_id, poll_name=poll_name):
            await ctx.send(content=f"{poll_name} already exists.")
        else:
            await ctx.send(view=MakerButtons(poll_name=poll_name,
                                             guild_id=ctx.guild_id,
                                             maker=ctx.user,
                                             question_dict=self.question_dict),
                           content="Make that poll!")
