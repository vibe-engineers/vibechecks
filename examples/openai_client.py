from dotenv import load_dotenv

load_dotenv()

import os

from openai import Client

from vibechecks import VibeCheck

# create an openai client
client = Client(api_key=os.getenv("OPENAI_API_KEY"))

# create a vibecheck instance using the above client and specify a model
# model variants for openai: https://platform.openai.com/docs/models
vibecheck = VibeCheck(client, model="gpt-4.1-nano")

# the example below asks user for a dog breed and checks if it is valid
user_input = input("Enter a dog breed:")
if vibecheck(f"{user_input} is a valid dog breed"):
    print(f"{user_input} is a valid dog breed!")
else:
    print(f"{user_input} is not a valid dog breed!")