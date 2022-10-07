"""
Contains the main entrypoint for the frontend side of PollCord.
"""

import os
from dotenv import load_dotenv
import discord
import poll_commands.MakerCommands
import poll_commands.RecallCommands


def main():
    """
    Main entrypoint for the frontend. Relies on the TOKEN field from .env file.
    Initializes the Discord bot and adds the necessary cogs to it.
    """
    load_dotenv()
    DISCORD_TOKEN = os.getenv("TOKEN")

    intents = discord.Intents.default()
    intents.message_content = True

    bot = discord.Bot(debug_guilds=[1021553449210499133])

    @bot.event
    async def on_ready():
        """
        Callback function used by Pycord for when the bot is ready to use in Discord.
        """
        print(f"We have logged in as {bot.user}")

    @bot.event
    async def on_message(message):
        """
        Callback function used by Pycord for when the bot recieves a message in Discord.
        Logs the message if it wasn't from the bot itself.
        """
        if message.author == bot.user:
            return
        print(message.content)

    bot.add_cog(poll_commands.MakerCommands.MakerCommands(bot))
    bot.add_cog(poll_commands.RecallCommands.RecallCommands(bot))
    bot.run(DISCORD_TOKEN)


if __name__ == "__main__":
    main()
