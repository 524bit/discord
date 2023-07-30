import discord
import os
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle
import datetime

bot = discord.Bot()

async def on_message(message):
    if message.author == bot.user:
        return

#기본키--------------------------------------------------------------------------------------------------------------------

@bot.event 
async def on_ready():
    print("logged in as {0.user}".format(bot))
    await bot.change_presence(activity=discord.Game(f"{len(bot.guilds)}개의 서버에서 과로사\n"))

#명령어------------------------------------------------------------------------------------------------------------------------------

@bot.command(description="퐁!")
async def ping(ctx):
    await ctx.respond(f'🏓pong! {round(round(bot.latency, 4)*1000)}ms')

@bot.command(description="증거인멸!")
@commands.has_permissions(ban_members = True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)
    await ctx.respond('cleared!')

@bot.command(description="임베드 생성")
async def 임베드(ctx: discord.ApplicationContext, 제목, 내용, 싸인):
    embed = discord.Embed(title=f"{제목}", description=f"{내용}",color=0xe890ff)
    embed.set_footer(text=f"{싸인}")
    await ctx.respond(embed=embed)

@bot.command(description="타임아웃")
@commands.has_permissions(ban_members = True)
async def 타임아웃(ctx: discord.ApplicationContext, member: discord.Member, minutes: int, reason):
    duration = datetime.timedelta(minutes=minutes)
    await member.timeout_for(duration)
    embed = discord.Embed(title=f"주둥이에 {minutes}분동안 붙어있는 본드를 붙였어요", description=f"{member} 은 {reason} 의 사유로 {minutes} 분 동안 타임아웃")
    await ctx.respond(embed=embed)

@bot.command(description="유저를 뻥 차버리자")
@commands.has_permissions(administrator=True)
async def 킥(ctx, user : discord.Member,*,reason):
  await user.kick(reason=reason)
  embed = discord.Embed(title="뻥하고 날라갔어요", description=f"{user} 은 {reason} 의 사유로 {ctx.author} 에게 추방")
  await ctx.respond(embed=embed)

@bot.command(description="유저의 이름을 블랙리스트에 올리자")
@commands.has_permissions(administrator=True)
async def 벤(ctx, user : discord.Member,*,reason):
  await user.ban(reason=reason)
  embed = discord.Embed(title="블랙리스트에 올렸어요", description=f"{user} 은 {reason} 의 사유로 {ctx.author} 에게 벤")
  await ctx.respond(embed=embed)

#토큰-----------------------------------------------------------------------------------------------------------------------------

bot.run('TOKEN')