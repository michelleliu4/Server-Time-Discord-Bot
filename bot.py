import discord
import asyncio
import datetime
import pytz

intents = discord.Intents.default()
client = discord.Client(intents=intents)

distoken = "MTA2MjA2ODQ1MDYxNDMzMzU5MA.GWURTt.yfWWlWuffdeUOnPDBOc0lK2kIspoy9b_j3iJuY"

timechannel = 1062067867073380365

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    while True:
        d = datetime.datetime.now()
        timezone = pytz.timezone("America/Los_Angeles")
        mcst = timezone.localize(d)

        twelve_hour = mcst.strftime("%I:%M %p")

        await client.get_channel(timechannel).edit(name=f"{twelve_hour} MCST")
        # Avoid Discord API issues by updating every 5 min
        await asyncio.sleep(300)


client.run(distoken)