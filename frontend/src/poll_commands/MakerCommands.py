import discord
from discord.ext import commands
from poll_commands.components.modals import MCPollModal
from poll_commands.components.views import PollButtons


class MakerCommands(commands.Cog):
    ctx_parse = discord.ApplicationContext

    def __init__(self, bot: discord.Bot):
        self.bot = bot
        self.question_dict = {}

    @commands.slash_command(name="makepoll", guild_id=[1021553449210499133], description="makes a poll")
    async def make_poll(self, ctx: ctx_parse, poll_name: str):
        print(type(ctx.guild_id), type(ctx.channel_id))
        print(poll_name)
        await ctx.send(f'Buttons for poll {poll_name}: ',
                       view=PollButtons(poll_name=poll_name, question_dict=self.question_dict, guild_id=ctx.guild_id))
