'''
This program should serve as the chat bot for Twitch.
This will share a commands.csv with the Discord bot.
This should have CRUD operations for the commands.csv
'''

import pandas as pd
from dotenv import load_dotenv
from twitchio.ext import commands


def main():
  load_dotenv()
  token = os.getenv('TWITCH_OAUTH_TOKEN')
  pass

if __name__ == '__main__':
  main()