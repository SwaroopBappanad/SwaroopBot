import discord
import datetime
import pytz
import os
from flask import Flask
import time

saidphrases = ['']

nono_words = ['fuck', 'bitch', 'shit', 'ass', 'damn']

client = discord.Client()
moderationLevel = 0
loserMode = True

spam = False
blacklist = ['mhm']

def convert(lst):
  return ' '.join(lst).split()

@client.event
async def on_message(message):
   message.content = message.content.lower()
   global moderationLevel
   global loserMode
   global spam
   global blacklist
   if ('<blacklist>' in str(message.content)):
     blacklist.append(str(message.content[12:]))

   if ('<whitelist>' in str(message.content)):
     for i in range(len(blacklist)):
       if (blacklist[i] == str(message.content[12:])):
         del blacklist[i]
         await message.channel.send(f'Succesfully whitelisted the word {str(message.content[12:])}')
   newChar = ''
   lst = [str(message.content)]
   words = convert(lst)
   for word in words:
     if word in blacklist:
       await message.channel.purge(limit=1)
       await message.channel.send("BAD BOI, NO BLACKLISTED WORDS")
     elif word in nono_words:
       await message.channel.purge(limit=1)
       await message.channel.send("No bad words! Language you hippie!") 
   for char in str(message.content):
     if char == ' ':
       pass
     else:
       newChar += char
   
  #Make sure the hippies don't decieve the bot
   for i in range(len(nono_words)):
     if nono_words[i] in newChar:
       await message.channel.purge(limit=1)
       await message.channel.send("AAAAH, thought u could decieve me did ya hippie?!")

   if '!purge' in str(message.content):
      await message.channel.purge(limit=int(message.content[6:])+1)
      await message.channel.send(f'succesfull purged{message.content[6:]} messages')
   if 'spam on' in str(message.content) and message.author != 'lolipop#8556':
     spam = True
     spamWord = message.content[8:]
   if str(message.content) == 'spam off':
     spam = False
   while spam:
    await message.channel.send(spamWord+'\n'+spamWord+'\n'+spamWord+'\n'+spamWord+'\n'+spamWord+'\n'+spamWord+'\n'+spamWord+'\n'+spamWord+'\n'+spamWord+'\n'+spamWord+'\n'+spamWord+'\n'+spamWord+'\n'+spamWord+'\n'+spamWord+'\n'+spamWord+'\n'+spamWord+'\n'+spamWord+'\n'+spamWord+'\n'+spamWord+'\n'+spamWord+'\n')


  #all current disabled features
   '''if (message.author == client.user) and loserMode:
      await message.add_reaction('\N{THUMBS UP SIGN}')
      pass
   elif (message.author != client.user and loserMode):
      await message.channel.send('no loser')

   if (str(message.content) == 'losermode on'):
      loserMode = True
      await message.channel.send("WHATS UP ASSHOLE")
   elif (str(message.content) == 'losermode off'):
      loserMode = False
      await message.channel.send("Sorry for being an asshole")

   if (loserMode == False):'''
'''   if ('modlevel' in str(message.content)):
       moderationLevel = int(message.content[9])
       print(moderationLevel)
       await message.channel.send(f"succesfully set moderation level to {message.content[9]}.")
   if message.content.startswith('!hello'):
          embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
          embedVar.add_field(name="Field1", value="hi", inline=False)
          embedVar.add_field(name="Field2", value="hi2", inline=False)
          await message.channel.send(embed=embedVar)
   if '卐' in str(message.content) or '㊦' in str(message.content):
       await message.channel.purge(limit=1)
       await message.channel.send("bad boi quinoa")
       t1 = time.time()
       m = message.content
       t2 = time.time()
   if (m in saidphrases) and moderationLevel == 1:
        await message.channel.purge(limit=1)
   elif (m not in saidphrases) and moderationLevel == 1:
         saidphrases[0] = m
    
   if t2 - t1 < 1 and moderationLevel >= 2:
   
       await message.channel.purge(limit=1)   
    
'''



    

     

client.run(os.environ.get('DISCORD_TOKEN'))





    
