import discord
from discord.ext import commands
import os, random
import json
from dotenv import load_dotenv

# .env dosyasını yükleyin
load_dotenv()

# Bot intents (izinler) ayarları
intents = discord.Intents.default()
intents.message_content = True  # Mesaj içeriği izni

bot = commands.Bot(command_prefix='!', intents=intents)


def load_memes():
    with open('memes.json', 'r') as f:
        return json.load(f)


@bot.command()
async def mem(ctx, category: str = None):

    memes = load_memes()

    if not category:
        category = random.choice(list(memes.keys()))

    if category not in memes:
        await ctx.send(f"Sorry, no memes found for the category: {category}")
        return

    meme_list = memes[category]


    weights = [meme['rarity'] for meme in meme_list]
    

    selected_meme = random.choices(meme_list, weights=weights, k=1)[0]
    
  
    with open(f"images/{selected_meme['file']}", 'rb') as f:
        picture = discord.File(f)
    
    await ctx.send(file=picture)

# Botunuzu çalıştırın
bot.run(os.getenv('MTMwMTk5NDAzMjI0NzA3ODk0Mw.GpxGzQ.KssGZLu37C4sMi5KyiXMl6qDRyH4iuiEsh1dQs'))
