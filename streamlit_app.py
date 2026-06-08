import streamlit as st
import subprocess
import os

st.set_page_config(page_title="CLI to Streamlit", page_icon="⚙️")
st.title("⚙️ CLI to Streamlit Converter")

# --- අලුත් Settings මෙනුව (වම් පැත්තේ) ---
st.sidebar.header("⚙️ Settings")
api_key = st.sidebar.text_input("Gemini API Key:", type="password", help="ඔබගේ API Key එක මෙහි ලබාදෙන්න.")
model_version = st.sidebar.selectbox(
    "Select Gemini Model:", 
    ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-1.0-pro"] # මෙතනින් කැමති එකක් තෝරන්න පුළුවන්
)

st.markdown("මෙමගින් ඔබට Command-line එකෙහි run කරන ඕනෑම command එකක් මෙහි run කරගත හැක.")

# Command එක (දැන් API key එක මෙතන ගහන්න ඕනි නෑ)
command_input = st.text_input("Enter your command here:", value="python examples/api_usage.py")

if st.button("Run Command", type="primary"):
    if not api_key:
        st.warning("⚠️ කරුණාකර වම් පස ඇති Settings මෙනුවෙන් API Key එක ලබා දෙන්න.")
    elif command_input:
        with st.spinner("Running command... Please wait."):
            try:
                # UI එකෙන් තෝරපු Model එකයි API Key එකයි Background එකට යැවීම
                custom_env = os.environ.copy()
                custom_env["GEMINI_API_KEY"] = api_key
                custom_env["GEMINI_MODEL"] = model_version

                result = subprocess.run(
                    command_input, 
                    shell=True, 
                    capture_output=True, 
                    text=True,
                    env=custom_env # අලුත් දත්ත ටික යවනවා
                )

                st.subheader("Output:")
                if result.stdout:
                    st.code(result.stdout, language="bash")
                else:
                    st.info("No output returned.")
                
                if result.stderr:
                    st.subheader("Errors / Warnings:")
                    st.error(result.stderr)
                    
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")
