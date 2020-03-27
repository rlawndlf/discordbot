import discord
import os
client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("뮤직봇설명")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("!뮤직봇도움말"):
        await message.channel.send(";;join=봇참가,;;leave=봇퇴장,;;play 노래제목=노래제목으로유튜브검색후곡설정,;;queue=재생목록,;;nowplaying=재생중인곡,;;skip=노래넘기기,;;pause=일시정지,;;unpause=다시재생")


        access_token = os.environ["BOT_TOKEN1"]
        client.run(access_token)