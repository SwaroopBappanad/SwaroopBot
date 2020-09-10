import discord
import time
from flask import Flask


client = discord.Client()
prefix = "&"

@client.event
async def on_message(message):
  message.content.lower()
  if message.author == client.user:
    return
  if message.content.startswith(prefix+"timer "):
    m = str(message.content)
    me = m[7:]
    await message.channel.send(time.strftime('%I %M %p', time.localtime()))
    timer = int(me)
    await message.channel.send(timer)
    t1 = time.time()
    await message.channel.send("What should I automate?")
    await message.channel.send()
    

client.run('NzUzMzg0OTkwMDc0NDcwNTgy.X1lacg.Fnxs96WghFuzxOvFNsL_pA5fuF8')
#https://docs.python.org/3/library/time.html#time.localtime

