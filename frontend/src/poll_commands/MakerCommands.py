import discord
from discord.ext import commands
from poll_commands.components.views import MakerButtons


class MakerCommands(commands.Cog):
    ctx_parse = discord.ApplicationContext

    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @commands.slash_command(name="makepoll", guild_id=[1021553449210499133], description="makes a poll")
    async def make_poll(self, ctx: ctx_parse, poll_name: str):
        await ctx.send(view=MakerButtons(poll_name=poll_name, guild_id=ctx.guild_id, maker=ctx.user),
                       content="Make that poll!")
