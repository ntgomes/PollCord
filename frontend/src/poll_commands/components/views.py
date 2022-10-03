import discord
from poll_commands.components.modals import MCPollModal, RemoveModal


class PollButtons(discord.ui.View):
    def __init__(self, poll_name, guild_id, question_dict, *items):
        super().__init__(*items)
        self.poll_name = poll_name
        self.question_dict = question_dict
        self.question_dict[(guild_id, poll_name)] = []

    @discord.ui.button(label="Add MC Question", row=0, style=discord.ButtonStyle.primary)
    async def mc_button_callback(self, button: discord.Button, interaction: discord.Interaction):
        new_modal = MCPollModal(title="Multiple Choice Form")
        await interaction.response.send_modal(new_modal)
        await new_modal.wait()
        self.question_dict[(interaction.guild_id, self.poll_name)].append(new_modal.val)

    @discord.ui.button(label="Remove Question", row=0, style=discord.ButtonStyle.danger)
    async def remove_button_callback(self, button:discord.Button, interaction: discord.Interaction):
        remove_modal = RemoveModal(title="Remove Question Form", question_list=self.question_dict[(interaction.guild_id,
                                                                                                   self.poll_name)])
        await interaction.response.send_modal(remove_modal)

    @discord.ui.button(label="List Questions", row=0, style=discord.ButtonStyle.primary)
    async def list_button_callback(self, button: discord.Button, interaction: discord.Interaction):
        questions = self.question_dict[(interaction.guild_id,  self.poll_name)]
        embeds = []
        for i, v in enumerate(questions, 1):
            embeds.append(v.as_embed(i))
        await interaction.response.edit_message(embeds=embeds)

    @discord.ui.button(label="Finalize ")