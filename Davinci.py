import openai
import discord
import re
from discord import Intents


#openai api key
openai.api_key = "-----------------"

intents = Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user.mentioned_in(message):
        prompt = re.sub(r'<@[!&]?[\d]+>\s*', '', message.content)
        response = generate_text(prompt)
        await message.channel.send(response)

def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=3500,
        n=1,
        stop=None,

        temperature=0.5,
    )
    return response.choices[0].text


#Discord api key
client.run("----------------")