import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("play")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕하세요")
    if message.content.startswith("!권경운"):
        await message.channel.send("케인장인")
    if message.content.startswith("!김주일"):
        await message.channel.send("아트록스원챔")
    if message.content.startswith("!출석"):
        await message.channel.send("출석되셧습니다")
    if message.content.startswith("!김도완"):
        await message.channel.send("몰라")
    if message.content.startswith("!이경민"):
        await message.channel.send("몰라")
    if message.content.startswith("!권혁무"):
        await message.channel.send("몰라")
    if message.content.startswith("!도움말"):
        await message.channel.send("!를 쓰고 권경운.김주일.출석.김도완.안녕.이경민.권혁무 등등을 쓰면된다")

        
        
  access_token = os.environ［BOT_TOKEN］ 
  client.run("access_token")
