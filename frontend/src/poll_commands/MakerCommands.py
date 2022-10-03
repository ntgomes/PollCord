import discord
from discord.ext import commands
from poll_commands.components.modals import OpenPollModal, MCPollModal


class PollButtons(discord.ui.View):
    def __init__(self, poll_name, question_dict, *items):
        super().__init__(*items)
        self.poll_name = poll_name
        self.question_dict = question_dict

    @discord.ui.button(label="List Questions", row=2, style=discord.ButtonStyle.primary)
    async def list_button_callback(self, button: discord.Button, interaction: discord.Interaction):
        questions = self.question_dict[(interaction.guild_id, interaction.channel_id, self.poll_name)]
        embeds = []
        for i, v in enumerate(questions, 1):
            embeds.append(v.as_embed(i))
        await interaction.response.edit_message(embeds=embeds)

    @discord.ui.select(
        placeholder="Select message to delete",
        max_values=1,
        min_values=1,
        options=[discord.SelectOption(label="Vanilla", description="Pick this one!")]
    )
    async def select_callback(self, select, interaction):
        await interaction.response.send_message(f"{select.values[0]}")
        select.disabled = True

    @discord.ui.button(label="Add MC Question", row=0, style=discord.ButtonStyle.primary)
    async def mc_button_callback(self, button: discord.Button, interaction: discord.Interaction):
        new_modal = MCPollModal(title="Multiple Choice Form")
        await interaction.response.send_modal(new_modal)
        await new_modal.wait()
        try:
            self.question_dict[(interaction.guild_id, interaction.channel_id, self.poll_name)].append(new_modal.val)
        except KeyError:
            self.question_dict[(interaction.guild_id, interaction.channel_id, self.poll_name)] = [new_modal.val]

    @discord.ui.button(label="Add Open-Ended Question")
    async def open_button_callback(self, button: discord.Button, interaction: discord.Interaction):
        new_modal = OpenPollModal(title="Open Choice Form")
        await interaction.response.send_modal(new_modal)
        await new_modal.wait()
        try:
            self.question_dict[(interaction.guild_id, interaction.channel_id, self.poll_name)].append(new_modal.val)
        except KeyError:
            self.question_dict[(interaction.guild_id, interaction.channel_id, self.poll_name)] = [new_modal.val]


class MakerCommands(commands.Cog):
    ctx_parse = discord.ApplicationContext

    def __init__(self, bot: discord.Bot):
        self.bot = bot
        self.question_dict = {}

    @commands.slash_command(name="makepoll", guild_id=[1021553449210499133], description="makes a poll")
    async def make_poll(self, ctx: ctx_parse, poll_name: str):
        print(type(ctx.guild_id), type(ctx.channel_id))
        print(poll_name)
        await ctx.send(f'Buttons for poll {poll_name}: ',
                       view=PollButtons(poll_name=poll_name, question_dict=self.question_dict))
