import discord
from discord import FFmpegPCMAudio
import os
import requests
import json
import cmath
import random
import youtube_dl
from discord.ext import commands , tasks
from itertools import cycle

client = commands.Bot(command_prefix='*')

queues = {}

def check_queue(ctx, id):
	if queues[id] != []:
		voice = ctx.guild.voice_client
		source = queues[id].pop(0)
		player = voice.play(source)

sad_word=["sad","depressed","oops"]

happy_words=["lol","happy","xd","khushi"]

gn_words=["gn","sone","sleep"]

bye_words=["bye","chala"]

self_words=["nice work bot","wow bot","thanks bot"]

reply_self=["MY PLEASURE SIR . THANKS FOR APPRECIATION"]

reply_bye=["ja na kisne roka hai tereko","pehli fursat mei nikal"]

reply_gn=["ja soja","jaldi so subah uthna hai tereko","tu soja mei hu yaha sambhal lunga"]

encouragements_happy=["aaj jayada khush hai tu","aaj ache mood mei hai tu","ka bhai itna khushi lottery lag gayi kya","bas bas ab itna khush hone ki jarurat nahi"]

encouragements_sad=["You are great.have faith in yourself","cheer up","ek peg mar aur chill kar","ritwik se bat kar le",]

def get_quote():
	response= requests.get("https://zenquotes.io/api/random")
	json_data = json.loads(response.text)
	quote= json_data[0]['q'] + " -" + json_data[0]['a']
	return(quote)



@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.idle,activity=discord.Game('SEARCHING THE INFINITY'))
	print('Bot is ready.')

@client.event
async def on_member_join(member):
	print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
	print(f'{member} has left the server.')

#For knowing the ping.

@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency*1000)}ms')

#Calling malav.

@client.command(aliases=['bsdwala'])
async def malav(ctx):
	await ctx.send(f'Malav Thakkar, Cse wale hai ,heavy comder hai')

#calling himanshu,god,engineeringgod,csegod.

@client.command(aliases=['god','engineeringgod','csegod'])
async def himanshu(ctx):
	await ctx.send(f'congrats you have just called @v1per AKA engineering god')

#calling harshal,boss,hero.




@client.command(aliases=['boss','hero'])
async def harshal(ctx):
	await ctx.send(f'baap ko kyu bulaya bsdk')

#For playing 8ball game.

@client.command(aliases=['8ball','test'])
async def _8ball(ctx,*, question):
	responses = ["It is certain.",
				"It is decidedly so.",
				"Without a doubt.",
				"Yes - definitely.",
				"You may rely on it.",
				"As I see it, yes.",
				"Most likely.",
				"Outlook good.",
				"Yes.",
				"Signs point to yes.",
				"Reply hazy, try again.",
				"Ask again later.",
				"Better not tell you now.",
				"Cannot predict now.",
				"Concentrate and ask again.",
				"Don't count on it.",
				"My reply is no.",
				"My sources say no.",
				"Outlook not so good.",
				"Very doubtful."]
	await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

#For deletion.

@client.command(aliases=['saafkaro'])
async def delete(ctx,amount=2):
	await ctx.channel.purge(limit=amount)
	await ctx.send(f'swaach bharat abhiyan ke antargat {amount} message delete kiya gaya')

#For kicking member.

@client.command()
@commands.is_owner()
async def kick(ctx,member : discord.Member,*,reason=None):
	await member.kick(reason=reason)
	await ctx.send(f'yaad teri aayegi {member.mention}')

#For banning member.



@client.command()
@commands.is_owner()
async def ban(ctx,member : discord.Member,*,reason=None):
	await member.ban(reason=reason)
	await ctx.send(f'{member.mention} has been banned for your indisciplinary act')

#For welcome.

@client.command()
async def welcome(ctx,member : discord.Member):
	await ctx.send(f'{member.mention} welcome back')


#For calling.
@client.command()
async def aaja(ctx,member : discord.Member):
	await ctx.send(f'Aaja {member.mention} kitna baat karega bhabhi se . Bhai log ke sath gaana sunle')

#For doing spam.
@client.command()
async def spam(ctx,n:int,*,member: discord.Member):
	while  n>0 :
		await ctx.send(f'{member.mention}')
		n-=1


#For sad, happy,bye,gn word reply.
#for self love.

@client.event
async def on_message(message):
	if message.author == client.user:
			return
	if any (word in message.content for word in sad_word):
		await message.channel.send(random.choice(encouragements_sad))
	if any (word in message.content for word in happy_words):
		await message.channel.send(random.choice(encouragements_happy))
	if any (word in message.content for word in gn_words):
		await message.channel.send(random.choice(reply_gn))
	if any (word in message.content for word in bye_words):
		await message.channel.send(random.choice(reply_bye))

	if any(word in message.content for word in self_words):
		await message.channel.send(random.choice(reply_self))
	await client.process_commands(message)

	

#For unbanning a member.

@client.command()
async def unban(ctx,*, member):
	banned_users = await ctx.guild.bans()
	member_name,member_discriminator = member.split('#')

	for ban_entry in banned_users:
		user=ban_entry.user


		if(user.name, user.discriminator)==(member_name,member_discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f'unbanned {user.mention}')
			return

#For inspiring quotes.

@client.command(name='inspire')
async def inspire(ctx):
	quote = get_quote()
	await ctx.send(quote)



#For cheating.

@client.command(aliases=["ansbata","ans"])
async def cheat(ctx,n:int,*,member: discord.Member):
	await ctx.send(f'{member.mention} question {n} ka answer bata jaldi')

#for addition.

