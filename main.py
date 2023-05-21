# IMPORTS
import discord
import datetime
from random import choice
from requests import get
from asyncio import sleep
from os import system
from discord.ext import commands
# from keep_alive import keep_alive 


#Commands are going to be called with command_prefix for example in that case it is going to be .function1
#We are also making sure, that server management functions will work
intents = discord.Intents.all()
discord.member = True
bot = commands.Bot(command_prefix=".", description="description", help_command=None, intents = intents)
bot.remove_command('help') #We are removing help command and will make our own below




@bot.command() #Lists all avaible functions / Not updated automatically
async def help(ctx):
    embedHelp = discord.Embed(
        description='All usable commands',
        colour=discord.Colour.blue())

    embedHelp.set_author(name="commands", icon_url="iconUrl") 
    embedHelp.set_footer(text="yourName")
    embedHelp.set_thumbnail(url="thumbnailUrl")

    embedHelp.add_field(name=".function1", value="pinging 1 user", inline=False)

    embedHelp.add_field(name=".function2", value="pinging multiple users", inline=False)

    embedHelp.add_field(name=".function3", value="Bot sends DM", inline=False)

    embedHelp.add_field(name=".function4", value="Storing text", inline=False)

    embedHelp.add_field(name=".function5", value="Sends copy of your file (from function4)", inline=False)

    embedHelp.add_field(name=".function6", value="Sends a photo of a cat from API", inline=False)

    embedHelp.add_field(name=".function7", value="Chooses between 1 - 2 / True or False", inline=False)

    embedHelp.add_field(name='.function8', value="Pinging IP or Domain - to see if ip/domain is online/offline", inline=False)

    embedHelp.add_field(name='.function9', value="Specfic dog from API", inline=False)
    
    embedHelp.add_field(name='.function10', value="Random dog from API", inline=False)

    await ctx.send(embed=embedHelp)



@bot.command() #You can ping discord user with @user
async def function1(ctx, member:discord.Member=None):
  if member == None:
    await ctx.send(f"Try again with user!")
  else:
    await ctx.send(f"You {ctx.message.author.name} pinged {member.mention}")



@bot.command() #You can ping author of the message || ping 1 user || ping 2 user @user1 @user2  
async def function2(ctx, member1:discord.Member=None, member2:discord.Member=None):
  if member1 == None and member2 == None:
    await ctx.send(f"Try again with user/s!")
  elif member1 != None and member2 == None:
    await ctx.send(f"{ctx.message.author.name} pinged {member1.mention}")
  elif member1 != None and member2 != None:
    await ctx.send(f"{member1.mention} wants something from {member2.mention}")



@bot.command() #Bot can send DMs by Discord ID and storing who sent what to who
async def command3(ctx, user = None, message = None):
    if user == None and message == None:
      await ctx.send("Enter user id and message")
    elif user != None and message == None:
      await ctx.send("Enter message")
    else:
      user = await bot.fetch_user(user)
      currentTime = datetime.datetime.now()
      timePlus = datetime.timedelta(hours=2)
      currentTime = currentTime + timePlus
      file = open(f"userDMS.txt", "a")
      file.write((currentTime.strftime("\n%Y-%m-%d %H:%M:%S " + ": " + ctx.author.name + ": said " + str(user) + ": " + message + "\n")))
      file.close()
      await user.send(message)
      print(f"{currentTime}: User {ctx.message.author.name} sent message to {user} - {message}")



@bot.command() #Bot will create text file and store your messages into with time
async def function4(ctx, message=None):
    if message == None:
        await ctx.send('Enter .function4 "your message"')
    else:
        currentTime = datetime.datetime.now()
        #timePlus = datetime.timedelta(hours=2) #This can be used to add +2 hours to the actual time
        #currentTime = currentTime + timePlus
        file = open(f"{ctx.message.author.name}.txt", "a")
        file.write((currentTime.strftime("\n%Y-%m-%d %H:%M:%S " + message + "\n")))
        file.close()
        await ctx.send('The message has been added to your folder')



