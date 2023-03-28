'''
This program should serve as the chat bot for Discord.
This will share a commands.csv with the Twitch bot.
This should have CRUD operations for the commands.csv
'''

import discord
import os
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
discordtoken = os.getenv('DISCORD_TOKEN')


class DiscordClient(discord.Client):
    async def on_ready(self):
        print(f'Discord Ready |  {self.user}')
        print('The Discord Bot is Online')

    async def on_message(self, message):
        # Don't respond to ourselves, that's dumb.
        if message.author == self.user:
            return

    def list_commands(self):
        # Open commands.csv and create a command for each command and response
        commands_list = []
        if os.path.isfile("commands.csv"):
            with open("commands.csv", "r") as f:
                for line in f:
                    commands_list.append(line)


intents = discord.Intents.default()
intents.message_content = True
client = DiscordClient(intents=intents)
client.run(discordtoken)
