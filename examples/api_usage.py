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

# අර පිස්සු උපදෙස් තියෙන ෆයිල් එක අයින් කරලා, සාමාන්‍ය AI උපදෙස් මෙතන දෙනවා
system_instruction = "ඔබ ඉතාමත් බුද්ධිමත්, මිත්‍රශීලී සහ සාමාන්‍ය AI සහායකයෙකි. කිසිදු චරිතයක් රඟ දැක්වීමෙන් වළකින්න. පරිශීලකයා අසන ඕනෑම ප්‍රශ්නයකට නිවැරදිව, පැහැදිලිව සහ ගෞරවනීය ලෙස සිංහල භාෂාවෙන් පමණක් පිළිතුරු ලබා දෙන්න."

try:
    response = client.models.generate_content(
        model=selected_model,
        contents=user_prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
        )
    )
    # පිළිතුර පමණක් ලබා දීම
    print(response.text)
except Exception as e:
    print(f"දෝෂයක් මතු විය: {e}")
