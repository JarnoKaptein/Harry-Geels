import os
from discord_webhook import DiscordWebhook
from keep_alive import keep_alive
import nextcord
from nextcord.ext import commands

client = commands.Bot()
SecretWeb = "https://discord.com/api/webhooks/1030466451112468501/zxq6K-bdMisxOjkZ1rfDpIMTly0FE_6Jk5mkXoara1i6S_90yO1wi62ydZvfnF6V9pAv"
AlgemeenWeb = "https://discord.com/api/webhooks/1029746331624935456/oGqPTGYyQ0PVroe81v8KKIPMGjD-N7zWrL4fxpUklDzM-wozFRTU96MymzNNLjR1vW-v"

@client.event
async def on_ready():
  game = nextcord.Game("met zijn doekoes.")
  await client.change_presence(status=nextcord.Status.idle, activity=game)
  
  print(f"{client.user.name} is ready for take-off.")
  webhook = DiscordWebhook(url=SecretWeb, content=f"{client.user.name} booted <@707654800904290376>").execute()

@client.event
async def on_message(message):
  await message.reply("Cock")

keep_alive()
token = os.environ['token']
client.run(token)
