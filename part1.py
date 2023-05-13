import nextcord
from nextcord.ext import commands
import requests, json, random, datetime, asyncio
import os

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)

@bot.command(name="test")
async def SendMessage(ctx):
    await ctx.send('still alive')

@bot.command(name="pic")
async def SendMessage(ctx):
    await ctx.send('https://tenor.com/view/trollge-we-do-a-little-trolling-2137-papaj-jp2-gif-23630507')

async def schedule_daily_message():
    sent_today = False  # flag to indicate whether the image has been sent today
    while True:
        now = datetime.datetime.now()
        then = now.replace(hour=17, minute=34)
        wait_time = (then-now).total_seconds()
        await asyncio.sleep(wait_time)

        if not sent_today:
            channel = bot.get_channel(1106949197451776132)
            await channel.send("https://tenor.com/view/trollge-we-do-a-little-trolling-2137-papaj-jp2-gif-23630507")
            sent_today = True

@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}")
    await schedule_daily_message()

if __name__ == '__main__':
    bot.run(os.environ["DISCORD_TOKEN"])
