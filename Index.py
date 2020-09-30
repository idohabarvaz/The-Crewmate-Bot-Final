#Among Us Bot
import discord
from discord.ext import commands
import json
import requests
import asyncio
import random
from discord.utils import get
from discord.utils import find
import datetime
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.environ["TOKEN"]

print(os.environ)
def get_prefix(bot, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]





def get_role(bot,message):
    with open("roles.json", 'r') as f:
        roles = json.load(f)
    return roles[str(message.guild.id)]



#איך הכל עושה קונפיג
# hidelobby - מתחיל כפולס כשהבוט נכנס לשרת
# prefixes - מתחיל כשאתה נכנס לשרת
# roles - עושים קונפיג על ידי הפקודה sethostrole
# voice - עושים קופניג על ידי הפקודה setvoicechannel



bot = commands.Bot(command_prefix=get_prefix,help_command = None)



#ctx.guild.default_role

@bot.command()
async def host(ctx, players: int, *, role:discord.Role=None):
    with open("voice.json", 'r') as f:
        data = json.load(f)


    with open("roles.json", 'r') as f:
        roles = json.load(f)


    with open("counter.json", 'r') as f:
        count = json.load(f)


    with open("audit.json", 'r') as f:
        log = json.load(f)

    








    muted = False
    locked = True
    guild = ctx.message.guild
    author = ctx.message.author
    host = ctx.message.author
    role_re = discord.utils.get(ctx.guild.roles, name=roles[str(ctx.guild.id)])
    print(roles[str(ctx.guild.id)])

        
    if players > 10:
        error3 = await ctx.send("There was a problem, please enter a number smaller than 11")
        await asyncio.sleep(10)
        await error3.delete()
    elif players < 4:
        error2 = await ctx.send("There was a problem, please enter a number larger than 3 and make sure you are in the required voice channel to start hosting!")
        await asyncio.sleep(10)
        await error2.delete()
    elif str(ctx.message.author.voice.channel.id) != data[str(guild.id)]:
        print(ctx.message.author.voice.channel.id)
        print(data[str(guild.id)])
        error = await ctx.send("Join The Required Voice Channel To Start Hosting!")
        await asyncio.sleep(10)
        await error.delete()

    elif role_re not in ctx.message.author.roles:
        await ctx.send("You Don't Have The Required Role To Start Hosting!")
    elif players < 11 and players > 3 and str(ctx.message.author.voice.channel.id) == data[str(ctx.guild.id)] and data[str(ctx.guild.id)] != None and role_re in ctx.message.author.roles:
        await ctx.send("Creating Lobby...")
        if role == None:
                

            category1 = await ctx.guild.create_category(f"Hosted By {ctx.message.author}")
            await asyncio.sleep(2)
            msg = await ctx.send(f"Creating Voice Channel For {players} Players.")
            vc = await guild.create_voice_channel(user_limit=players, name=f"Game {int(count[str(ctx.guild.id)]) + 1}", category=category1)
            txt = await guild.create_text_channel(name=f"Host Panel", category=category1)
            await txt.set_permissions(ctx.guild.default_role, send_messages=False, read_messages=False)
            await vc.set_permissions(ctx.guild.default_role, connect=True)
            await txt.set_permissions(ctx.message.author, send_messages=False, read_messages=True)
            await vc.set_permissions(ctx.message.author, mute_members=True, move_members=True)
            if str(ctx.guild.id) in log:
                datetime_object = datetime.datetime.now()
                channel = bot.get_channel(int(log[str(ctx.guild.id)]))

                logs=discord.Embed(title="Lobby Logs", color=0x1943c2)
                logs.set_author(name="Game Info")
                logs.add_field(name="Lobby Host:", value=f"{ctx.message.author}", inline=False)
                logs.add_field(name="Time Created:", value=f"{datetime_object}", inline=True)
                logs.add_field(name="Time Deleted:", value=f"N/A", inline=False)
                logs.add_field(name="Max Players Limit:", value=f"{players} Players", inline=True)
                logs.add_field(name="Lobby Name:", value=f"Game {int(count[str(ctx.guild.id)]) + 1}", inline=True)
                logs.set_footer(text="Created By <Dips#6999")
                logss1 = await channel.send(embed=logs)
                #something



            count[str(ctx.guild.id)] = count[str(ctx.guild.id)] + 1

            with open("counter.json", 'w') as f:
                json.dump(count, f, indent=4)






            await msg.edit(content=f'Lobby Created, Hosted By {ctx.message.author.mention}. Access Your {txt.mention} Here')
        elif role != None:
            category1 = await ctx.guild.create_category(f"Hosted By {ctx.message.author}")
            await asyncio.sleep(2)
            msg = await ctx.send(f"Creating Voice Channel For {players} Players.")
            vc = await guild.create_voice_channel(user_limit=players, name=f"Game {int(count[str(ctx.guild.id)]) + 1}", category=category1)
            txt = await guild.create_text_channel(name=f"Host Panel", category=category1)
            await txt.set_permissions(ctx.guild.default_role, send_messages=False, read_messages=False)
            await txt.set_permissions(ctx.message.author, send_messages=False, read_messages=True)
            await vc.set_permissions(ctx.message.author, mute_members=True, move_members=True)
            await vc.set_permissions(role, connect=True)
            await vc.set_permissions(ctx.guild.default_role, connect=False)
            count[str(ctx.guild.id)] = count[str(ctx.guild.id)] + 1
            if str(ctx.guild.id) in log:
                channel = bot.get_channel(int(log[str(ctx.guild.id)]))
                datetime_object = datetime.datetime.now()
                logs=discord.Embed(title="Lobby Logs", color=0x1943c2)
                logs.set_author(name="Game Info")
                logs.add_field(name="Lobby Host:", value=f"{ctx.message.author.mention}", inline=False)
                logs.add_field(name="Time Created:", value=f"{datetime_object}", inline=True)
                logs.add_field(name="Time Deleted:", value=f"N/A", inline=False)
                logs.add_field(name="Max Players Limit:", value=f"{players} Players", inline=True)
                logs.add_field(name="Lobby Name:", value=f" Game {int(count[str(ctx.guild.id)]) + 1}", inline=True)
                logs.set_footer(text="Created By <Dips#6999")
                logss = await channel.send(embed=logs)
             


            
            

            with open("counter.json", 'w') as f:
                json.dump(count, f, indent=4)

            
            
            

            await msg.edit(content=f'Lobby Created For ```{role}```, Hosted By {ctx.message.author.mention}. Access Your {txt.mention} Here')
            


            
        await author.move_to(vc)
        await txt.send(f"{ctx.message.author.mention} Welcome")
        embed=discord.Embed(title="Your Host Panel!", description="This Is Your Personal Host Panel!", color=0x53e4bb)
        embed.add_field(name="**React With 🔇 To Mute ** ", value="React Once To Mute All And Again To Unmute", inline=False)
        embed.add_field(name="**React With 🔒 To Lock **", value="React Once To Lock The Lobby And Again To Open", inline=False)
        embed.add_field(name="**React With 🚫 To Close **", value="React To Close The Your Lobbu", inline=True)
        msg15 = await txt.send(embed=embed)
        await msg15.add_reaction("🔇")
        await msg15.add_reaction("🔒")
        await msg15.add_reaction("🚫")
        #await msg15.add_reaction("emoji")
        await asyncio.sleep(3)
        await msg.delete()
        await ctx.message.delete()
        while True:
            def check(reaction, user):
                return user == host and user != "Crewmate#9393" and str(reaction.emoji) == "🚫" or "🔇" or "🔒"





            with open('hidelobby.json', 'r') as f:
                hide = json.load(f)

            if hide[str(ctx.guild.id)] == True and vc.user_limit == len(vc.members):
                print("Doesn't Viewing Channel")
                await vc.set_permissions(ctx.guild.default_role, view_channel=False)
            elif vc.user_limit != len(vc.members):
                print("Viewing Channel")
                await vc.set_permissions(ctx.guild.default_role, view_channel=True)


                    

                
                


            try:
                 
                reaction, user = await bot.wait_for("reaction_add", check = check)
            
            except asyncio.TimeoutError:
                    
                print("TimeOut")

            half = int(vc.user_limit) / 2

            if str(reaction.emoji) == "🚫" and ctx.message.author == ctx.message.author and len(vc.members) <= half:
                    
                 
                await msg15.remove_reaction("🚫", host)
                
                await txt.send(f"{user.mention} Closed The Lobby, Closing Lobby In 5 Seconds")
                await asyncio.sleep(5)


                if str(ctx.guild.id) in log:
                    datetime_object_delete = datetime.datetime.now()
                    channel = bot.get_channel(int(log[str(ctx.guild.id)]))

                    logs_new=discord.Embed(title="Lobby Logs", color=0x1943c2)
                    logs_new.set_author(name="Game Info")
                    logs_new.add_field(name="Lobby Host:", value=f"{ctx.message.author}", inline=False)
                    logs_new.add_field(name="Time Created:", value=f"{datetime_object}", inline=True)
                    logs_new.add_field(name="Time Deleted:", value=f"{datetime_object_delete}", inline=False)
                    logs_new.add_field(name="Max Players Limit:", value=f"{players} Players", inline=True)
                    logs_new.add_field(name="Lobby Name:", value=f"Game {int(count[str(ctx.guild.id)]) + 1}", inline=True)
                    logs_new.set_footer(text="Created By <Dips#6999")
                    if role == None:
                        await logss1.edit(embed=logs_new)
                    elif role != None:
                        await logss.edit(embed=logs_new)

                await vc.delete()
                await txt.delete()
                await category1.delete()

            elif str(reaction.emoji) == "🔇" and ctx.message.author == user:
                if role != None:
                    await msg15.remove_reaction("🔇", user)

                    if muted == False:
                        for users in vc.members:
                            await users.edit(mute=True)
                        muted = True
                        print(muted)
                    elif muted == True:
                        for users in vc.members:
                            await users.edit(mute=False)
                        muted = False
                        print(muted)
                        print(vc.members)
                elif role == None:
                    await msg15.remove_reaction("🔇", user)
                    if muted == False:
                        for users in vc.members:
                            await users.edit(mute=True)

                        muted = True
                        print(muted)
                    elif muted == True:
                        for users in vc.members:
                            await users.edit(mute=False)
                        
                        muted = False
                        print(muted)
            elif str(reaction.emoji) == "🔒" and ctx.message.author == ctx.message.author:
                await msg15.remove_reaction("🔒", host)
                
                if locked == True:
                    await vc.edit(user_limit=len(vc.members))
                    locked = False

                    print(f" locked is {locked}")
                elif locked == False:
                    await vc.edit(user_limit=players)

                    locked = True
                    print(f" locked is {locked}")
                    print(vc.members)






                 




