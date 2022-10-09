import asyncio

import src
import pytest

@pytest.mark.asyncio
async def test_bot():
    bot, DISCORD_TOKEN = src.bot.main()


