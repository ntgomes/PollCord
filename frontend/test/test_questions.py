import src
import discord


def test_question():
    sample = src.poll_commands.components.questions.MCQuestion("Sample Question", ["Option 1", "Option 2", "Option 3"])
    embed = discord.Embed(title=f"Question {1} (Multiple Choice)")
    embed.add_field(name="Question", value=sample.question)
    embed.add_field(name="Options", value=sample.options)
    assert embed.to_dict() == sample.as_embed(1).to_dict()
