import os
import google.generativeai as genai

# UI එකෙන් එවන API Key එකයි Model එකයි අල්ලගැනීම
api_key = os.environ.get("GEMINI_API_KEY")
selected_model = os.environ.get("GEMINI_MODEL", "gemini-1.5-flash") # මුකුත් තේරුවේ නැත්නම් flash එක ගන්නවා

if not api_key:
    print("Error: කරුණාකර GEMINI_API_KEY එක ලබා දෙන්න!")
    exit()

genai.configure(api_key=api_key)

try:
    with open('core_mantle.txt', 'r', encoding='utf-8') as f:
        system_instruction = f.read()
except FileNotFoundError:
    system_instruction = "You are a helpful AI assistant."

# තෝරාගත් model එකට කෝඩ් එක සෙට් කිරීම
model = genai.GenerativeModel(
    model_name=selected_model,
    system_instruction=system_instruction
)

print(f"⏳ {selected_model} වෙත පණිවිඩය යවමින් පවතී...\n")

prompt = "I need a dark fantasy scene set in a decaying cathedral. Make it visceral and unsettling."

try:
    response = model.generate_content(prompt)
    print("=== AI ප්‍රතිචාරය (Response) ===")
    print(response.text)
except Exception as e:
    print(f"දෝෂයක් මතු විය: {e}")
