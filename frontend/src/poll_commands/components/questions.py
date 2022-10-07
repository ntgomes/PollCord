import discord


class MCQuestion(object):
    """
    Class that represents a poll question, with the question text and the options themselves.
    """

    def __init__(self, question, options):
        """
        Constructor.
        """
        self.question = question
        self.options = options

    def as_embed(self, number):
        """
        Describes how the fields of this MCQuestion should be displayed onto a Discord UI
        as an embed.

        Args:
          number: The ordinal number of the poll question
        Returns:
          The Discord embed to display
        """
        embed = discord.Embed(title=f"Question {number} (Multiple Choice)")
        embed.add_field(name="Question", value=self.question)
        embed.add_field(name="Options", value=self.options)
        return embed

    def as_embed_with_votes(self, number):
        """
        Just like as_embed but includes the votes during a recall or finalize.

        Args:
          number: The ordinal number of the poll question
        Returns:
          The Discord embed to display
        """
        embed = discord.Embed(title=f"Question {number} (Multiple Choice)")
        embed.add_field(name="Question", value=self.question)
        embed.add_field(name="Options", value=self.options)
        embed.add_field(name="Votes", value=self.options)
        return embed
