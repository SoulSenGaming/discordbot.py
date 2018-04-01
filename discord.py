import profanity # learn more: https://python.org/pypi/profanity
import discord
from discord.ext import commands

Client = discord.Client() 
bot = commands.Bot("$")
token = "NDI3MTY2MzUwMjA5OTc0Mjc0.DZ71jQ.WhddOZNft2UoIEtj60t3PewPAcU"
chat_filter = ["bob", "timmy"]
bypass_list = []

@bot.event
async def on_ready():
    bot.remove_command("help")
    await bot.change_status(game=discord.Game(name='Sub & Like Botting Kryb'))
    print ("Kryb YT Bot Is Online And Connected To Hydration Gaming Discord")
    print ("-------------------------------------")
    print ("Author: SoulSen")
    print ("Youtuber: Kryb")
    print ("-------------------------------------")
    print ("Logged In As:")
    print ("Bot Name: {}".format(bot.user.name))
    print ("Bot ID: {}".format(bot.user.id))

@bot.command(pass_context=True)
async def kryb(ctx):
    await bot.say("**COUGH** **COUGH** You Should Go Subscribe To The **BEST** MC Youtuber Which is Kryb, Youtube Channel: https://www.youtube.com/channel/UCp6A5ZOs0ZKFmBsnZ-VZKBw")

@bot.command(pass_context=True)
async def Help(ctx):
    await bot.say("Help Is On The Way!")

@bot.command(pass_context=True)
async def kick(ctx, user:discord.Member):
    await bot.say("User: {}, Was Kicked!".format (user.name))
    await bot.kick(user)
    
@bot.command(pass_context=True)
async def ban(ctx, user:discord.Member):
    await bot.say ("User: {}, Was Banned!".format (user.name))
    await bot.ban(user)
    
@bot.command(pass_context=True)
async def mute(ctx, user:discord.Member):
    await bot.say ("User: {}, Was Muted!".format (user.name))
    
@bot.event
async def on_message(message):
    await bot.delete_message(message)
    await bot.say(":octagonal_sign: **HEY!** NO SWEARING, THIS IS A :pray:***CHRISTIAN DISCORD SERVER :pray:!*** :octagonal_sign:")
       
bot.run(token)
