#!/bin/env python3
# Written by lowborn#0101, April 2022
# For deployment on https://api.yourbotis.live
import asyncio
import logging
import os
import random

import discord

from constants import conjunctions, message_templates, words

logger = logging.getLogger('MyClient')
logger.setLevel(logging.INFO)

# Stdout is piped directly to the yourbot web console.
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
default_handler = logging.StreamHandler()
default_handler.setFormatter(formatter)

logger.addHandler(default_handler)

class EldenRingMessagesBotClient(discord.Client):

    async def on_ready(self):
        logger.info('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author.id != self.user.id:
            lowered_message = message.content.lower()

            if any(
                command in lowered_message
                for command in ['?finger']
            ):
                conjunction = random.choice([False, *conjunctions])
                loop_count = 2 if conjunction else 1
                constructed_message = ""

                for index in range(loop_count):
                    template = random.choice(message_templates)
                    word = random.choice(words)
                    # logger.info(f'Template: {template}')
                    # logger.info(f'Word: {word}')
                    constructed_message += template.format(word)
                    if conjunction and index == 0:
                        constructed_message += random.choice(conjunctions)

                await message.reply(constructed_message)

client = EldenRingMessagesBotClient() 
asyncio.create_task(client.start(os.environ['DISCORD_TOKEN']))
