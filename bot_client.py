'''
NW Community Bot
A Discord bot for managing New World community information e.g. crafting station progress, available crafters, and more. 

botclient.py
Events and functions for the discord.py client.
'''

import logging
import discord
import api_keys


logger = logging.getLogger(__name__)

client = discord.Client()

def startup():
  token = api_keys.get_key('discord_token')
  client.run(token)