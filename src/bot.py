import discord
from discord.ext import commands
from config import Config


class Bot:
    """A Discord bot that responds to commands."""

    def __init__(self, token: str, bot: commands.Bot) -> None:
        self.token = token
        self.bot = bot

    def run(self):
        self.bot.run(self.token)


if __name__ == "__main__":
    bot = Bot(
        token=Config.TOKEN,
        bot=commands.Bot(command_prefix="!", intents=discord.Intents.default()),
    )
    bot.run()
