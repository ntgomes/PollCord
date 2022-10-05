import discord
import poll_commands.components.questions as questions


class MCPollModal(discord.ui.Modal):
    def __init__(self, *children: discord.ui.InputText, title: str):
        super().__init__(*children, title=title)

        self.add_item(discord.ui.InputText(label="Question"))
        self.add_item(discord.ui.InputText(label="Options(comma separated)", style=discord.InputTextStyle.long))
        self.val = None

    async def callback(self, interaction: discord.Interaction):
        if len(self.children[1].value.split(",")) > 25:
            await interaction.response.edit_message(embeds=[discord.Embed(title="You can't have more than 25 options")])
        else:
            self.val = questions.MCQuestion(self.children[0].value, self.children[1].value)
            embed = discord.Embed(title="Question Added to Poll")
            embed.add_field(name="Question", value=self.children[0].value)
            embed.add_field(name="Options", value=self.children[1].value)

            await interaction.response.edit_message(embeds=[embed])


class RemoveModal(discord.ui.Modal):
    def __init__(self, *children: discord.ui.InputText, title: str, question_list):
        super().__init__(*children, title=title)

        self.add_item(discord.ui.InputText(label="Question"))
        self.question_list = question_list
        self.val = None

    async def callback(self, interaction: discord.Interaction):
        self.val = self.children[0].value
        remove_question = None
        for i in self.question_list:
            if i.question == self.val:
                remove_question = i
                break
        try:
            self.question_list.remove(remove_question)
            embed = discord.Embed(title="Deleted Quesiton")
            embed.add_field(name="Question:", value=self.children[0].value)
            await interaction.response.edit_message(embeds=[embed])
        except ValueError:
            error_embed = discord.Embed(title="Error")
            error_embed.add_field(name="No such question:", value=self.children[0].value)
            await interaction.response.edit_message(embeds=[error_embed])
