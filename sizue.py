import discord
import time
import datetime
from discord.ext import commands

client = commands.Bot('s!')

class Normal_Command:
    __slots__ = ('client', 'name', 'data', 'categories')

    def __init__(self, client, data, name=None):
        self.client = client
        self.name = name if name is not None else type(self).__name__
        self.data = data

#発言コマンド
@client.command()
async def say(ctx,*,arg):
    await ctx.send(arg)

@client.event
async def on_ready():
    print('起動が完了しました。')
    await client.change_presence(activity=discord.Game(name="村運営",type=discord.ActivityType.playing))

@client.listen('on_message')
async def on_message(message):
    if message.author == client.user or message.author.bot:
        return
    
    if message.content.startswith('s!now'):
        now = datetime.datetime.now()
        await message.channel.send('今は{0:%Y.%m/%d %H:%M}です'.format(now))

    #メッセージ削除
    if message.content == ('死ね'):
        await message.delete()
        await message.channel.send('不適切な発言は止めて下さい！')
    
    if message.content == ('消えろ'):
        await message.delete()
        await message.channel.send('不適切な発言は止めて下さい！')

#アカウント登録コマンド
@client.command()
async def join(ctx):
    sopaca = ctx.guild.get_role(507910389757902849)
    if sopaca not in ctx.author.roles:
        content = """
{0}さんが村民登録されました
<#507951668290256918>で自己紹介をしてみましょう！
""".format(ctx.author.mention)
        await ctx.author.add_roles(sopaca)
        await ctx.send(content)
    else:
        await ctx.send('登録されていますよ？')


client.run('NDgzMDc3MDIzNjk5NDM1NTIw.DmOMOA.zL4ArnO1tNdJFY8b6zaVVi5mgwA')