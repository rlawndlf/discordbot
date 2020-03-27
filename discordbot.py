import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("아무거나")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕하세요")
    if message.content.startswith("!출석"):
            await message.channel.send("출석되셨습니다")
    if message.content.startswith("!권경운"):
        await message.channel.send("케인장인")
    if message.content.startswith("!김주일"):
        await message.channel.send("아트록스원챔")
    if message.content.startswith("!김도완"):
        await message.channel.send("아칼리?카타리나?장인")
    if message.content.startswith("!이경민"):
        await message.channel.send("가렌장인")
    if message.content.startswith("!권혁무"):
        await message.channel.send("몰라요")
    if message.content.startswith("!도움말"):
        await message.channel.send("!를 치고 이름이나 출석,안녕을 입력해보세요")
     if message.content.startswith("!권순형"):
        await message.channel.send("모른다고")
         if message.content.startswith("!박재윤"):
        await message.channel.send("진충")
      if message.content.startswith("!박재연"):
        await message.channel.send("계정빌려주는애")
      if message.content.startswith("!종료"):
        await message.channel.send("안녕히가세요")
      if message.content.startswith("!설명충"):
        await message.channel.send("저입니다만?")
       if message.content.startswith("!야"):
        await message.channel.send("뭐")
       if message.content.startswith("!황현수"):
        await message.channel.send("노틸.")
        

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