@bot.command() #Bot will send text document (from function 4) of user that called the function
async def function5(ctx):
    await ctx.send("Your file is:")
    await ctx.send(file=discord.File(f"{ctx.message.author.name}.txt"))



@bot.command() #Contacts cat API and sends picture of a cat
async def function6(ctx): 
    response = get('https://aws.random.cat/meow')
    data = response.json()
    await ctx.send(data['file'])



@bot.command() #Chooses between 1 and 2
async def function7(ctx):
    await ctx.send(choice("12"))



@bot.command() #Pinging server / Works only on those servers, where you have access to the console
               #Ping -c 1 IP works only for Linux || for Windows it is ping -n 1 IP
async def function8(ctx, ip=None):
    if ip == None:
        
        await ctx.send("Try again with IP or domain")
        
    else:    
        
        response = system("ping -c 1 {ip}")

        if response == 0: 
            await ctx.send("Online")
        else:
            await ctx.send("Not Online")



@bot.command() #Contacts dog API and sends picture of a pembroke dog
async def function9(ctx):
    response = get('https://dog.ceo/api/breed/pembroke/images/random')
    data = response.json()
    await ctx.send(data['message'])



@bot.command() #Contacts dog API and sends picture of a random dog
async def function10(ctx): 
    response = get('https://dog.ceo/api/breeds/image/random')
    data = response.json()
    await ctx.send(data['message'])



@bot.event #Bot information after login 
async def on_ready():

    bot.loop.create_task(presence_changer())
    print("...........")
    print("Logged as")
    print("Name: " + bot.user.name)
    print("ID: " + str(bot.user.id))
    print("...........")   
   

#When member joins
@bot.event
async def on_member_join(member):
    guild = bot.get_guild(guildID) #Guild stands for discord server
    channelWelcome = bot.get_channel(channelID) #Bot is storing channel ID
    await channelWelcome.send(f"Welcome {member.mention}🥳.") #Welcoming user in channel we have selected

#When member leaves
@bot.event
async def on_member_remove(member):
    guild = bot.get_guild(guildID) #Guild stands for discord server
    channelRemove = bot.get_channel(channelID) #Bot is storing channel ID
    await channelRemove.send(f"{member} has left 😥") #Bot sends message 

#Bot gives roles based on reactions
@bot.event
async def on_raw_reaction_add(payload):
    messageId = idOfTheMessageYouWantToAddReactions
    
    if messageId == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name

        if emoji == "emojiName":
            role = discord.utils.get(guild.roles, name="role1")
        elif emoji == "emojiName2":
            role = discord.utils.get(guild.roles, name="role2")

        await member.add_roles(role)






async def presence_changer(): #Function to change discord presence
    while True:
        await bot.change_presence(activity=discord.Game(name = choice("list[]/tuple() of your presences")))
        await sleep(10)
        await bot.change_presence(activity=discord.Game(name = choice("Same list[]/tuple() of your presences")))
        await sleep(10)



@bot.listen() #Bot is listening to the words
async def on_message(message): #He does not respond to his own words
    if message.author == bot.user:
        return

    if any(word in message.content for word in "word or {list[]/tuple()/variable}"):
      await message.channel.send("message")
    
    if isinstance(message.channel,discord.DMChannel): #Bot will save every Dm sent to him to a file.
        currentTime = datetime.datetime.now()
        file = open(f"botDM.txt", "a")
        file.write((currentTime.strftime("\n%Y-%m-%d %H:%M:%S "+ ": " + message.author.name + ": " + message.content + "\n")))
        file.close()
 



#keep_alive() #If bot is hosted for example via replit then uncomment and go to keep_alive.py if not you dont need it 



#Bot Token
bot.run("BOT TOKEN from https://discord.com/developers/applications")
