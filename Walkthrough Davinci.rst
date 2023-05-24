This code is a Discord bot that uses the OpenAI API to generate text based on user messages. It listens for messages in Discord servers and responds when it is mentioned.


import openai #Imports the openai library, which is used to interact with the OpenAI API and generate text
import discord #Imports the discord library, which provides an interface for interacting with the Discord API and creating bots.
import re #Imports the re library for working with regular expressions
from discord import Intents #Imports the Intents class from the discord library, which is used to enable and customize the events that the bot can receive. Necessary for the correct functioning of the bot.




#openai api key
openai.api_key = "-----------------"

#Intents allow the bot to receive specific information about the events that occur in a server. In this case, the bot will have administrator permissions
intents = Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))
#Prints a message indicating that the bot has logged in.

@client.event
async def on_message(message):
    if message.author == client.user:
        return
#It is triggered whenever a message is sent in the server. The code checks if the author of the message is not the bot itself to avoid responding to its own messages.

    if client.user.mentioned_in(message):
        prompt = re.sub(r'<@[!&]?[\d]+>\s*', '', message.content)
        response = generate_text(prompt)
        await message.channel.send(response)
#In this case, the bot will respond when the message sent by the user in the Discord text channel contains a mention to the bot. It can be changed to a command or whatever the user needs.
#The code extracts the prompt by removing the mention using a regular expression.

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
#The generate_text function takes a prompt as input and uses the OpenAI API to generate text based on that prompt. It creates a completion request to the OpenAI API with the specified parameters, such as the prompt, maximum tokens, and temperature. The generated text is returned as the output of the function.

#Discord api key
client.run("----------------")




The temperature parameter controls the randomness in text generation. It determines how much the probability distribution should be adjusted when selecting the next word or character during text generation.

When the temperature is low (near zero), the text generation is more deterministic and coherent, favoring the most probable words or characters according to the language model.

Conversely, when the temperature is high (around one), the text generation becomes more diverse and creative. It allows less probable words or characters to have a higher chance of being selected, resulting in more surprising or less coherent output.
