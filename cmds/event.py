import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open("setting.json",mode="r",encoding='utf8') as jfile:
	jdata = json.load(jfile)

class Event(Cog_Extension):

    @commands.Cog.listener()
    async def on_member_join(self,member):
	    print(f'{member} join')
	    channel = self.bot.get_all_channels(int(jdata['Channel']))
	    await channel.send(f"{member} join,こんるる～")

    @commands.Cog.listener()
    async def on_member_remove(self,member):
	    print(f'{member} leave')
	    channel = self.ot.get_all_channels(int(jdata['Channel']))
	    await channel.send(f"{member} leave,おつるる～")

    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.author != self.bot.user :
            print(f"{msg.content}")
            if msg.content == '野' :
	            await msg.channel.send('格')
            elif msg.content == '格' :
	            await msg.channel.send('炸')
            elif msg.content == '炸' :
	            await msg.channel.send('彈')
            elif msg.content == "<:RU1:628607335434027039>" :
	            await msg.channel.send('<:Konruru:860021875312295967>')
            elif msg.content == "<@!717385251902718053>" :
	            await msg.channel.send('<:Konruru:860021875312295967>')
              



def setup(bot):
     bot.add_cog(Event(bot))