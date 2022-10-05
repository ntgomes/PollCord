import discord


class MCQuestion(object):
    def __init__(self, question, options):
        self.question = question
        self.options = options

    def as_embed(self, number):
        embed = discord.Embed(title=f"Question {number} (Multiple Choice)")
        embed.add_field(name="Question", value=self.question)
        embed.add_field(name="Options", value=self.options)
        return embed

    def as_embed_with_votes(self, number):
        embed = discord.Embed(title=f"Question {number} (Multiple Choice)")
        embed.add_field(name="Question", value=self.question)
        embed.add_field(name="Options", value=self.options)
        embed.add_field(name="Votes", value=self.options)
        return embed
