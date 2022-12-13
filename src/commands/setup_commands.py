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
            mention = ctx.author.mention
            discord_id: str = ctx.author.id

            await self.database.insert_user(
                discord_id, fpl_id
            ) if fpl_id.isdigit() else await self.initial_setup(ctx)
        except:
            await ctx.send(
                content=f"{mention}\n :thumbsdown: oops... something went wrong, please make sure your fpl id is a number, use **+setup help** for help finding your fpl id and **+help** for any other useful commands"
            )

    async def initial_setup(self, ctx: commands.Context) -> None:
        """
        This function guides the user through the process of finding their FPL ID
        and setting up their account.

        :param ctx: The context of the command invocation.
        :return: None
        """
        embed = discord.Embed(title="Setup")
        embed.add_field(
            name="Intructions:",
            value='Type **+setup "FPL id" ** \n if you do not know how to get your FPL id please type  **+XXX**',
        )
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Setup(bot))
