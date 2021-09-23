# Imports

import sys
import random

import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get
from timeit import default_timer as timer
import asyncio
from datetime import datetime


# Bot config

intents = discord.Intents.all()
intents.members = True
intents.presences = True
load_dotenv()
TOKEN = (' REMOVED ')

bot = commands.Bot(command_prefix="#", intents = intents, help_command=None)





# Main Variables - Perm Variables are below Vital Functions

build_ldd = "Build loaded. Use system_info for information on the build."
last_half = "Executing the last half of on_ready"
ch = "Ping"
botlog = 887385137879339020

setup = False
setup_author = 0
mod_one = "Owner"
mod_two = "staff"
mod_three = "Proper Idiots"














# Main Events

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    
    activity = discord.Game(name="https://twitch.tv/proper_idiots_")
    await bot.change_presence(status=discord.Status.online, activity=activity)



    botlog_func = bot.get_channel(int(botlog))
    await botlog_func.send(build_ldd)





# Functions



async def change_db(ch_name, new):
                fetch_arg = ch_name
                db_func = discord.utils.get(bot.get_all_channels(), name=fetch_arg)
                channel_id = db_func.id
                db_user = bot.get_channel(channel_id)


                msg_info = discord.utils.get(await db_user.history(limit=100).flatten())
                msg = msg_info.content
                msg_id = msg_info.id
                msg_fetch = await db_user.fetch_message(msg_id)
                new_db = str(new)
                await msg_fetch.edit(content=new_db)

async def check_db(check: str):
                fetch_arg = check
                db_func = discord.utils.get(bot.get_all_channels(), name=fetch_arg)
                channel_id = db_func.id
                db_user = bot.get_channel(channel_id)


                msg_info = discord.utils.get(await db_user.history(limit=100).flatten())
                msg = msg_info.content
                msg_id = msg_info.id
                msg_fetch = await db_user.fetch_message(msg_id)
                return msg


# Side Events (or events that use functions)

@bot.event
async def on_member_join(user: discord.Member):
    perm_on_member_join = await check_db("perm_on_member_join")
    if perm_on_member_join == True:
        db_on_member_join_ch = bot.get_channel(890181705128902706)
        message = await db_on_member_join_ch.fetch_message(890529102312906752)
        channel = bot.get_channel(int(message.content))
        await channel.send(str(content_on_member_join))
    else:
        return






# General commands


@bot.command(brief="Checks if the bot's online", description="This command checks if the bot's online. Aliases: c", aliases=["c"])
async def check(ctx):
  await ctx.send(ch)


@bot.command()
async def help(ctx):
    embedVar = discord.Embed(title="Help;", color=0x2C5ED1)
    embedVar.add_field(name="General", value="check", inline=False)
    embedVar.add_field(name="Moderation", value="config, mute, unmute, kick, ban, unban, purge, restart", inline=False)
    embedVar.add_field(name="Developer", value="edit_db, view_db", inline=False)
    embed = await ctx.send(embed=embedVar)



#Moderation  

@bot.command(pass_context=True, brief="Mute Command", description="This command mutes a specified user.\nSyntax: #mute (user / ID) (time) (unit)\nNote: Specifying the time and unit is optional.")
@commands.has_any_role(mod_one, mod_two, mod_three)
async def mute(ctx, user: discord.Member, duration = 0,*, unit = None):
    try:
        role = 'muted'
        global mute_process
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
        await ctx.send(f'{user} has been muted')
        if unit == "s":
            mute_process = "MUTE_" + str(user) + "_" + str(duration) + "s"
            operations_list.append(mute_process)
            wait = 1 * int(duration)
            await asyncio.sleep(wait)
            operations_list.remove(mute_process)
            await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
            await ctx.send(f"{user} has been unmuted")

        elif unit == "m":
            mute_process = "MUTE_" + str(user) + "_" + str(duration) + "m"
            operations_list.append(mute_process)
            wait = 60 * int(duration)
            await asyncio.sleep(wait)
            operations_list.remove(mute_process)
            await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
            await ctx.send(f"{user} has been unmuted")
    except Exception as e:
        embedVar = discord.Embed(title="Error;", color=0x2C5ED1)
        embedVar.add_field(name="** **", value=str(e), inline=False)
        embed = await ctx.send(embed=embedVar)

        



@bot.command(pass_context=True, brief="Unmute Command", description="This command unmutes a specified user.\nSyntax: unmute (user / ID)")
@commands.has_any_role(mod_one, mod_two, mod_three)
async def unmute(ctx, user: discord.Member):
    try:
        role = 'muted'
        await user.remove_roles(discord.utils.get(user.guild.roles, name=role))
        await ctx.send(f'{user} has been unmuted')
        operations_list.remove(mute_process)
    except Exception as e:
        embedVar = discord.Embed(title="Error;", color=0x2C5ED1)
        embedVar.add_field(name="** **", value=str(e), inline=False)
        embed = await ctx.send(embed=embedVar)



@bot.command(pass_context=True, brief="Kick Command", description="This command kicks a specified user.\nSyntax: kick (user / ID)")
@commands.has_any_role(mod_one, mod_two, mod_three)
async def kick(ctx, user: discord.Member):
    try:
        await ctx.guild.kick(user)
        await ctx.send(f"{user} has been kicked from the server")
    except Exception as e:
        embedVar = discord.Embed(title="Error;", color=0x2C5ED1)
        embedVar.add_field(name="** **", value=str(e), inline=False)
        embed = await ctx.send(embed=embedVar)



