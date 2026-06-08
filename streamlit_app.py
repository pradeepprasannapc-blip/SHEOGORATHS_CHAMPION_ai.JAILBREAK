import streamlit as st
import subprocess
import os

st.set_page_config(page_title="සිංහල AI Chat", page_icon="🤖")
st.title("🤖 මගේ AI සහායකයා")

st.sidebar.header("⚙️ Settings")
api_key = st.sidebar.text_input("Gemini API Key:", type="password")
model_version = st.sidebar.selectbox(
    "Select Gemini Model:", 
    ["gemini-2.5-flash", "gemini-2.5-flash-lite", "gemini-3.1-pro"] 
)

st.markdown("ඔබට දැනගැනීමට අවශ්‍ය ඕනෑම දෙයක් පහතින් සිංහලෙන් type කර අසන්න.")

# ප්‍රශ්නය අහන පෙට්ටිය
user_prompt = st.text_area("ඔබේ ප්‍රශ්නය මෙහි ඇතුළත් කරන්න:", height=100)

if st.button("අසන්න / Send", type="primary"):
    if not api_key:
        st.warning("⚠️ කරුණාකර වම් පස ඇති Settings මෙනුවෙන් API Key එක ලබා දෙන්න.")
    elif not user_prompt:
        st.warning("⚠️ කරුණාකර ප්‍රශ්නයක් ඇතුළත් කරන්න.")
    else:
        with st.spinner("පිළිතුර සකසමින් පවතී... කරුණාකර රැඳී සිටින්න."):
            try:
                # ඔයා අහන ප්‍රශ්නය Background එකෙන් කෝඩ් එකට යවනවා
                custom_env = os.environ.copy()
                custom_env["GEMINI_API_KEY"] = api_key
                custom_env["GEMINI_MODEL"] = model_version
                custom_env["USER_PROMPT"] = user_prompt 

                # මෙතනදි අපි command එක ස්වයංක්‍රීයව run කරනවා
                result = subprocess.run(
                    "python examples/api_usage.py", 
                    shell=True, 
                    capture_output=True, 
                    text=True,
                    env=custom_env
                )

                st.subheader("පිළිතුර:")
                if result.stdout:
                    # උත්තරේ ලස්සනට කියවන්න පුළුවන් විදිහට පෙන්නනවා
                    st.markdown(result.stdout)
                
                if result.stderr:
                    st.error(result.stderr)
                    
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")
