import discord
from discord.ext import commands

TOKEN = "NTkwMTg2NzQzOTE2MTM0NDAx.XQekgg.aji-n0h5CguKllQRUWDXN2r4YZI"

bot = commands.Bot(command_prefix='#')

@bot.event
async def on_ready():
    print("bot is ready")



bot.run(TOKEN)
    
