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
        self.load_commands()

    def load_commands(self):
        with open('commands.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                command_name = row['Commands']
                command_output = row['Output']
                command_func = self.make_command_func(command_output)
                self.add_command(command_name, command_func)

    def make_command_func(self, output):
        async def command_func(self, ctx):
            message = output.replace('{message.channel}', ctx.channel.name)
            message = message.replace('{message.text_args[0]}', ctx.content.split()[1])
            await ctx.send(message)
        return command_func

bot = Bot()
bot.run()
