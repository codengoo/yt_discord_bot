import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load token từ .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Khởi tạo bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Khi bot khởi động
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

# Command kiểu prefix: !hello
@bot.command()
async def hello(ctx):
    await ctx.send("👋 Hello! Bot đang hoạt động nè đồ ngu")

# Slash command kiểu modern: /ping
@bot.tree.command(name="ping", description="Kiểm tra độ trễ của bot")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"🏓 Pong! Latency: {round(bot.latency * 1000)}ms")

# Sync slash command khi start
@bot.event
async def setup_hook():
    await bot.tree.sync()
    print("🔁 Slash commands synced.")

# Run bot
bot.run(TOKEN)
