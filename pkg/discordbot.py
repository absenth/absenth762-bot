'''
This program should serve as the chat bot for Discord.
This will share a commands.csv with the Twitch bot.
This should have CRUD operations for the commands.csv
'''

import discord
import os
import pandas as pd
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
discordtoken = os.getenv('DISCORD_TOKEN')

class DiscordClient(discord.Client):
  async def on_ready(self):
    print(f'Discord Ready |  {self.user}')
    print(f'The Discord Bot is Online')

  async def on_message(self, message):
    # Don't respond to ourselves, that's dumb.
    if message.author == self.user:
      return


intents = discord.Intents.default()
intents.message_content = True
client = DiscordClient(intents=intents)
client.run(discordtoken)
