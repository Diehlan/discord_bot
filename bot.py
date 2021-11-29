import random
import discord
#import youtube_dl
import json
import os.path

from discord.ext import commands
import os
from asyncio import sleep

intents = discord.Intents().default()
intents.members = True

steve = commands.Bot(command_prefix = "?", intents=intents)



@steve.event
async def on_ready():
    print("Steve online and ready.")
    while True:
        await steve.change_presence(activity = discord.Game(name = "Message Diehlan if I die"))
        await sleep(5)
        await steve.change_presence(activity = discord.Activity(type=discord.ActivityType.watching, name="?list_commands for help"))
        await sleep(5)
        if False:
            break

#role on join
@steve.event
async def on_member_join(member:discord.Member):
    server = steve.get_guild(423678025377382410) #server id
    channel = steve.get_channel(907070265849180190) #channel id
    role = server.get_role(423681511800438785) #role id
    await member.add_roles(role)
    await channel.send(f"Welcome to your doom {member}")

#ping    
@steve.command()
async def ping(ctx):
   await ctx.send(f"My ping is {round(steve.latency * 1000)} ms")

#bully
@steve.command()
async def bully(ctx):
    threat = ["FUCK ", "Congratulations. It's time to call mom and dad. Tell them that the second mortgage that they pulled out for your degree was worthless because you're now a weeb with nothing going for them. Now, if you want to be standing where I'm standing anytime in your pathetic future, you had better listen very fucking carefully to the next 115 words that I say because this is your new reality. When you log onto that computer each and every day, YOUR ASS IS MINE. There will be no cell phone use; there will be no smoke breaks; there will be no motherfucking shits taken unless authorized by me personally. And IF you happen to be lucky enough to get that authorization, you will have exactly 4 minutes and 30 seconds to expel your fecal material, wipe your ass, wash your filthy hands and get back to your computer. And if I happen to come across a shit smear in that toilet bowl, I will personally go to your home and shit in places that will leave you confused for the rest of your pathetic life ", \
              "What the fuck did you just fucking say about me, you fucking noob? I'll have you know I am in the top 0.1% of crucible KDA, I've completed nearly 1000 flawless cards, and I have over 300k confirmed PVP kills. I am also highly skilled in PVE and am at the top of the leaderboard of GM nightfall completions with a max triump score. You are nothing to me but just another blueberry. I will wipe you and your fireteam the fuck out with precision the likes of which has never been seen before by Saint-14, Lord Saladin and Lord Shaxx. I swear on the fucking traveler, mark my fucking words. You think you and your ghost can get away with saying that shit to me in DMs? Think again, scrub. As we speak I am contacting my secret network of vanguard spies across the universe and your IP is being traced right now so you better prepare for the DDOS storm, shitter. The storm that wipes out the pathetic little thing you call your life (and your router). You're fucking dead, guardian. I can teleport anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my melee attack. Not only am I extensively trained in the crucible, but I have access to the entire arsenal of raid weapons and exotics that you'll never own, and I will use them to their full extent to wipe your miserable ass off the face of the Destiny universe, kinderguardian. If only you could have known what unholy retribution your little 'clever' comment was about to bring down upon you, maybe you would have kept your fucking ghost quiet. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit light and darkness powers all over you and you will drown in it. You're fucking dead "]
    subjects = ["<@372887053245087756>", "<@314702634558685184>", "<@201184624070754304>", "<@338092541113139201>",\
        "<@214481816684462080>", "<@196104209332961280>", "<@179726534477742090>", "<@417202993499209749>",\
            "<@205464885797060608>", "<@202145262683029514>", "<@276216143998615552>", "<@122183498541826050>"]
    await ctx.send(random.choice(threat) + random.choice(subjects))
    
#pick rock
@steve.command()
async def rock(ctx):
    options = ["Rock", "Paper", "Scissors"]

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    steve_pick = options[random_number]
    
    await ctx.send(steve_pick)

    if steve_pick == "Rock":
        await ctx.send(f"Huh, it looks like we tied.")
    elif steve_pick == "Paper":
        await ctx.send(f"Nice try, but I won that one.")  
    elif steve_pick == "Scissors":
        await ctx.send(f"Aw, you beat me. I'll get you next time.")

#pick paper
@steve.command()
async def paper(ctx):
    options = ["Rock", "Paper", "Scissors"]

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    steve_pick = options[random_number]
    
    await ctx.send(steve_pick)

    if steve_pick == "Paper":
        await ctx.send(f"Huh, it looks like we tied.")
    elif steve_pick == "Scissors":
        await ctx.send(f"Nice try, but I won that one.")
    elif steve_pick == "Rock":
        await ctx.send(f"Aw, you beat me. I'll get you next time.")
        
#pick scissors
@steve.command()
async def scissors(ctx):
    options = ["Rock", "Paper", "Scissors"]

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    steve_pick = options[random_number]
    
    await ctx.send(steve_pick)
    
    if steve_pick == "Scissors":
        await ctx.send(f"Huh, it looks like we tied.")
    elif steve_pick == "Rock":
        await ctx.send(f"Nice try, but I won that one.")
    elif steve_pick == "Paper":
        await ctx.send(f"Aw, you beat me. I'll get you next time.")

#dice roll        
@steve.command()
async def dice(ctx):
    roll = random.randint(0, 6)
    roll2 = random.randint(0,6)
    await ctx.send(f"{roll} , {roll2}")

        
 
#join
@steve.command() 
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel")
        return
    
    else:
        channel = ctx.message.author.voice.channel
        
    await channel.connect()

  
#music
# @steve.command()
# async def play(ctx, url : str):
#     song_there = os.path.isfile("song.mp3")
#     try:
#         if song_there:
#             os.remove("song.mp3")
#     except PermissionError:
#         await ctx.send("Wait for the music to stop playing or use the '?stop' command")
#         return
    
#     voiceChannel = discord.utils.get(ctx.guild.voice_channels, name="General")
#     channel = ctx.message.author.voice.channel
#     await channel.connect()
#     voice = discord.utils.get(steve.voice_clients, guild=ctx.guild)
   
        
#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'prefferedquality': '192',
#         }],
#     }
#     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         ydl.download(url)
#     for file in os.listdir("./"):
#         if file.endswith(".mp3"):
#             os.rename(file, "song.mp3")                        
#     voice.play(discord.FFmpegPCMAudio("song.mp3"))                     
   
#leave
@steve.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@steve.command()
async def purple(ctx):
    await ctx.send(f"She's a one eyed, one horned, flying purple people eater")
    
#commands list
@steve.command()
async def list_commands(ctx):
    help_list = ["?rock // Play rock, paper, scissors with me and choose rock",
        "?paper // Play rock, paper, scissors with me and choose paper",
        "?scissors // Play rock, paper, scissors with me and choose scissors",
        "?ping // This lets you know what my ping is",
        "?bully // This bullies someone from the server at random",
        "?dice // This rolls a pair of 6 sided dice",
        "?join // This pulls me into whatever voice channel the user is connected to",
        "?leave // This disconnects from the voice channel",
        "?purple // Fuck around and find out"]
    await ctx.send("\n".join(help_list))
    
def startup_check():
    if os.path.exists("credentials.json"):
        f = open('credentials.json')
        data = json.load(f)
        print("Successfully found credentials.")
        return data["discord_token"]
    else:
        print("Credentials do not exist.")
        return input("What are your credentials? ")

TOKEN = startup_check()
print("Starting bot")
steve.run(TOKEN)
