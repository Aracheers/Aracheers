import discord
import random
from discord.ext import commands

client = commands.Bot('a!')

@client.listen('on_message')
async def on_message(message):
    # 自分以外のユーザに返信
    if message.author == client.user:
        return

    #以下rewrite版

    #招待リンク取得用
    if message.content.startswith('a!invite'):
        embed = discord.Embed(title='**Invite Link**',
        description='[このBotの招待リンク](https://discordapp.com/api/oauth2/authorize?client_id=485014555509129216&permissions=8&scope=bot)',
        colour=0x2ea9ff)
        embed.add_field(name='※注意',value='導入をお考えのサーバーの管理者権限が必要です。')
        await message.channel.send(embed=embed)

    global channel
    if isinstance(message.channel,discord.DMChannel) and message.author.id == 441157692464300032:
        if message.content.startswith('!ch'):
             split = message.content.split()
             channel = client.get_channel(int(split[1]))
             await message.channel.send('{0}に設定しました。'.format(channel.mention))
        else: 
             await channel.send(message.content)


    if message.content.startswith('!hello'):
        await message.channel.send('Hello')

# サーバステータス表示
@client.command()
async def server(ctx):
    guild = ctx.guild
    description = '''
    サーバーの名前:{0.name}
    サーバーのオーナー:{0.owner.mention}
    サーバーの人数:{0.member_count}
    サーバーのチャンネル数:{1}
    サーバー作成日:{0.created_at}
    サーバーのID:{0.id}
    '''.format(guild, len(guild.channels))
    embed = discord.Embed(title='サーバー情報', description=description,colour=0x0000ff)
    embed.set_thumbnail(url=guild.icon_url)
    await ctx.send(embed=embed)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="α版試験運用",
    type=discord.ActivityType.playing))
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NDg1MDE0NTU1NTA5MTI5MjE2.Dpo6Dw.WgYrZnwJ14tcn261KGCFog8jGVQ')