import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Import commands
from commands.hello import setup_hello
from commands.ping import setup_ping

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

# Đăng ký các command
setup_hello(bot)
setup_ping(bot)

# Sync slash command khi start
@bot.event
async def setup_hook():
    await bot.tree.sync()
    print("🔁 Slash commands synced.")

# Run bot
bot.run(TOKEN)
