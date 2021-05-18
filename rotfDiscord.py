import discord
from discord.ext import commands
import RotfWrapper as RW
import os
from dotenv import load_dotenv


load_dotenv()
# Load important stuff from .env DO NOT HACK MY KINDLE FIRE.
DISCORD_TOKEN = os.getenv("TOKEN")
client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print("Ready")


'''
Lookup by player name
'''


@client.command()
async def lookup(ctx, name: str):

    account = RW.get_account(str.capitalize(name))

    if type(account) == str:
        await ctx.send(account)
    else:
        embed = discord.Embed(
            title=account['playerName'] + "\nRating: " + str(account['rating']),
            description="Account Fame: " + str(account['playerFame']),
            colour=discord.Colour.blue()
        )

        embed.set_footer(text='Squiddy WIP')
        embed.set_author(name="Account Lookup")
        for char in account['playerCharacters']:
            embed.add_field(name="Class: " + str(char['class']) + "| Stats: " + char['stats']['statsMaxed'] +
                                 "| Fame: " + str(char['fame']),
                            value="Equipped" + str(
                                char['items']['equipped']) + "\n" + "Inventory" + str(char['items']['inventory']),
                            inline=False)

        await ctx.send(embed=embed)


@client.command()
async def rate(ctx, name, rating):
    response = RW.update_rating(name, int(rating))
    if response == "Character Undiscovered":
        await ctx.send(response)
    else:
        await ctx.send(response)


client.run(DISCORD_TOKEN)
