'''
This program should serve as the chat bot for Twitch.
This will share a commands.csv with the Discord bot.
This should have CRUD operations for the commands.csv
'''

import os
import pandas as pd
from dotenv import load_dotenv
from twitchio.ext import commands

load_dotenv()
twitchtoken = os.getenv('TWITCH_OAUTH_TOKEN')

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=twitchtoken, client_id='client_id', nick='nick', prefix='!',
                         initial_channels=['absenth762'])

    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        print(message.content)
        await self.handle_commands(message)

    @commands.command(name='hello')
    async def my_command(self, ctx):
        await ctx.send(f'Hello {ctx.author.name}!')

bot = Bot()
bot.run()
