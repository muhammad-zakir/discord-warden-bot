# This example requires the 'message_content' privileged intent to function.

import discord
import os

from dotenv import load_dotenv


class MyClient(discord.Client):

    async def on_ready(self):
        await self.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name="his own existential crisis"))
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hi'):
            reply_message = """Hi Hooman, I'm Warden the Bot. I'm here trying to help everyone in this Server.
            You can try to ask myhelp with using '!' prefix before entering the command that you wishes to use.
            Here's the list of my currently available commands:
            - hello
            - realmcode
            - realmlink
            - sup"""
            await message.reply(reply_message, mention_author=True)

        if message.content.startswith('!hello'):
            await message.reply('Hello, Hooman!', mention_author=True)

        if message.content.startswith('!realmcode'):
            await message.reply('Hi Hooman!, here\'s the Realm\'s code: `DSMDAoMYdkw`', mention_author=True)

        if message.content.startswith('!realmlink'):
            await message.reply('Hi Hooman!, here\'s the Realm\'s link: https://realms.gg/DSMDAoMYdkw',
                                mention_author=True)

        if message.content.startswith('!sup'):
            await message.reply('Did you just tried chit - chatting with a bot? Are you that bored hooman?',
                                mention_author=True)


intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
token = os.getenv('DISCORD_BOT_TOKEN')

client = MyClient(intents=intents)
client.run(token)
