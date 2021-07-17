import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open("setting.json",mode="r",encoding='utf8') as jfile:
	jdata = json.load(jfile)

class React(Cog_Extension):

    @commands.command()
    async def pic(self,ctx):
	    await ctx.send(SelectUrl(random.choice(jdata['PicSource'])))

    @commands.command()
    async def san(self,ctx):
	    await ctx.send(SelectUrl('sankaku'))

    @commands.command()
    async def yan(self,ctx):
	    await ctx.send(SelectUrl('yande'))

    @commands.command()
    async def gel(self,ctx):
	    await ctx.send(SelectUrl('gelbooru'))

    @commands.command()
    async def dan(self,ctx):
	    await ctx.send(SelectUrl('danbooru'))
    
    @commands.command()
    async def konruru(self,ctx):
	    await ctx.send('空嚕嚕')

    @commands.command()
    async def set_time(self,ctx,time):
      with open('setting.json','r',encoding='utf8') as jfile:
        jdata = json.load(jfile)
      jdata['time'] = time
      with open("setting.json",mode="w",encoding='utf8') as jfile:
	      json.dump(jdata,jfile,indent=4)
      await ctx.send(f'Set Time {time}')
    


def SelectUrl(source):
    max = source + "_max"
    return jdata[source] + str(random.randint(1,int(jdata[max])))

def setup(bot):
    bot.add_cog(React(bot))