from dotenv import load_dotenv

load_dotenv()

import os

from openai import Client

from vibechecks import VibeCheck

# create an openai client
client = Client(api_key=os.getenv("OPENAI_API_KEY"))

# create a vibecheck instance using the above client and specify a model
# model variants for openai: https://platform.openai.com/docs/models
vc = VibeCheck(client, model="gpt-4.1-nano")

# the example below asks user for a number and vibechecks if the number is prime
user_input = input("Enter a number:")
if vc(f"{user_input} is a prime number"):
    print(f"{user_input} is a prime number!")
else:
    print(f"{user_input} is not a prime number.")
