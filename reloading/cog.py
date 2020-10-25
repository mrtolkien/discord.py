from discord.ext import commands


# This is crucial for it to be treated as an *extension* by discord.py
#   See the doc here: https://discordpy.readthedocs.io/en/latest/ext/commands/extensions.html
#   If developing multiple cogs, they can just all be loaded from a single extension
def setup(bot):
    bot.add_cog(TestCog(bot))


class TestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send("NOT")
