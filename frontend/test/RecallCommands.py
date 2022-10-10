import src
import pytest
import discord


def test_make_poll():
    bot, _ = src.bot.main()
    commands = src.poll_commands.RecallCommands.RecallCommands(bot)
    commands.recall_poll(None, "thing")
    