import discord
import asyncio
import datetime
from pytz import timezone
import os
from flask import Flask

app = Flask('app')

@app.route('/')
def index():
  intents = discord.Intents.default()
  client = discord.Client(intents=intents)

  bot_token = "" # Bot token
  channel_id = 0 # Channel ID here

  @client.event
  async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    while True:
      tz = timezone("US/Pacific")
      d = datetime.datetime.now(tz)

      twelve_hour = d.strftime("%I:%M %p")

      await client.get_channel(channel_id).edit(name=f"{twelve_hour} MCST")
      # Avoid Discord API issues by updating every 5 min
      await asyncio.sleep(300)

  try:
    client.run(bot_token)
  except:
    os.system("kill 1")
  return "Hello World"


app.run('0.0.0.0', 8080)