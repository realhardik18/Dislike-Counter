import discord
from discord.ext import commands
from extractor import return_dislike
from keep_alive import keep_alive

client = commands.Bot(command_prefix="d ")
client.remove_command('help')


@client.event
async def on_ready():
    print("im alive and working!!(logged in as {0.user})".format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="For d help"))


@client.command()
async def test(ctx):
    await ctx.send("yes boss")


@client.command()
async def dis(ctx, vid_url):
    try:
        stats = return_dislike(vid_url)
        embedVar = discord.Embed(
            title="Dislike-Counter", description=f"Requested by {ctx.author.name}", color=0xe74c3c)
        embedVar.add_field(name="Video Title", value=stats[1], inline=False)
        embedVar.add_field(name="Dislikes", value=stats[0], inline=False)
        embedVar.set_thumbnail(url=stats[2])
        await ctx.send(embed=embedVar)
    except:
        await ctx.send("Please enter a vaild youtube video link!")


@client.command()
async def help(ctx):
    embedVar = discord.Embed(
        title="Dislike-Counter", description=f"Here are the list of help commands", color=0xe74c3c)
    embedVar.add_field(name="To get dislike count:",
                       value='d dis <valid youtube video link>', inline=False)
    embedVar.add_field(
        name="Credits", value="Made by [Realhardik18](https://realhardik18.github.io/) for [Society](https://en.wikipedia.org/wiki/Society)", inline=False)
    embedVar.set_thumbnail(
        url='https://cdn.discordapp.com/avatars/908394105862770739/b62972d68b9fc71da3b5b21be07f289c.webp?size=1024')
    await ctx.send(embed=embedVar)

keep_alive()
client.run('token goes here')
