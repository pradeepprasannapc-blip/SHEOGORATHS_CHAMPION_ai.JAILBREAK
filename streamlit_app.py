import streamlit as st
import subprocess
import os

st.set_page_config(page_title="CLI to Streamlit", page_icon="⚙️")
st.title("⚙️ CLI to Streamlit Converter")

# --- අලුත් Settings මෙනුව ---
st.sidebar.header("⚙️ Settings")
api_key = st.sidebar.text_input("Gemini API Key:", type="password", help="ඔබගේ API Key එක මෙහි ලබාදෙන්න.")

# නොමිලේ වැඩ කරන අලුත්ම මාදිලි ලැයිස්තුව
model_version = st.sidebar.selectbox(
    "Select Gemini Model:", 
    [
        "gemini-2.5-flash",       # දැනට නොමිලේ වැඩ කරන ප්‍රධාන මාදිලිය
        "gemini-2.5-flash-lite",  # ඉතා වේගවත් සහ සැහැල්ලු මාදිලිය
        "gemini-3.1-pro",         # අලුත්ම Preview මාදිලිය
    ] 
)

st.markdown("මෙමගින් ඔබට Command-line එකෙහි run කරන ඕනෑම command එකක් මෙහි run කරගත හැක.")

command_input = st.text_input("Enter your command here:", value="python examples/api_usage.py")

if st.button("Run Command", type="primary"):
    if not api_key:
        st.warning("⚠️ කරුණාකර වම් පස ඇති Settings මෙනුවෙන් API Key එක ලබා දෙන්න.")
    elif command_input:
        with st.spinner("Running command... Please wait."):
            try:
                custom_env = os.environ.copy()
                custom_env["GEMINI_API_KEY"] = api_key
                custom_env["GEMINI_MODEL"] = model_version

                result = subprocess.run(
                    command_input, 
                    shell=True, 
                    capture_output=True, 
                    text=True,
                    env=custom_env
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
