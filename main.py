'''
NW Community Bot
A Discord bot for managing New World community information e.g. crafting station progress, available crafters, and more. 

main.py
'''

import logging
import bot_client


def main():
  log_filename =('nw-community-bot-' + 
                 datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + 
                 '.log')
  logging.basicConfig(
    filename=log_filename, 
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

  logging.info('Starting bot client.')
  bot_client.startup()

if __name__ == '__main__':
  main()