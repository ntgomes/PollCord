import discord
import poll_commands.components.questions as questions


class OpenPollModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Question", style=discord.InputTextStyle.long))
        self.val = None

    async def callback(self, interaction: discord.Interaction):
        self.val = questions.OpenQuestion(self.children[0].value)
        embed = discord.Embed(title="Question Added to Poll")
        embed.add_field(name="Question", value=self.children[0].value)

        await interaction.response.edit_message(embeds=[embed])


class MCPollModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Question"))
        self.add_item(discord.ui.InputText(label="Options(comma separated)", style=discord.InputTextStyle.long))
        self.val = None

    async def callback(self, interaction: discord.Interaction):
        self.val = questions.MCQuestion(self.children[0].value, self.children[1].value)
        embed = discord.Embed(title="Question Added to Poll")
        embed.add_field(name="Question", value=self.children[0].value)
        embed.add_field(name="Options", value=self.children[1].value)

        await interaction.response.edit_message(embeds=[embed])
