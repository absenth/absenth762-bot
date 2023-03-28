'''
This program should serve as the chat bot for Twitch.
This will share a commands.csv with the Discord bot.
This should have CRUD operations for the commands.csv
'''

import csv
import os
from dotenv import load_dotenv
from twitchio.ext import commands

load_dotenv()
twitchtoken = os.getenv('TWITCH_OAUTH_TOKEN')


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=twitchtoken, client_id='client_id', nick='nick',
                         prefix='!', initial_channels=['absenth762'])

    async def event_ready(self):
        print(f'Twitch Ready | {self.nick}')
        print('The Twitch Bot is Online')
        self.load_commands()  # load commands from the CSV file when the bot is ready

    def load_commands(self):
        # Open commands.csv and create a command for each command and response
        if os.path.isfile("commands.csv"):
            with open("commands.csv", "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.commands[row['Commands']] = row['Output']
                    setattr(self, row['Commands'].lstrip('!'), self.handle_command)
                    print(f"Added command {row['Commands']} with output {row['Output']}")

    async def handle_command(self, message):
        # Check if the message is a command and if it is, send the appropriate response
        if message.content in self.commands:
            response = self.commands[message.content].format(message=message)
            await message.channel.send(response)


bot = Bot()
bot.run()