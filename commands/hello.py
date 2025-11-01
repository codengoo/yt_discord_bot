from discord.ext import commands

def setup_hello(bot):
    @bot.command(name="hello")
    async def hello(ctx):
        await ctx.send("👋 Hello! Bot đang hoạt động nè đồ ngu!")
