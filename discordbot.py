import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    
        

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
