import os
from google import genai
from google.genai import types

api_key = os.environ.get("GEMINI_API_KEY")
selected_model = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
user_prompt = os.environ.get("USER_PROMPT", "හලෝ")

if not api_key:
    print("Error: කරුණාකර GEMINI_API_KEY එක ලබා දෙන්න!")
    exit()

client = genai.Client(api_key=api_key)

try:
    with open('core_mantle.txt', 'r', encoding='utf-8') as f:
        system_instruction = f.read()
except FileNotFoundError:
    system_instruction = "You are a helpful AI assistant."

print(f"⏳ {selected_model} වෙත පණිවිඩය යවමින් පවතී...\n")

try:
    response = client.models.generate_content(
        model=selected_model,
        contents=user_prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
        )
    )
    print("=== AI ප්‍රතිචාරය (Response) ===")
    print(response.text)
except Exception as e:
    print(f"දෝෂයක් මතු විය: {e}")
