"""
Contains the cog implementation for recalling an archived poll.
"""

import discord
from discord.ext import commands
from api.api import BackendClient


class RecallCommands(commands.Cog):
    """
    Class that represents the cog for handling the /recallpoll command for the bot.

    Args:
      bot: The Discord bot to link the cog to
    """

    ctx_parse = discord.ApplicationContext

    def __init__(self, bot):
        """
        Constructor.
        """
        self.bot = bot

    @commands.slash_command(
        name="recallpoll",
        guild_id=[1021553449210499133],
        description="recalls the results of a previous poll",
    )
    async def recall_poll(self, ctx: ctx_parse, poll_name: str):
        """
        Function to handle the input of the /recallpoll command from the user.

        Args:
          ctx: The Discord application context for the bot to send messages with.
          poll_name: The name of the poll you want to recall
        """
        result = BackendClient().recall_poll(ctx.guild_id, poll_name)
        if result is None:
            await ctx.respond(content=f"There is no previous poll called {poll_name}")
        else:
            actual_results = result["results"]
            embeds = [discord.Embed(title=f"{poll_name}")]
            for _, value in actual_results.items():
                new_embed = discord.Embed()
                for key, option in value.items():
                    if key == "question_text":
                        new_embed.title = f"Question: {option}"
                    else:
                        new_embed.add_field(name=key, value=str(option))
                embeds.append(new_embed)
            await ctx.respond(embeds=embeds)
