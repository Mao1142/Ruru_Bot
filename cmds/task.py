import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json,asyncio,datetime
import random 

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)


class Task(Cog_Extension):
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
    
    self.counter = 0
    async def interval():
      await self.bot.wait_until_ready()
      with open('setting.json','r',encoding='utf8') as jfile:
          jdata = json.load(jfile)
      self.channel = self.bot.get_channel(int(jdata['Channel']))
      while not self.bot.is_closed():
        now_time = datetime.datetime.now().strftime('%H%M')
        #print(now_time)
        if now_time == '0100' and self.counter == 0:
          #await self.channel.send(SelectUrl(random.choice(jdata['PicSource'])))
          await self.channel.send(f'こんるる～')
          self.counter = 1
        elif now_time == '1400' and self.counter == 0:
          await self.channel.send(f'おつるる～')
          self.counter = 1
        else :
          self.counter = 0       
        await asyncio.sleep(35)

    self.bg_task = self.bot.loop.create_task(interval())    


@commands.command()
async def set_channel(self,ctx,ch:int):
  self.Channel = self.bot.get_channel(ch)
  await ctx.send(f'Set Channel : {self.channel.mention}')


def setup(bot):
  bot.add_cog(Task(bot))

def SelectUrl(source):
    max = source + "_max"
    return jdata[source] + str(random.randint(1,int(jdata[max])))