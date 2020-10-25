#Among Us Bot
import discord
from discord.ext import commands
import json
from discord.ext.commands import has_permissions, CheckFailure
import requests
import asyncio
import random
from discord.utils import get
from discord.utils import find
import datetime
import os
from dotenv import load_dotenv
import string
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

@bot.command(aliases = ['h'])
async def host(ctx, players: int, *, role:discord.Role=None):
    roles_list = ctx.author.roles
    roles_list.reverse()
    top_role = roles_list[0]



    print(role)
    with open("voice.json", 'r') as f:
        data = json.load(f)


    with open("roles.json", 'r') as f:
        roles = json.load(f)








    with open('ads.json', 'r') as f:
        ad = json.load(f)



    

    








    muted = False
    locked = True
    isClosed = False
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
    elif role != None and top_role < role:
        await ctx.send("Make Sure Your highest Role Is Above The Role You Mentioned!")
    



    elif role_re not in ctx.message.author.roles:
        await ctx.send("You Don't Have The Required Role To Start Hosting!")
    elif players < 11 and players > 3 and str(ctx.message.author.voice.channel.id) == data[str(ctx.guild.id)] and data[str(ctx.guild.id)] != None and role_re in ctx.message.author.roles:
        await ctx.send("Creating Lobby...")
        gamenum = random.randint(1000, 9999)
        if role == None:
                

            category1 = await ctx.guild.create_category(f"Hosted By {ctx.message.author}")
            await asyncio.sleep(2)

            msg = await ctx.send(f"Creating Voice Channel For {players} Players.")
            vc = await guild.create_voice_channel(user_limit=players, name=f"Game {gamenum}", category=category1)
            txt = await guild.create_text_channel(name=f"Host Panel", category=category1)
            await txt.set_permissions(ctx.guild.default_role, send_messages=False, read_messages=False)
            await vc.set_permissions(ctx.guild.default_role, connect=True)
            await txt.set_permissions(host, send_messages=False, read_messages=True)
            await vc.set_permissions(host, mute_members=True, move_members=True)
            
                #something










            await msg.edit(content=f'Lobby Created, Hosted By {ctx.message.author.mention}. Access Your {txt.mention} Here')
        elif role != None:

            overwrites = {
                guild.default_role: discord.PermissionOverwrite(connect=False, view_channel=False),
                role: discord.PermissionOverwrite(connect=True, view_channel=True)
                
            }






            #default_role = get(ctx.guild.roles, name=dr[str(ctx.guild.id)])
            category1 = await ctx.guild.create_category(f"Hosted By {ctx.message.author}")
            await asyncio.sleep(2)
            msg = await ctx.send(f"Creating Voice Channel For {players} Players.")
            vc = await guild.create_voice_channel(user_limit=players, name=f"Game {gamenum}", category=category1, overwrites=overwrites)
            txt = await guild.create_text_channel(name=f"Host Panel", category=category1)
            await category1.set_permissions(role, connect=True)
            await category1.set_permissions(ctx.guild.default_role, connect=False)
            await txt.set_permissions(ctx.guild.default_role, send_messages=False, read_messages=False)
            await txt.set_permissions(host, send_messages=False, read_messages=True)
            await vc.set_permissions(host, mute_members=True, move_members=True, connect=True)
            await vc.set_permissions(ctx.guild.default_role, connect=False)

             


            
            



            
            
            

            await msg.edit(content=f'Lobby Created For `{role}`, Hosted By {ctx.message.author.mention}. Access Your {txt.mention} Here')
            


            
        await author.move_to(vc)
        await txt.send(f"{ctx.message.author.mention} Welcome")
        embed=discord.Embed(title="Your Host Panel!", description="This Is Your Personal Host Panel!", color=0x53e4bb)
        embed.add_field(name="**React With 🔇 To Mute ** ", value="React Once To Mute All And Again To Unmute", inline=False)
        embed.add_field(name="**React With 🔒 To Lock **", value="React Once To Lock The Lobby And Again To Open", inline=False)
        embed.add_field(name="**React With 🚫 To Close **", value="React To Close The Your Lobby", inline=False)
        embed.add_field(name="**React With 📝 To Rename **", value="React To Rename Your Lobby Name", inline=True)
        msg15 = await txt.send(embed=embed)
        await msg15.add_reaction("🔇")
        await msg15.add_reaction("🔒")
        await msg15.add_reaction("🚫")
        await msg15.add_reaction("📝")
        #await msg15.add_reaction("emoji")
        await asyncio.sleep(3)
        await msg.delete()
        await ctx.message.delete()
        if str(ctx.guild.id) in ad:
            channel = bot.get_channel(int(ad[str(ctx.guild.id)]))
            join=discord.Embed(title=f"Click Me To Join!", color=0x11ff00)
            embed.set_author(name=f"{host} is Looking For Crewmates!", icon_url=host.avatar_url)
            join.set_thumbnail(url=f"{bot.user.avatar_url}")
            join.add_field(name="**Players Playing:**", value=f"{len(vc.members)} \ {vc.user_limit}", inline=False)
            join.add_field(name="**Voice Name:**", value=f"{vc.name}", inline=True)
            joinMessage = await channel.send(embed=join)
            invite = await channel.send(await vc.create_invite())





        while True:
            try:
                channel = bot.get_channel(int(ad[str(ctx.guild.id)]))
            except:
                pass
            else:
                
                join2=discord.Embed(title=f"Click Me To Join!", color=0x11ff00)
                join2.set_author(name=f"{host} Is Looking For Crewmates!", icon_url=host.avatar_url)
                join2.set_thumbnail(url=f"{bot.user.avatar_url}")
                join2.add_field(name="**Players Playing:**", value=f"{len(vc.members)} \ {vc.user_limit}", inline=False)
                join2.add_field(name="**Voice Name:**", value=f"{vc.name}", inline=True)
            if role != None and isClosed is False:
                join2.add_field(name="**Lobby Status:**", value=f"Closed For {role.mention}", inline=True)
                await joinMessage.edit(embed=join2)
            elif role == None and isClosed is False:
                join2.add_field(name="**Lobby Status:**", value=f"Open", inline=True)
                await joinMessage.edit(embed=join2)






            def check(reaction, user):
                return user == host and user != "Crewmate#9393" and str(reaction.emoji) == "🚫" or "🔇" or "🔒" or "📝"






                    

                
                


            try:
                 
                reaction, user = await bot.wait_for("reaction_add", check = check)
            
            except asyncio.TimeoutError:
                    
                print("TimeOut")

            half = int(vc.user_limit) / 2

            if str(reaction.emoji) == "🚫" and host == user and len(vc.members) <= half:
                def confirm_generator(size=6, chars=string.ascii_uppercase + string.digits):
                    return ''.join(random.choice(chars) for _ in range(size))
                    
                 
                await msg15.remove_reaction("🚫", host)
                confirm_number = confirm_generator()


                confirm=discord.Embed(color=0xff0000)
                confirm.add_field(name="Lobby Canceling Confirmation", value=f"Type **{confirm_number}** To Close The Lobby", inline=False)
                confirm_message = await txt.send(embed=confirm)
                await txt.set_permissions(host, send_messages=True, read_messages=True)

                def confirmationCheck(m):
                    return str(m.content) == str(confirm_number) and m.author == host

                try:
                    confirmed = await bot.wait_for('message', timeout=60.0, check=confirmationCheck)
                    await confirm_message.delete()
                except:
                    timeError = await txt.send("Timed Out")
                    asyncio.sleep(3)
                    await timeError.delete()
                    await txt.set_permissions(host, send_messages=False, read_messages=True)
                    await confirm_message.delete()

                else:
                    await txt.set_permissions(host, send_messages=False, read_messages=True)
                    await txt.send(f"{user.mention} Closed The Lobby, Closing Lobby In 5 Seconds")
                    await invite.delete()
                    try:
                        closed=discord.Embed(title=f"Joining Unavaliable", color=0xff0000)
                        closed.set_author(name=f"{host} Was Looking For Crewmates!", icon_url=host.avatar_url)
                        closed.set_thumbnail(url=f"{bot.user.avatar_url}")
                        await joinMessage.edit(embed=closed)
                    isClosed = True
                    await asyncio.sleep(5)
                    await vc.delete()
                    await txt.delete()
                    await category1.delete()



            elif str(reaction.emoji) == "🔇" and host == user:
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
            elif str(reaction.emoji) == "🔒" and host == user:
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
            elif str(reaction.emoji) == "📝" and host == user:
                def nameCheck(m):
                    return m.content != ""


                await msg15.remove_reaction("📝", host)
                await txt.send("Type The Name You Wish To Change To")


                await txt.set_permissions(host, send_messages=True, read_messages=True)
                lobbyName = await bot.wait_for("message",check=nameCheck)
                await vc.edit(name=lobbyName.content)
                await txt.set_permissions(host, send_messages=False, read_messages=True)
                await txt.purge(limit=2)
            

                    








                    

                    

                








                 




