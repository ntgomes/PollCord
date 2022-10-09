import src
import pytest
import discord


def test_make_poll():
    bot, _ = src.bot.main()
    commands = src.poll_commands.MakerCommands.MakerCommands(bot)
    commands.make_poll(None, "thing")
