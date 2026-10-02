import discord
from discord.ext import commands
import os
import random
import requests

img_nome = ""

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')  


@bot.command()
async def meme(ctx):
    numero = random.randint(1, 100)
    if numero <= 70:
        img_nome = 'enem_2.png'
        await ctx.send('Meme comum!')
    elif numero <= 95:
        img_nome = 'mem1.jpg'
        await ctx.send('Meme incomum!')
    else:
        img_nome = 'mem2.png'
        await ctx.send('Meme raro!')
    with open(f'images/{img_nome}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Uma vez que chamamos o comando duck, o programa chama a função get_duck_image_url '''
    image_url = get_duck_image_url()
    await ctx.send(image_url)



bot.run('')