@bot.command(aliases = ['s', 'set'])
@has_permissions(manage_channels=True)  
async def settings(ctx, action=None, *, var=None):
    guild = ctx.guild
    print(var, action)



    with open("voice.json", 'r') as f:
        voice = json.load(f)

    with open("roles.json", 'r') as f:
        roles = json.load(f)




    with open("ads.json", 'r') as f:
        ad = json.load(f)



    




    if action == "setvoicechannel" and var != None:


        voice[str(ctx.guild.id)] = str(var)

        with open("voice.json", 'w') as f:
            json.dump(voice, f, indent=4)
        await ctx.send("Voice Channel Set Successfully")
        






    elif action == "sethostrole" and var != None:
            
            
        roles[str(ctx.guild.id)] = str(var)

        with open("roles.json", 'w') as f:
            json.dump(roles, f, indent=4)
        await ctx.send("Host Role Saved.")


    elif action == "setadlobby" and var != None:
        ad[str(ctx.guild.id)] = str(var)

        with open('ads.json', 'w') as f:
            json.dump(ad, f, indent=4)
        await ctx.send("Channel set.")












    elif var == None and action == None:
        settings=discord.Embed(title="**Crewmate Settings**", color=0xb6a5a5)
        settings.add_field(name="Sets The Voice Channel To Open Hosted Games", value=f"`settings setvoicechannel (voice-channel-id)` ", inline=False)
        settings.add_field(name="Sets The Role Required For Start Hosting", value=f"`settings sethostrole (host-role-name)` ", inline=True)
        settings.add_field(name="Sets The Channel To Send Other People Lobbys", value=f"`settings setadlobby (AD-channel-id)` ", inline=False)
        settings.set_footer(text=f"Requested By {ctx.message.author}")
        await ctx.send(embed=settings)