@bot.command()
async def settings(ctx, action=None, *, var=None):
    guild = ctx.guild
    print(var, action)

    with open("hidelobby.json", 'r') as f:
        data = json.load(f)

    with open("voice.json", 'r') as f:
        voice = json.load(f)

    with open("roles.json", 'r') as f:
        roles = json.load(f)

    with open("audit.json", 'r') as f:
        log = json.load(f)

    




    if action == "setvoicechannel" and var != None:


        voice[str(ctx.guild.id)] = str(var)

        with open("voice.json", 'w') as f:
            json.dump(voice, f, indent=4)
        await ctx.send("Voice Channel Set Successfully")
        

    elif action == "hidefull":
        if data[str(guild.id)] == True:


            data[str(ctx.guild.id)] = False

            with open("hidelobby.json", 'w') as f:
                json.dump(data, f, indent=4)
            await ctx.send("Set To False, Now Full lobbies will appear as invisible")




        elif data[str(guild.id)] == False:



            data[str(ctx.guild.id)] = True

            with open("hidelobby.json", 'w') as f:
                json.dump(data, f, indent=4)
            await ctx.send("Set To True.")

    elif action == "sethostrole" and var != None:
            
            
        roles[str(ctx.guild.id)] = str(var)

        with open("roles.json", 'w') as f:
            json.dump(roles, f, indent=4)
        await ctx.send("Host Role Saved.")
    
    elif action =="setauditlogchannel" and var != None:

        log[str(ctx.guild.id)] = str(var)

        with open('audit.json', 'w') as f:
            json.dump(log, f, indent=4)
        await ctx.send("Audit Log Channel Set.")









    elif var == None and action == None:
        settings=discord.Embed(title="**Crewmate Settings**", color=0xb6a5a5)
        settings.add_field(name="Sets The Voice Channel To Open Hosted Games", value=f"`settings setvoicechannel (voice-channel-id)` ", inline=False)
        settings.add_field(name="Sets The Audit Logs Channel", value=f"`settings setauditlogchannel (text-channel-id)` ", inline=False)
        settings.add_field(name="Hide Full Lobbies, Default `False`", value=f"`settings hidefull`, Currently Set To `{data[str(ctx.guild.id)]}`", inline=True)
        settings.add_field(name="Sets The Role Required For Start Hosting", value=f"`settings sethostrole (host-role-name)` ", inline=False)
        settings.set_footer(text=f"Requested By {ctx.message.author}")
        await ctx.send(embed=settings)









