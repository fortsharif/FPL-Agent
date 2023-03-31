import asyncio


from discord.ext import commands  # type: ignore

from config import Config


class Bot:
    """A Discord bot that responds to commands."""

    def __init__(self, token: str, bot: commands.Bot) -> None:
        self.token = token
        self.bot = bot

    def run(self):
        self.bot.run(self.token)

    async def load_extension(self, cog):
        await self.bot.load_extension(cog)


if __name__ == "__main__":
    bot = Bot(
        token=Config.TOKEN,
        bot=commands.Bot(command_prefix="!", intents=Config.INTENTS),
    )
    asyncio.run(bot.load_extension("commands.help_commands"))
    asyncio.run(bot.load_extension("commands.setup_commands"))
    asyncio.run(bot.run())
