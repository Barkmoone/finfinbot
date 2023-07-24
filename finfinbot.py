import discord
from PIL import ImageGrab, Image

bot = discord.Bot()
with open("token") as f:
    bottoken = f.read()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(description="Say Hello to FinFin!", guild_ids=[your guild id here])
async def hello(ctx):
    await ctx.respond("Hello!")

@bot.slash_command(description="Get bot latency", guild_ids=[your guild id here])
async def ping(ctx):
     await ctx.respond(f'Pong! In {round(bot.latency * 1000)}ms')

@bot.slash_command(description="Send Image", guild_ids=[your guild id here])
async def showmefinfin(ctx):
     with open('finfin1.jpg', 'rb') as f:
        picture = discord.File(f)
        await ctx.respond(file=picture)

@bot.slash_command(description="Get live picture of FinFin's world", guild_ids=[your guild id here])
async def capture(ctx):
    pic = ImageGrab.grab(bbox=(295, 47, 1625, 1050)) 
    #hardcoded window location snapped to top left on 4k monitor
    pic.save('finfin_live.png')
    with open('finfin_live.png', 'rb') as f:
        livepicture = discord.File(f)
        await ctx.respond(file=livepicture)
        
bot.run(bottoken)
