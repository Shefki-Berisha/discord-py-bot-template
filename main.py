import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!") #command_prefix's value can be channged to whatever value you want

@bot.event
async def on_ready():
    print("Ready!") #make the bot print "Ready!" in the console when the bot is ready

#bot commands
@bot.command()
async def command(ctx):
    await ctx.send("this is a command") #the bot will send this when the command is used in discord
@bot.command()
async def command2(ctx):
    await ctx.send("this is the 2nd command")
@bot.command()
async def command3(ctx):
    await ctx.send("this is the 3rd command")
#you can make as many commands as you want, these are just examples

bot.run("PLACE YOUR BOT TOKEN HERE")
# to get your bot token, go to discord.dev and sign in if you havent already, go to applications and click on your bot, go to "Bot" and click "Reset Token" and copy the bot token