@bot.command(pass_context=True, brief="Ban Command", description="This command permanently bans a specified user.\nSyntax: ban (user / ID)")
@commands.has_any_role(mod_one, mod_two, mod_three)
async def ban(ctx, user: discord.Member):
    try:
        await ctx.guild.ban(user)
        await ctx.send(f"{user} has been banned from the server")
    except Exception as e:
        embedVar = discord.Embed(title="Error;", color=0x2C5ED1)
        embedVar.add_field(name="** **", value=str(e), inline=False)
        embed = await ctx.send(embed=embedVar)





@bot.command(pass_context=True, brief="Unban Command", description="This command unbans a specified user.\nSyntax: unban (user / ID)")
@commands.has_any_role(mod_one, mod_two, mod_three)
async def unban(ctx, id: int):
    try:
        user = await bot.fetch_user(id)
        await ctx.guild.unban(user)
        await ctx.send(f"{user} has been unbanned from the server")
    except Exception as e:
        embedVar = discord.Embed(title="Error;", color=0x2C5ED1)
        embedVar.add_field(name="** **", value=str(e), inline=False)
        embed = await ctx.send(embed=embedVar)


@bot.command(brief="Purge Command", description="This command purges a specified number of messages (if no arguments are given, it'll purge as many messages as it can)\nSyntax: purge (number of messages)")
@commands.has_any_role(mod_one, mod_two, mod_three)
async def purge(ctx, amount: int):
    try:
        amount = amount+1
        deleted = await ctx.channel.purge(limit=amount)
    except Exception as e:
        embedVar = discord.Embed(title="Error;", color=0x2C5ED1)
        embedVar.add_field(name="** **", value=str(e), inline=False)
        embed = await ctx.send(embed=embedVar)






@bot.command(brief="Restart Command", description="This command restarts the bot.")
@commands.has_any_role(mod_one, mod_two, mod_three)
async def restart(ctx):
    try:
        print("Proper Nerd is restarting due to restart request")
        await ctx.send("Restarting, this may take a while")
        channel = bot.get_channel(botlog)
        await channel.send("Restarting, this may take a while")
        await bot.close()
    except Exception as e:
        embedVar = discord.Embed(title="Error;", color=0x2C5ED1)
        embedVar.add_field(name="** **", value=str(e), inline=False)
        embed = await ctx.send(embed=embedVar)




# Configuration

config_list = "**config** - list of configuration commands\n**config_perm_on_member_join** - can be set to True or False, decides whether a message gets sent everytime someone joins the server or not\n**config_content_on_member_join** - if you've set the on_member_join perm to True and want a message to get sent everytime someone joins the server, use this command to set the message"


@bot.command(brief="Shows a list of configuration commands", description="Shows a list of configuration commands\nAliases: settings", aliases=["settings"])
@commands.has_any_role(mod_one, mod_two, mod_three)
async def config(ctx):
    await ctx.send("**Configuration Commands:**\n" + config_list)


@bot.command(brief="Set whether you want the bot to send a message whenever someone joins the server", description="Set whether you want the bot to send a message whenever someone joins the server\nSyntax: config_perm_on_member_join (True/False)")
@commands.has_any_role(mod_one, mod_two, mod_three)
async def config_perm_on_member_join(ctx, argument: str):
    try:
        if argument == "True" or argument == "False":
            await change_db("perm_on_member_join", argument)
            await ctx.send(":white_check_mark:")
        else:
            await ctx.send("Invalid syntax, `argument` must be either True or False")
    except Exception as e:
        embedVar = discord.Embed(title="Error;", color=0x2C5ED1)
        embedVar.add_field(name="** **", value=str(e), inline=False)
        embed = await ctx.send(embed=embedVar)




@bot.command(brief="Set a message to send whenever someone joins the server", description="Set a message to send whenever someone joins the server\nSyntax: config_content_on_member_join \"(message)\" ")
@commands.has_any_role(mod_one, mod_two, mod_three)
async def config_content_on_member_join(ctx, argument: str):
    try:
        await change_db("on_member_join_content", argument)
        await ctx.send(":white_check_mark:")
    except Exception as e:
        embedVar = discord.Embed(title="Error;", color=0x2C5ED1)
        embedVar.add_field(name="** **", value=str(e), inline=False)
        embed = await ctx.send(embed=embedVar)














# Developer Commands

@bot.command()
@commands.has_role("Dev_Azrael")
async def edit_db(ctx, ch, new):
    try:
        ch = str(ch)
        new = str(new)
        await change_db(ch, new)
        await ctx.send(":white_check_mark:")
    except Exception as e:
        await ctx.send(str(e))


@bot.command()
@commands.has_role("Dev_Azrael")
async def view_db(ctx, ch):
    try:
        ch = str(ch)
        value = await check_db(ch)
        await ctx.send(str(value))
    except Exception as e:
        await ctx.send(str(e))


@bot.command()
@commands.has_role("Dev_Azrael")
async def send_db(ctx, ch_arg, new):
    try:
        ch = bot.get_channel(int(ch_arg))
        new = str(new)
        await ch.send(new)
        await ctx.send(":white_check_mark:")
    except Exception as e:
        await ctx.send(str(e))













      




bot.run(TOKEN)
