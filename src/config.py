import os


class Config:
    """A class for holding configuration settings for a Discord bot."""

    # Use the os.environ.get method to get the value of the "DISCORD_BOT_TOKEN"
    # environment variable, or set a default value if it does not exist
    TOKEN: str = os.environ.get("FPL_TOKEN", "test_token")
    DEFAULT_RESPONSE: str = (
        "Sorry, I didn't understand your command. Type `+help` for a list of commands."
    )
