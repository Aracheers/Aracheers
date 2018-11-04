import discord

client = discord.Client()

@client.event
async def on_message(message):
    # 自分自身以外を対象に返信
    if message.author == client.user:
        return

    if message.content.startswith('システムリンク構築'):
        msg = '接続成功 システムとのリンクを構築しました。'
        await message.channel.send( msg)

    if message.content.startswith('!Task_start'):
        if message.author.id == 441157692464300032:
            await message.channel.send('携帯型心理診断鎮圧執行システム\nドミネーター起動しました。\nユーザー認証あらち監視官 公安局刑事課所属\n使用許諾確認 適正ユーザーです。')
        else:
            await message.channel.send('Error!\n不正ユーザーです。')

    if message.content.startswith('!under_100'):
        msg = '執行モード ノンリーサル:パラライザー\n落ち着いて照準を定め対象を無力化してください。'
        await message.channel.send( msg)

    if message.content.startswith('!over_100'):
        msg = '執行モード リーサル：エレミネーター\n慎重に照準を定め対象を排除してください。'
        await message.channel.send( msg)

    if message.content.startswith('!s_targer'):
        msg = '対象の脅威判定が更新されました\n執行モード デストロイ:デコンポーザー\n対象を完全排除します。ご注意ください。'
        await message.channel.send( msg)

@client.event
async def on_ready():
    print('ログインしました')
    await client.change_presence(activity=discord.Game(name="タスク待機"))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NDc4OTY3MTk3MDg0MTU1OTA0.DlSY7w.GSJAadr8olcPcAMF24bQC8lacfQ')