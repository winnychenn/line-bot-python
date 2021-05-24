#!/usr/bin/env python3
# coding=utf8

import discord
from discord_webhook import DiscordWebhook

bot = discord.Client()

#bot = commands.Bot(command_prefix='$', description='A bot that greets the user back.')

@bot.event
async def on_ready():
    print('userid:',bot.user.id)
    print('username:',bot.user.name)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    #如果包含 ping，機器人回傳 pong
    if message.content == '測試':
        await message.channel.send('不給測試')
        await message.channel.send(message.author.id)
        await message.channel.send(message.author.name)
        await message.channel.send(' <@350265813695201280> 測試測試') 
    await message.channel.send(message)
    print(message)
    if message.content == '群組':
        guilds = await bot.fetch_guilds(limit=150).flatten()
        for i in guilds:
            #由於我們只要 guilds 的name 就好，當然也可以獲取 id~
            await message.channel.send(i.name)

    if message.content == '名單':
        member_list = ''
        for member in ctx.message.server.members:
            member_list += member.name
        print(member_list)

bot.run('ODQwMTUxMTI0Mzg4NjEwMDc4.YJUBtQ.dgK3Jc1xAW72IkjHkTj0MFwJ714') 


