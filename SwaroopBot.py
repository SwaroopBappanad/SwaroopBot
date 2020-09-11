import discord
import datetime
import pytz
import os
from flask import Flask

auto = "auto"
help = "SB"

client = discord.Client()

datetime.timezone(datetime.timedelta(hours=-4), 'EST')
prefix = "$" 
@client.event
 
async def on_message(message):
  global prefix
  message.content.lower()
  if message.author == client.user:
    return
  if str(message.content) == help + " help":
    await message.channel.send("The prefix is:"+prefix)
  if message.content.startswith(prefix+"change "):
    newPrefix = str(message.content[7:])
    prefix = newPrefix
    await message.channel.send("Successfully changed prefix!")

  if message.content.startswith(prefix+"timer "):
    m = str(message.content)
    me = m[7:]
    await message.channel.send(datetime.datetime.now(pytz.timezone("EST")))
    timer = int(me)
    await message.channel.send(timer)
    await message.channel.send("What should I automate?")
    global itsAutomationTimeBaby 
    itsAutomationTimeBaby = True
  if auto in message.content and itsAutomationTimeBaby:
    m = str(message.content)


token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
#https://docs.python.org/3/library/time.html#time.localtime

