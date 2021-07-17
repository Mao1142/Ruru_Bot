import discord
from discord.ext import commands
import os
import keep_alive
import json

with open("setting.json",mode="r",encoding='utf8') as jfile:
	jdata = json.load(jfile)

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
	print("---Bot is online---")




@bot.command()
async def load(ctx,extension): #load function
	bot.load_extension(f'cmds.{extension}')
	await ctx.send(f'Loaded {extension} done.')

@bot.command()
async def unload(ctx,extension): #unload function
	bot.unload_extension(f'cmds.{extension}')
	await ctx.send(f'Unloaded {extension} done.')

@bot.command()
async def reload(ctx,extension): #reload function
	bot.reload_extension(f'cmds.{extension}')
	await ctx.send(f'Reloaded {extension} done.')

for Filename in os.listdir('./cmds'):
	if Filename.endswith('.py'):
 		bot.load_extension(f'cmds.{Filename[:-3]}')

if  __name__ == "__main__":
  keep_alive.keep_alive()
  bot.run( jdata[ 'TOKEN' ] )








