import os


import discord  # type: ignore


class Config:
    """A class for holding configuration settings for a Discord bot."""

    # Use the os.environ.get method to get the value of the "DISCORD_BOT_TOKEN"
    # environment variable, or set a default value if it does not exist
    TOKEN: str = os.environ.get("FPL_TOKEN", "test_token")
    DEFAULT_RESPONSE: str = (
        "Sorry, I didn't understand your command. Type"
        " `+help` for a list of commands."
    )
    INTENTS = discord.Intents.default()
    INTENTS.message_content = True
    SETUP_DESCRIPTION: str = (
        "Link your discord to your FPL ID using +setup"
        " '123' WHERE '123' is replaced with your FPL ID."
    )
