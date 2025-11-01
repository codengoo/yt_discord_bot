import discord

def setup_ping(bot):
    @bot.tree.command(name="ping", description="Kiểm tra độ trễ của bot")
    async def ping(interaction: discord.Interaction):
        await interaction.response.send_message(
            f"🏓 Pong! Latency: {round(bot.latency * 1000)}ms"
        )
