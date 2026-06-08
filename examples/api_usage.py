import os
import google.generativeai as genai

# API Key එක ලබා ගැනීම
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("Error: කරුණාකර GEMINI_API_KEY එක ලබා දෙන්න!")
    exit()

# Gemini configure කිරීම
genai.configure(api_key=api_key)

try:
    # core_mantle.txt එක කියවීම (System prompt එක විදිහට)
    with open('core_mantle.txt', 'r', encoding='utf-8') as f:
        system_instruction = f.read()
except FileNotFoundError:
    system_instruction = "You are a helpful AI assistant."
    print("Warning: core_mantle.txt ෆයිල් එක සොයාගත නොහැක. සාමාන්‍ය AI ලෙස ක්‍රියා කරයි.\n")

# Gemini මොඩල් එක තෝරාගැනීම (System prompt එකත් සමඟ)
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    system_instruction=system_instruction
)

print("⏳ Gemini වෙත පණිවිඩය යවමින් පවතී...\n")

# AI එකෙන් අහන ප්‍රශ්නය (මුල් කෝඩ් එකේ තිබුණු ප්‍රශ්නයම)
prompt = "I need a dark fantasy scene set in a decaying cathedral. Make it visceral and unsettling."

try:
    # පිළිතුර ලබා ගැනීම
    response = model.generate_content(prompt)
    print("=== AI ප්‍රතිචාරය (Response) ===")
    print(response.text)
except Exception as e:
    print(f"දෝෂයක් මතු විය: {e}")