@bot.event
async def on_guild_join(guild):


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





@settings.error
async def settings_error(error, ctx):
    if isinstance(error, CheckFailure):
        await ctx.send("Look Like You Don't Have Permission To Use That!")

   



@bot.event
async def on_guild_remove(guild):


    with open("prefixes.json", 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open("prefixes.json", 'w') as f:
        json.dump(prefixes, f, indent=4)



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

    








@bot.command(aliases = ['change', 'cha', 'c'])
@has_permissions(manage_roles=True)
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

        

@bot.command(aliases = ['ren', 're'])
@has_permissions(manage_channels=True)
async def rename(ctx, *, new_name):
    try:
        int(ctx.author.voice.channel.id)
    except:
        await ctx.send("Please Enter A Voice Channel To Use This Command")
    else:
        channel = ctx.author.voice.channel
        old_name = channel.name
        await channel.edit(name=new_name)
        await ctx.send(f"Channel Name Changed From `{old_name}`=>`{new_name}`")


        
        
        
        


@bot.event
async def on_message(message):
    with open("prefixes.json", 'r') as f:
        data = json.load(f)

 

    for x in message.mentions:
        print(x)
        if 'Crewmate#9393' == str(x) and "prefix" in message.content:
            await message.channel.send(f"My Prefix Is  `{data[str(message.guild.id)]}`")




    await bot.process_commands(message)
 


@bot.command(aliases = ['inv'])
async def invite(ctx):
    await ctx.send("Want To Add Me To Your Very Own Server? Here's A Link https://discord.com/api/oauth2/authorize?client_id=759429302918840391&permissions=8&scope=bot")



            
@bot.command(aliases = ['hel', 'he'])
@commands.cooldown(rate=1, per=4, type=commands.BucketType.user)
async def help(ctx):
    with open("prefixes.json", 'r') as f:
        data = json.load(f)  
    embed=discord.Embed(title="**Help Menu**", description=data[str(ctx.guild.id)] + "help to get this menu", color=0x36cea8)
    embed.set_thumbnail(url=f"{bot.user.avatar_url}")
    embed.add_field(name="@Crewmate prefix ", value="Shows prefix for current server", inline=True)
    embed.add_field(name=data[str(ctx.guild.id)] + "Host (Players Playing) (Optional:@Role)", value="Hosts a game, \n creating a channel and an admin panel \n with the ability to mute all / or make a role only lobby", inline=False)
    embed.add_field(name=data[str(ctx.guild.id)] + "Settings", value="Opens the settings menu", inline=True)
    embed.add_field(name=data[str(ctx.guild.id)] + "Changeprefix", value="Changes the prefix for this server (@Crewmate to view current prefix)", inline=False)
    embed.add_field(name=data[str(ctx.guild.id)] + "Rename", value="Changes the name for your current vc", inline=True)
    embed.set_footer(text="Coded by <Dips#6999 // And Idea By Danny-#4531")
    await ctx.send(embed=embed)


 











    








        

        
        
        











                


            







bot.run(TOKEN)
