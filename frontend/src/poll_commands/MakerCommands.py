"""
Contains the cog implementation for creating a new poll.
"""

import discord
from discord.ext import commands
from poll_commands.components.views import MakerButtons
from api.api import BackendClient


class MakerCommands(commands.Cog):
    """
    Class that represents the cog for handling the /makepoll command for the bot.

    Args:
      bot: The Discord bot to link the cog to
    """

    ctx_parse = discord.ApplicationContext

    def __init__(self, bot: discord.Bot):
        """
        Constructor.
        """
        self.bot = bot
        self.question_dict = {}

    @commands.slash_command(
        name="makepoll", guild_id=[1021553449210499133], description="makes a poll"
    )
    async def make_poll(self, ctx: ctx_parse, poll_name: str):
        """
        Function to handle the input of the /makepoll command from the user.

        Args:
          ctx: The Discord application context for the bot to send messages with.
          poll_name: The name of the poll you want to create
        """
        if (
            ctx.guild_id,
            poll_name,
        ) in self.question_dict.keys() or BackendClient().check_if_poll_exists(
            guild_id=ctx.guild_id, poll_name=poll_name
        ):
            await ctx.send(content=f"{poll_name} already exists.")
        else:
            await ctx.send(
                view=MakerButtons(
                    poll_name=poll_name,
                    guild_id=ctx.guild_id,
                    maker=ctx.user,
                    question_dict=self.question_dict,
                ),
                content="Make that poll!",
            )
