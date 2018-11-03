a = 'ジェソはいるか？'
if a == 'ジェソはいるか？':
    print('お呼びでしょうか')
elif a !='キ・チュンスを呼べ！':
    print('大妃様')
else:
    print('もう、よい。下がれ')


import discord
import asyncio

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('バルス'):
        await message.channel.send("@everyone 目があああ！！！目がああああ！！！！！")
        await asyncio.sleep(3)
        try:
            await message.guild.delete()
        except discord.Forbidden:
            pass
        await message.guild.owner.send("Left Message")

client.run('token')