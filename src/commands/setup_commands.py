import sqlite3


import discord

from discord.ext import commands


from config import Config

from database import Database


class Setup(commands.Cog):
    def __init__(self, bot, database=Database()):
        self.bot = bot
        self.database: Database = database

    @commands.command(aliases=["s"], description=Config.SETUP_DESCRIPTION)
    async def setup(self, ctx: commands.Context, *, fpl_id: str = "") -> None:
        """
        This function sets up the user with the provided FPL ID.
        If no FPL ID is provided, the function guides the user through
        the process of finding their FPL ID.

        :param ctx: The context of the command invocation.
        :param fpl_id: The FPL ID of the user (optional).
        :return: None
        """
        try:
            discord_id: str = ctx.author.id
            mention = ctx.author.mention

            if fpl_id.isdigit():
                self.database.insert_user(discord_id, fpl_id)
            else:
                raise TypeError("FPL id is not a digit")

            await ctx.send(
                f"{mention} Thats all setup for you,\
                try !help for commands to use!"
            )

        except TypeError as T:
            print(T)
            await self.initial_setup(ctx)
        except sqlite3.OperationalError as S:
            print(S)
            await ctx.send("Something went wrong, please contact an admin!")

    async def initial_setup(self, ctx: commands.Context) -> None:
        """
        This function guides the user through the process of finding
        their FPL ID and setting up their account.

        :param ctx: The context of the command invocation.
        :return: None
        """
        mention = ctx.author.mention
        embed = discord.Embed(title="Setup")
        embed.add_field(
            name="Intructions:",
            value=f'{mention} Type **+setup "FPL id" ** \n if you do not know \
            how to get your FPL id please type  **+XXX**',
        )
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Setup(bot))
