'''
This program should serve as the chat bot for Twitch.
This will share a commands.csv with the Discord bot.
This should have CRUD operations for the commands.csv
'''

import csv
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
        print(f'Twitch Ready | {self.nick}')
        print(f'The Twitch Bot is Online')




bot = Bot()
bot.run()