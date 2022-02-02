import discord as dc

def getBotToken():
    return open("E:\Öffentliche Dokumente\BanBot-Verification\keys.txt").read()

intent = dc.Intents.default()
intent.members = True

TOKEN = getBotToken()

client = dc.Client()

print("Booting..")


@client.event
async def on_ready():
    print("Bot is now online")



client.run(TOKEN)