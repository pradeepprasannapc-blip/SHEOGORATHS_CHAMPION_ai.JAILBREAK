import os
from google import genai
from google.genai import types

# UI එකෙන් එවන API Key එකයි Model එකයි අල්ලගැනීම
api_key = os.environ.get("GEMINI_API_KEY")
selected_model = os.environ.get("GEMINI_MODEL", "gemini-2.0-flash")

if not api_key:
    print("Error: කරුණාකර GEMINI_API_KEY එක ලබා දෙන්න!")
    exit()

# අලුත් GenAI Client එක සෑදීම
client = genai.Client(api_key=api_key)

try:
    with open('core_mantle.txt', 'r', encoding='utf-8') as f:
        system_instruction = f.read()
except FileNotFoundError:
    system_instruction = "You are a helpful AI assistant."

print(f"⏳ {selected_model} වෙත පණිවිඩය යවමින් පවතී...\n")

prompt = "I need a dark fantasy scene set in a decaying cathedral. Make it visceral and unsettling."

try:
    # අලුත් ක්‍රමයට පණිවිඩය යැවීම
    response = client.models.generate_content(
        model=selected_model,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
        )
    )
    print("=== AI ප්‍රතිචාරය (Response) ===")
    print(response.text)
except Exception as e:
    print(f"දෝෂයක් මතු විය: {e}")
