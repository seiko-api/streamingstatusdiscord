import discord, os, keep_alive, asyncio, datetime, pytz


from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix=':',
  self_bot=True
)



@client.event
async def on_connect():
  await client.change_presence(activity = discord.Streaming(name = " JASA MAPPING SA-MP | Murah Meriah | Order DM Aja Okkey !! ", url = "https://discord.gg/qK4HbVQWTJ"))


keep_alive.keep_alive()
client.run(os.getenv("TOKEN"), bot=False)
