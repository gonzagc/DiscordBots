import openai
import discord
import re
from discord import Intents

#openai api key
openai.api_key = "----------------"

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
        prompt, image_url = extract_prompt_and_image(message)
        if image_url is not None:
            edited_image_url = generate_edited_image(prompt, image_url)
            await message.channel.send(edited_image_url)
        else:
            generated_image_url = generate_image(prompt)
            await message.channel.send(generated_image_url)

def extract_prompt_and_image(message):
    mention_regex = r'<@[!&]?[\d]+>\s*'
    prompt = re.sub(mention_regex, '', message.content)
    image_url = None
    if message.attachments:
        image_url = message.attachments[0].url
    return prompt, image_url

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url

def generate_edited_image(prompt, image_url):
    response = openai.Image.create_edit(
        image=image_url,
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    edited_image_url = response['data'][0]['url']
    return edited_image_url



#Discord api key
client.run("----------------")


