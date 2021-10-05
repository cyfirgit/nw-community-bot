'''
NW Community Bot
A Discord bot for managing New World community information e.g. crafting station progress, available crafters, and more. 

api_keys.py
Retrieve private keys.
'''

import os
import logging

logger = logging.getLogger(__name__)

key_file = 'api_keys.json'
key_path = os.getcwd() + '/' + key_file

def get_key(key_name):
  logger.info(f'Retrieving key {key_name} from {key_path}.')
  with open(key_path, 'r') as f:
    all_keys = json.load(f)
    key = all_keys[key_name]
  return key