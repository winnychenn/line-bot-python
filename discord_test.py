#!/usr/bin/env python3
# coding=utf8

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
#bot = discord.Client()

@bot.command(name="test")
async def SendMessage(ctx):
    await ctx.channel.send(ctx.guild.members)
    member_list = ''
    for member in ctx.guild.members:
        member_list += member.name
    print(member_list)
    

bot.run('ODQwMTUxMTI0Mzg4NjEwMDc4.YJUBtQ.dgK3Jc1xAW72IkjHkTj0MFwJ714')
