import discord
import random
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import asyncio
import time
import yaml

client = commands.Bot('!!')

YML_DATA = './../data/data.yml'

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

@client.command()
async def say(ctx,*, arg):
    await ctx.send(arg)

@client.listen('on_message')
async def on_message(message):
    
    with open(YML_DATA) as stream:
        data = yaml.load(stream)
        user = data["user"]

    # 自分以外のユーザに返信
    if message.author == client.user or message.author.bot:
        return

    #挨拶
    if message.content.startswith('こんにちは'):
        msg = 'こんにちは！{0}さん'.format(message.author.display_name)
        await message.channel.send(msg)

    if message.content.startswith('おやすみ'):
        night = [ 'おやすみなさい。\n明日もよい一日でありますように…', 'おやすみなさい\n一日、お疲れ様でした']
        await message.channel.send(random.choice(night))

    if message.content.startswith('おはよう'):
        day = ['おはようございます。\n今日も一日がんばりましょう！', 'おはようございます。\nご飯は摂られましたか？']
        await message.channel.send(random.choice(day))
        
    #ヘルプコマンド
    if message.content.startswith('!!help'):
        embed = discord.Embed(title='**Help Menu**',
        description='全体でコマンド改良中\n基本的な会話、挨拶に反応します。\nPrefixは**!!**に設定されています。',colour=0x2ea9ff)
        embed.add_field(name='Commands',
        value='**!!invite**で招待リンクを所得出来ます。\n**!!server**でサーバー情報を取得できます。\n挨拶に反応します。話しかけてみて下さい！')
        await message.channel.send(embed=embed)

    #更新情報表示
    if message.content.startswith('!!update'):
        embed = discord.Embed(title='**Recent Updates**',description='CommandBot化しました。\n24H起動の準備中です。',colour=0x2ea9ff)
        embed.add_field(name='version',value='α版(試験運用段階)')
        await message.channel.send(embed=embed)

    #招待リンク取得用
    if message.content.startswith('!!invite'):
        embed = discord.Embed(title='**Invite Link**',
        description='[このBotの招待リンク](https://discordapp.com/api/oauth2/authorize?client_id=478914225062805504&permissions=2146954743&scope=bot)',colour=0x2ea9ff)
        embed.add_field(name='※注意',value='導入をお考えのサーバーの管理者権限が必要です。\n権限は必要に応じて調整して下さい。\n[このBotのサポートサーバー](https://discord.gg/wdhCCJD)')
        await message.channel.send(embed=embed)
    
    #ユーザ認証
    if message.content.startswith('!replay'):
        if message.author.id == user:
            await message.channel.send('Yes')
        else:
            await message.channel.send('No')

    #DMで!ch <チャンネルID> を打った後、DMで言った内容を発言させるプログラム
    global channel
    if isinstance(message.channel,discord.DMChannel) and message.author.id == user:
        if message.content.startswith('!set'):
             split = message.content.split()
             channel = client.get_channel(int(split[1]))
             await message.channel.send('{0}に設定しました。'.format(channel.mention))
        else: 
             await channel.send(message.content)

    #ランダムモジュール動作確認用
    if message.content.startswith('フルーツ'):
        fruit = ['りんご', 'バナナ', 'メロン','ぶどう']
        await message.channel.send(random.choice(fruit))

    #メッセージ削除
    if message.content == ('!!delete.test'):
        await message.delete()

    #役職付与 誰でも出来ちゃう版
    if message.content.startswith('!!add_test'):
            role = message.guild.get_role(502531768268619778)
            await message.author.add_roles(role)
            await message.channel.send('付与しました。')

    if message.content.startswith('!!Add_sp'):
        await  message.author.add_roles(message.guild.get_role(494852513908916226))
    
    # user info
    if message.content.startswith('!!userinfo'):
        if(message.author.status == discord.Status.online):
            status = "オンライン"
        elif(message.author.status == discord.Status.offline or message.author.status == discord.Status.invisible):
            status = "オフライン"
        elif(message.author.status == discord.Status.dnd or message.author.status == discord.Status.do_not_disturb):
            status = "起こさないで"
        elif(message.author.status == discord.Status.idle):
            status = "退席中"
        else:
            status = "その他"

        # ニックネームの有無で分岐
        if(message.author.nick != None):
            embed = discord.Embed(title='Userinfo',
            description='名前: ' + message.author.mention + '\nニックネーム: ' + message.author.nick + 
            '\nアカウント作成日: ' + str(message.author.created_at) + '\nサーバ参加日: ' + str(message.author.joined_at) + '\n現在のステータス: ' + status,
            colour=0x2ea9ff)
        else:
            embed = discord.Embed(title='Userinfo',
            description='名前: ' + message.author.mention + '\nアカウント作成日: ' + str(message.author.created_at) +
            '\nサーバ参加日: ' + str(message.author.joined_at) + '\n現在のステータス: ' + status
            ,colour=0x2ea9ff)
        await message.channel.send(embed=embed)



    #役職付与 付与者制限有
    splietd = message.content.split()
    if splietd[0] == '!!staff':
        member = message.author
        role = message.guild.get_role(465890968957354023)
        if role in member.roles:
            member = message.guild.get_member(int(splietd[1]))
            role = message.guild.get_role(502548685457063936)
            await member.add_roles(role)
            await message.channel.send('付与しました。')