@client.command(aliases=["sum","plus"])
async def add(ctx,n1:float,n2:float):
	await ctx.send(f'the sum of {n1} and{n2} is {n1+n2}')


#for subtraction.

@client.command(aliases=["diff","minus"])
async def subtract(ctx,n1:float,n2:float):
	await ctx.send(f'the diff of {n1} and{n2} is {n1-n2}')


#for multiplication.

@client.command(aliases=["product","gunna"])
async def multiply(ctx,n1:float,n2:float):
	await ctx.send(f'the product of {n1} and{n2} is {n1*n2}')

#for division.

@client.command(aliases=["divide"])
async def division(ctx,n1:float,n2:float):
	await ctx.send(f'the division of {n1} by {n2} is {n1/n2}')


#for remiander.
@client.command(aliases=["whole_ans"])
async def remiander(ctx,n1:int,n2:int):
	await ctx.send(f'the remiander when{n1} is divided by {n2} is{n1%n2}')

#for finding power.

@client.command(aliases=["pow"])
async def power(ctx,n1:float,n2:int):
	ans=n1
	while n2 > 1:
		ans=ans* n1
		n2-=1
	await ctx.send(f' the answer is {ans} ')


#for finding solution of quadratic equation.

@client.command(alaises=["solve_quadratic"])
async def quadratic(ctx,a:float,b:float,c:float):
	d = (b**2) - (4*a*c)

	sol1 = (-b-cmath.sqrt(d))/(2*a)
	sol2 = (-b+cmath.sqrt(d))/(2*a)
	await ctx.send(f'the roots of {a}x2 + {b}x + {c} = 0  are {sol1} and {sol2}')


#for joining voice channel
@client.command(pass_context=True)
async def join(ctx):
	if (ctx.author.voice):
		channel=ctx.message.author.voice.channel
		await channel.connect()
	else:
		await ctx.send('you are not in a voice channel')

#For leaving the voice channel
@client.command(pass_context=True)
async def leave(ctx):
	if(ctx.voice_client):
		await ctx.guild.voice_client.disconnect()
		await ctx.send('I left the voice channel')
	else:
		await ctx.send('I am not in a voice channel')

#For playing the song
@client.command(pass_context=True)
async def play(ctx,*, arg):
	voice = ctx.guild.voice_client
	song = arg + '.mp3'
	source = FFmpegPCMAudio(song)
	player = voice.play(source, after=lambda x=None: check_queue(ctx, ctx.message.guild.id))

#For queueing a bot
@client.command(pass_context=True)
async def queue(ctx,*, arg):
	voice = ctx.guild.voice_client
	song = arg +'.mp3'
	source = FFmpegPCMAudio(song)

	guild_id = ctx.message.guild.id

	if guild_id in queues:
		queues[guild_id] = [source]
	else:
		queues[guild_id] = [ source]

	await ctx.send('added to queue')

#For pausing the song
@client.command(pass_context=True)
async def pause(ctx):
	voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
	if voice.is_playing():
		voice.pause()
	else:
		await ctx.send('At the moment , there is no song playing')

#For resuming the song
@client.command(pass_context=True)
async def resume(ctx):
	voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
	if voice.is_paused():
		voice.resume()
	else:
		await ctx.send("At the moment , no song is paused")

#For stopping the song.
@client.command(pass_context=True)
async def stop(ctx):
	voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
	voice.stop()
#For embeding.
@client.command()
async def embed(ctx,*,arg:str):
	embed = discord.Embed(title=arg, url="https://www.google.com/search?q="+arg, description="we love "+ arg, color=0x4dff4d)
	embed.set_author(name=ctx.author.display_name, url="https://instagram.com", icon_url=ctx.author.avatar_url)
	embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2016/10/22/17/46/mountains-1761292_960_720.jpg")
	embed.add_field(name="facebook", value = "[https://facebook.com/search?q=](url)", inline= True)
	embed.add_field(name="instagram", value = "[https://instagram.com](url)", inline= True)
	embed.set_footer(text="Thank you for reading")
	await ctx.send(embed=embed)

@client.command()
async def insta(ctx,*,arg:str):
	insta = discord.Embed(title="Instagram", url="https://www.instagram.com/"+arg +"/", description="here you go", color=0xff33bb)
	insta.set_author(name=ctx.author.display_name, url="https://instagram.com/search?q="+ arg, icon_url=ctx.author.avatar_url)
	insta.set_thumbnail(url="https://cdn.pixabay.com/photo/2016/10/22/17/46/mountains-1761292_960_720.jpg")
	insta.add_field(name="instagram", value = "Click the link to go to your insta page", inline= True)
	insta.set_footer(text="Thank you for reading")
	await ctx.send(embed=insta)

#For youtube link
@client.command()
async def playyt(ctx, url:str):
	if(ctx.author.voice):
		channel= ctx.message.author.voice.channel
		voice = await channel.connect()


		ydl_opts ={
		'format': 'bestaudio/best',
		'postprocessors':[{
			'key': 'FFmpegExtractAudio',
			'preferredcodec':'mp3',
			'preferredquality':'192',
		}],
		}
		if os.path.exists("song2.mp3"):
 			 os.remove("song2.mp3")
		with youtube_dl.YoutubeDL(ydl_opts)as ydl:
			ydl.download([url])
		for file in os.listdir("./"):
			if file.endswith(".mp3"):
				os.rename(file,"song2.mp3")



		source = FFmpegPCMAudio('song2.mp3')
		player = voice.play(source)



	else:
		await ctx.send("you are not in a voice channel, you must be in a voice channel to run this command")

client.run('ODQ2OTg2MjA0NjQxNjI0MDk1.YK3fXw.D1d9v66PGA51Q-GfeqS9WW4Pz5o')
