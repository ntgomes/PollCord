import src
import discord

def test_inits():
    try:
        src.poll_commands.components.views.MakerButtons(
            guild_id=12343245234, poll_name="thing", maker=None, question_dict={}
        )
    except RuntimeError:
        try:
            src.poll_commands.components.views.PollButtons(
                guild_id=12343245234, poll_name="thing", question_dict={}
            )
        except RuntimeError:
            return 0
