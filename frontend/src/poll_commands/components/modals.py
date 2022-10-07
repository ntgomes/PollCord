"""
This module contains all the modals (pop-ups) used for managing questions on a poll.
"""

import discord
import poll_commands.components.questions as questions


class MCPollModal(discord.ui.Modal):
    """
    Class for representing the modal used for creating a new question to a poll,
    with a set of comma-separated options.
    """

    def __init__(self, *children: discord.ui.InputText, title: str):
        """
        Constructor. Creates the modal and adds the input text elements for creating the question.

        Args:
          title: The title of the modal
        kwargs:
          children: Expected items for use in this modal
        Returns:
          None
        """
        super().__init__(*children, title=title)

        self.add_item(discord.ui.InputText(label="Question"))
        self.add_item(
            discord.ui.InputText(
                label="Options(comma separated)", style=discord.InputTextStyle.long
            )
        )
        self.val = None

    async def callback(self, interaction: discord.Interaction):
        """
        Callback function whenever the user submits their input for the modal
        for creating the poll question. Does some validation of the option field
        before embedding the question into the poll.

        Args:
          interaction: The submission interaction from the user
        """
        if len(self.children[1].value.split(",")) > 25:
            await interaction.response.edit_message(
                embeds=[discord.Embed(title="You can't have more than 25 options")]
            )
        else:
            self.val = questions.MCQuestion(
                self.children[0].value, self.children[1].value
            )
            embed = discord.Embed(title="Question Added to Poll")
            embed.add_field(name="Question", value=self.children[0].value)
            embed.add_field(name="Options", value=self.children[1].value)

            await interaction.response.edit_message(embeds=[embed])


class RemoveModal(discord.ui.Modal):
    """
    Class for representing the modal used for deleting a question from the poll.
    """

    def __init__(self, *children: discord.ui.InputText, title: str, question_list):
        """
        Constructor. Used for the instantiating the modal and adding a input text field
        to it for the question to delete.

        Args:
          title: The title of the modal
          question_list: The list of questions to validate/delete from
        kwargs:
          children: The items that will be included in this modal
        Returns:
          None
        """
        super().__init__(*children, title=title)

        self.add_item(discord.ui.InputText(label="Question"))
        self.question_list = question_list
        self.val = None

    async def callback(self, interaction: discord.Interaction):
        """
        Callback for when the user submits their input for the modal. Removes the question from
        the poll if it was there and states it was successful in doing so, but reports back
        stating otherwise.

        Args:
          interaction: The submission interaction from the user
        """
        self.val = self.children[0].value
        remove_question = None
        for i in self.question_list:
            if i.question == self.val:
                remove_question = i
                break
        try:
            self.question_list.remove(remove_question)
            embed = discord.Embed(title="Deleted Question")
            embed.add_field(name="Question:", value=self.children[0].value)
            await interaction.response.edit_message(embeds=[embed])
        except ValueError:
            error_embed = discord.Embed(title="Error")
            error_embed.add_field(
                name="No such question:", value=self.children[0].value
            )
            await interaction.response.edit_message(embeds=[error_embed])