@bot.event
async def on_guild_join(guild):
    with open("hidelobby.json", 'r') as f:
        data = json.load(f)


    data[str(guild.id)] = False

    with open("hidelobby.json", 'w') as f:
        json.dump(data, f, indent=4)

    with open("prefixes.json", 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '/'

    with open("prefixes.json", 'w') as f:
        json.dump(prefixes, f, indent=4)


    with open("counter.json", 'r') as f:
        count = json.load(f)

    count[str(guild.id)] = 0

    with open("counter.json", 'w') as f:
        json.dump(count, f, indent=4)

    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        embed=discord.Embed(title="Thanks for adding me!", description="To Start Configing Me, Start By Typing /help.", color=0x381e76)
        embed.set_footer(text="Coded By <Dips#6999 And Idea By Danny-#4531")
        await general.send(embed=embed)




      
   



@bot.event
async def on_guild_remove(guild):
    with open("hidelobby.json", 'r') as f:
        data = json.load(f)


    data.pop(str(guild.id))

    with open("hidelobby.json", 'w') as f:
        json.dump(data, f, indent=4)

    with open("prefixes.json", 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open("prefixes.json", 'w') as f:
        json.dump(prefixes, f, indent=4)

    with open("hidelobby.json", 'r') as f:
        hide = json.load(f)

    hide.pop(str(guild.id))

    with open("hidelobby.json", 'w') as f:
        json.dump(hide, f, indent=4)

    with open("voice.json", 'r') as f:
        voice = json.load(f)
    
    voice.pop(str(guild.id))

    with open("voice.json", 'w') as f:
        json.dump(voice, f, indent=4)
    
    with open("roles.json", 'r') as f:
        roles = json.load(f)

    roles.pop(str(guild.id))

    with open('roles.json', 'w') as f:
        json.dump(roles, f, indent=4)


    with open("counter.json", 'r') as f:
        count = json.load(f)


    count.pop(str(guild.id))

    with open("counter.json", 'w') as f:
        json.dump(count, f, indent=4)








@bot.command()
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    
    prefixes[str(ctx.guild.id)] = str(prefix)

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f"Prefix Changed To `{prefix}`")









@bot.event
async def on_ready():
    print("Bot Is Ready!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"You Playing"))

        




@bot.event
async def on_message(message):
    with open("prefixes.json", 'r') as f:
        data = json.load(f)

 

    for x in message.mentions:
        print(x)
        if 'Crewmate#9393' == str(x) and "prefix" in message.content:
            await message.channel.send(f"My Prefix Is  `{data[str(message.guild.id)]}`")




    await bot.process_commands(message)
 


@bot.command()
async def invite(ctx):
    await ctx.send("Want To Add Me To Your Very Own Server? Here's A Link https://discord.com/api/oauth2/authorize?client_id=759429302918840391&permissions=8&scope=bot")



            
@bot.command()
async def help(ctx):
    with open("prefixes.json", 'r') as f:
        data = json.load(f)  
    embed=discord.Embed(title="**Help Menu**", description=data[str(ctx.guild.id)] + "help to get this menu", color=0x36cea8)
    embed.set_thumbnail(url=f"{bot.user.avatar_url}")
    embed.add_field(name="@Crewmate ", value="Shows prefix for current server", inline=True)
    embed.add_field(name=data[str(ctx.guild.id)] + "Host (Players Playing) (Optional:@Role)", value="Hosts a game, \n creating a channel and an admin panel \n with the ability to mute all / or make a role only lobby", inline=False)
    embed.add_field(name=data[str(ctx.guild.id)] + "Settings", value="Opens the settings menu", inline=True)
    embed.add_field(name=data[str(ctx.guild.id)] + "changeprefix", value="Changes the prefix for this server (@Crewmate to view current prefix)", inline=False)
    embed.set_footer(text="Coded by <Dips#6999 // And Idea By Danny-#4531")
    await ctx.send(embed=embed)


 












    








        

        
        
        











                


            







bot.run(TOKEN)