# サーバステータス表示
@client.command()
async def server(ctx):
    guild = ctx.guild
    description = '''
    サーバー名称:{0.name}
    サーバー所有者:{0.owner.mention}
    サーバー人数:{0.member_count}人
    チャンネル数:{1}個
    サーバー作成日:{0.created_at}
    Server_ID:{0.id}
    '''.format(guild, len(guild.channels))
    embed = discord.Embed(title='サーバー情報', description=description,colour=0x2ea9ff)
    embed.set_thumbnail(url=guild.icon_url)
    await ctx.send(embed=embed)

#BANコマンド
@client.command()
async def ban(ctx, member: discord.Member):
    await member.ban()
    await ctx.send('BANしました。')

#入退出メッセージ
@client.event
async def on_member_join(member):
    if 'discord.gg' in member.display_name:
        await member.ban(reason='招待リンクが名前に含まれている為BANされました。'
        ,delete_message_days=1)
    name = member.display_name
    embed = discord.Embed(title='{0}さんが参加しました。'.format(name),colour=0x2ea9ff,description=
    'ようこそ{0}さん\nよろしくお願いします！\nこのサーバーの現在の人数は{1}人です。'.format(name,member.guild.member_count))
    embed.set_thumbnail(url=member.avatar_url)
    channel = next(c for c in member.guild.channels if c.name == 'general-chat')
    await channel.send(embed=embed)

@client.event
async def on_member_remove(member):
    name = member.display_name
    embed = discord.Embed(title='{0}さんが退出しました。'.format(name),
     colour=0x2ea9ff, description='{0}さん、ご利用ありがとうございました。\nこのサーバーの現在の人数は{1}人です'
     .format(name, member.guild.member_count))
    embed.set_thumbnail(url=member.avatar_url)
    channel = next(c for c in member.guild.channels if c.name == 'general-chat')
    await channel.send(embed=embed)


@client.event
async def on_ready():
    print('起動が完了しました。')
    await client.change_presence(activity=discord.Game(name="α版試験運用｜!!help",type=discord.ActivityType.playing))
    print(client.user.name)
    print(client.user.id)
    print('------')
    loop = asyncio.get_event_loop()
    client.loop.create_task(greeting_schedule(client.get_channel(507552110900936711),loop))

# あいさつする関数
async def on_greeting(channel):
    embed = discord.Embed(title='おはようございます。',colour=0x2ea9ff)
    await channel.send(embed=embed)

# 挨拶を実行する
@asyncio.coroutine
async def greeting_schedule(channel, loop):
    while True:
        if time.strftime('%H:%M:%S',time.localtime())=='6:00:00':
            await on_greeting(channel)

# 起動時
f = open("./../data/data.yml", "r")
token= yaml.load(f)
f.close()

client.run(token["token"])