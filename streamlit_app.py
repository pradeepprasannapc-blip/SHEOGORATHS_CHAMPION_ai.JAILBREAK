import streamlit as st
import subprocess
import os

st.set_page_config(page_title="CLI to Streamlit", page_icon="⚙️")
st.title("⚙️ CLI to Streamlit Converter")

# --- අලුත් Settings මෙනුව (වම් පැත්තේ) ---
st.sidebar.header("⚙️ Settings")
api_key = st.sidebar.text_input("Gemini API Key:", type="password", help="ඔබගේ API Key එක මෙහි ලබාදෙන්න.")

# අලුත්ම මාදිලි (Models) ලැයිස්තුව
model_version = st.sidebar.selectbox(
    "Select Gemini Model:", 
    [
        "gemini-2.0-flash",       # අලුත්ම සහ වේගවත්ම (නිර්දේශිතයි)
        "gemini-2.0-pro-exp",     # 2.0 Pro අත්හදාබැලීමේ මාදිලිය
        "gemini-1.5-flash", 
        "gemini-1.5-pro",
        "gemini-1.5-flash-8b"
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
                # UI එකෙන් තෝරපු අලුත් Model එකයි API Key එකයි Background එකට යැවීම
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
