import discord

bot = discord.Bot()
with open("token") as f:
    bottoken = f.read()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(description="Say Hello to FinFin!", guild_ids=[])
async def hello(ctx):
    await ctx.respond("Hello!")

@bot.slash_command(description="Get bot latency", guild_ids=[])
async def ping(ctx):
     await ctx.send(f'Pong! In {round(bot.latency * 1000)}ms')

@bot.slash_command(description="Send Image", guild_ids=[])
async def showmefinfin(ctx):
     with open('finfin1.jpg', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

bot.run(bottoken)
