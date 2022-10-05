import discord
from poll_commands.components.modals import MCPollModal, RemoveModal


class MakerButtons(discord.ui.View):
    """
    Main view used for authoring new polls
    :parameter poll_name: name of the poll
    :parameter guild_id: the guild id of where of poll is
    :parameter question_dict: a dict key:(guild_id,poll_name) value:[MCQuestions]
    """

    def __init__(self, poll_name: str, guild_id: int, maker: discord.User, *items):
        super().__init__(timeout=None, *items)
        self.poll_name = poll_name
        self.question_dict = {(guild_id, poll_name): []}
        self.maker = maker

    @discord.ui.button(label="Add MC Question", row=0, style=discord.ButtonStyle.primary)
    async def mc_button_callback(self, button: discord.Button, interaction: discord.Interaction):
        if interaction.user != self.maker:
            await interaction.response.send_message(content=f"You aren't that maker of this poll",
                                                    ephemeral=True)
        else:
            new_modal = MCPollModal(title="Multiple Choice Form")
            await interaction.response.send_modal(new_modal)
            await new_modal.wait()
            self.question_dict[(interaction.guild_id, self.poll_name)].append(new_modal.val)

    @discord.ui.button(label="Remove Question", row=0, style=discord.ButtonStyle.danger)
    async def remove_button_callback(self, button: discord.Button, interaction: discord.Interaction):
        if interaction.user != self.maker:
            await interaction.response.send_message(content=f"You aren't that maker of this poll",
                                                    ephemeral=True)
        else:
            remove_modal = RemoveModal(title="Remove Question Form",
                                       question_list=self.question_dict[(interaction.guild_id,
                                                                         self.poll_name)])
            await interaction.response.send_modal(remove_modal)

    @discord.ui.button(label="List Questions", row=0, style=discord.ButtonStyle.primary)
    async def list_button_callback(self, button: discord.Button, interaction: discord.Interaction):
        if interaction.user != self.maker:
            await interaction.response.send_message(content=f"You aren't that maker of this poll",
                                                    ephemeral=True)
        else:
            questions = self.question_dict[(interaction.guild_id, self.poll_name)]
            embeds = []
            for i, v in enumerate(questions, 1):
                embeds.append(v.as_embed(i))
            await interaction.response.edit_message(embeds=embeds)

    @discord.ui.button(label="Finalize Poll", row=1, style=discord.ButtonStyle.green)
    async def finalize_button_callback(self, button: discord.Button, interaction: discord.Interaction):
        if interaction.user != self.maker:
            await interaction.response.send_message(content=f"You aren't that maker of this poll",
                                                    ephemeral=True)
        else:
            await interaction.response.send_message(view=PollButtons(self.poll_name,
                                                                     interaction.guild_id,
                                                                     question_dict=self.question_dict))
            await self.message.delete()


class PollButtons(discord.ui.View):
    def __init__(self, poll_name, guild_id, question_dict, result=None, question_num=0):
        super().__init__(timeout=None)
        if result is None:
            result = {}
        self.poll_name = poll_name
        self.question_dict = question_dict
        self.question_num = question_num
        self.guild_id = guild_id
        self.selector = self.make_select()
        self.add_item(self.selector)
        self.results = result
        self.answers = {}  # key:user_name value:voted on answer

    def as_selector_options(self):
        options = []
        answers = self.question_dict[(self.guild_id, self.poll_name)][self.question_num].options.split(",")
        for i in answers:
            options.append(discord.SelectOption(label=i))
        return options

    def make_select(self):
        answer_selector = discord.ui.Select(
            min_values=1,
            max_values=1,
            options=self.as_selector_options()
        )

        async def answer_select(interaction: discord.Interaction):
            choice = interaction.data["values"][0]
            self.answers[interaction.user] = choice
            await interaction.response.send_message(content=f"{interaction.user.name} voted for: {choice}",
                                                    ephemeral=True)

        answer_selector.callback = answer_select
        return answer_selector

    def result_embeds(self):
        finish_embed = discord.Embed(title=f"Poll Finish({self.poll_name})")
        embeds = [finish_embed]
        for question in self.results.keys():
            result_embed = discord.Embed(title=question)
            for option in self.results[question].keys():
                result_embed.add_field(name=option, value=self.results[question][option])
            embeds.append(result_embed)
        return embeds

    @discord.ui.button(label="Next Question", row=1, style=discord.ButtonStyle.primary)
    async def next_button_callback(self, button: discord.Button, interaction: discord.interactions):
        question_list = self.question_dict[(self.guild_id, self.poll_name)]
        self.results[question_list[self.question_num].question] = {}
        for i in question_list[self.question_num].options.split(","):
            self.results[question_list[self.question_num].question][i] = 0

        for user in self.answers.keys():
            self.results[question_list[self.question_num].question][self.answers[user]] += 1

        if self.question_num >= len(question_list) - 1:
            embed = self.result_embeds()
            await interaction.response.edit_message(embeds=embed, view=None)
        else:
            await interaction.response.edit_message(view=PollButtons(self.poll_name,
                                                                     self.guild_id,
                                                                     self.question_dict,
                                                                     self.results,
                                                                     self.question_num + 1))
