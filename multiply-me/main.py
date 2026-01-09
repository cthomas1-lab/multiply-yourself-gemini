import os
import json
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Load the project's persona
with open('persona.json', 'r') as f:
    persona = json.load(f)

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Construct the System Instruction from the Project files
instruction = f"You are a digital twin of {persona['name']}. Expertise: {persona['expertise']}. Tone: {persona['tone']}. Bio: {persona['background']}"

chat = client.chats.create(
    model="gemini-3-flash",
    config={"system_instruction": instruction}
)

print(f"--- {persona['name']}'s Digital Twin is Online ---")

while True:
    user_input = input("User: ")
    if user_input.lower() in ['exit', 'quit']: break
    response = chat.send_message(user_input)
    print(f"\n{persona['name']}: {response.text}\n")
