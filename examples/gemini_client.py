from dotenv import load_dotenv

load_dotenv()

import os

from google import genai

from vibechecks import VibeCheck

# create a google gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# create a vibecheck instance using the above client and specify a model
# model variants for gemini: https://ai.google.dev/gemini-api/docs/models#model-variations
vc = VibeCheck(client, model="gemini-2.0-flash-lite")

# the example below asks user for a number and vibechecks if the number is prime
user_input = input("Enter a number:")
if vc(f"{user_input} is a prime number"):
    print(f"{user_input} is a prime number!")
else:
    print(f"{user_input} is not a prime number.")
