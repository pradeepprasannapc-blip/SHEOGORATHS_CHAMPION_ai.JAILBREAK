import streamlit as st
import subprocess

st.set_page_config(page_title="CLI to Streamlit", page_icon="⚙️")

st.title("⚙️ CLI to Streamlit Converter")
st.markdown("මෙමගින් ඔබට Command-line එකෙහි run කරන ඕනෑම command එකක් (උදා: `python main.py --arg1 value1`) මෙහි run කරගත හැක.")

# Command එක ඇතුලත් කිරීමට text box එකක්
command_input = st.text_input("Enter your command here:", placeholder="e.g., python main.py --help")

# Run button එක
if st.button("Run Command", type="primary"):
    if command_input:
        with st.spinner("Running command... Please wait."):
            try:
                # Subprocess හරහා command එක run කිරීම
                result = subprocess.run(
                    command_input, 
                    shell=True, 
                    capture_output=True, 
                    text=True
                )

                # Output එක පෙන්වීම
                st.subheader("Output:")
                if result.stdout:
                    st.code(result.stdout, language="bash")
                else:
                    st.info("No output returned.")
                
                # Error එකක් ආවොත් ඒක පෙන්වීම
                if result.stderr:
                    st.subheader("Errors / Warnings:")
                    st.error(result.stderr)
                    
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")
    else:
        st.warning("Please enter a command before clicking Run.")
