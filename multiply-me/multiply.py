import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Updated to the current stable model for 2026
model = genai.GenerativeModel('gemini-2.5-flash')
chat = model.start_chat(history=[])

print("--- Multiply Me: Digital Twin Activated (v2026) ---")
print("Type 'exit' to quit.\n")

while True:
    try:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        
        response = chat.send_message(
            f"You are a digital version of the user. Answer this as them: {user_input}"
        )
        print(f"\nDigital Twin: {response.text}\n")
    except Exception as e:
        print(f"\n[Error]: {e}\n")
