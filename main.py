import os
from keep_alive import keep_alive
import nextcord
from nextcord.ext import commands

client = commands.Bot()


@client.event
async def on_ready():
    game = nextcord.Game("met zijn doekoes.")
    await client.change_presence(status=nextcord.Status.idle, activity=game)
    print(f"{client.user.name} booted up.")

keep_alive()
token = os.environ['token']
client.run(token)
