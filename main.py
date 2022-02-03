import discord
import discord as dc
from discord.ext import commands

targetPlayerName = ""
targetGameName = ""


def getBotToken():
    return open("E:\Öffentliche Dokumente\BanBot-Verification\keys.txt").read()


intent = dc.Intents.default()
intent.members = True

TOKEN = getBotToken()

bot = commands.Bot(command_prefix="$")
client = discord.Client()

print("Booting..")


@client.event
async def on_ready():
    print("Client-Bot is now online!")


@bot.event
async def on_ready():
    print("Command-Bot is now online!")


@bot.command()
async def ping(ctx):
    await ctx.channel.send("pong")


bot.run(TOKEN)
client.run(TOKEN)
