import os
import re
import socket
import streamlit as st
from dotenv import load_dotenv

# Load local environment keys for local testing
load_dotenv()

# High-tier performance model parameters
CLOUD_MODEL = "llama-3.3-70b-versatile"

# Safely extract key from system or Streamlit Cloud Secrets management
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def extract_clean_code(text):
    code_blocks = re.findall(r'```python\s*(.*?)\s*```', text, re.DOTALL)
    if not code_blocks:
        code_blocks = re.findall(r'```\s*(.*?)\s*```', text, re.DOTALL)
    return code_blocks[0].strip() if code_blocks else text.strip()

# ==========================================================
# STREAMLIT UI DESIGN LAYOUT
# ==========================================================
st.set_page_config(page_title="Multi-Agent Coding Engine", page_icon="🤖", layout="wide")

st.title("🤖 Hybrid Multi-Agent Self-Correcting Coding Engine")
st.markdown("---")

# User Input Field
user_prompt = st.text_input("What would you like the AI Software Factory to build today?", 
                            placeholder="e.g., build a simple calculator or create a snake game")

if st.button("🚀 Trigger Agentic Pipeline", type="primary"):
    if not user_prompt:
        st.warning("Please enter a project prompt first!")
    elif not GROQ_API_KEY:
        st.error("Security Error: GROQ_API_KEY missing from environment variables.")
    else:
        from groq import Groq
        client = Groq(api_key=GROQ_API_KEY)
        
        # UI Status containers
        status_box = st.info("📡 Connecting to Groq Cloud Infrastructure cluster arrays...")
        
        try:
            # ==========================================================
            # STEP 1: DEVELOPER AGENT EXECUTION
            # ==========================================================
            status_box.info(f"💻 **Agent 1 (Developer):** Compiling first-pass logic matrices for '{user_prompt}'...")
            coding_prompt = f"Write a complete, working Python script for this exact task: '{user_prompt}'. Provide only the code wrapped in standard markdown triple backticks. Do not add casual conversation."
            
            dev_response = client.chat.completions.create(model=CLOUD_MODEL, messages=[{'role': 'user', 'content': coding_prompt}])
            initial_raw_text = dev_response.choices[0].message.content
            initial_code = extract_clean_code(initial_raw_text)
            
            # ==========================================================
            # STEP 2: REVIEWER AGENT EXECUTION
            # ==========================================================
            status_box.info("🔍 **Agent 2 (Reviewer):** Running structural optimization and syntax verification pass...")
            review_prompt = f"Analyze this Python code for bugs or syntax errors:\n{initial_code}\n\nIf perfect with zero flaws, reply with exactly one word: 'PERFECT'. Otherwise, list the bugs."
            
            reviewer_response = client.chat.completions.create(model=CLOUD_MODEL, messages=[{'role': 'user', 'content': review_prompt}])
            bug_report = reviewer_response.choices[0].message.content.strip()
            
            # ==========================================================
            # STEP 3: CONDITIONAL SELF-CORRECTION LOOP
            # ==========================================================
            if "PERFECT" in bug_report.upper() and len(bug_report) < 20:
                status_box.success("✨ **Agent 2 (Reviewer):** Code structure verified! Zero flaws isolated.")
                final_clean_code = initial_code
            else:
                status_box.warning("⚠️ **Agent 2 (Reviewer):** Structural anomalies detected! Generating error logs...")
                
                # Show bug logs to the user on screen
                with st.expander("Reviewer Feedback Logs"):
                    st.text(bug_report)
                
                status_box.info("🛠️ **Agent 1 (Developer):** Executing programmatic code self-correction refactoring pass...")
                fix_prompt = f"Fix this Python code based on the error report below:\nOriginal: {initial_code}\nErrors: {bug_report}\nReturn ONLY the finalized Python code block inside code fences."
                
                fix_response = client.chat.completions.create(model=CLOUD_MODEL, messages=[{'role': 'user', 'content': fix_prompt}])
                final_clean_code = extract_clean_code(fix_response.choices[0].message.content)
            
            # ==========================================================
            # STEP 4: TECHNICAL WRITER AGENT EXECUTION
            # ==========================================================
            status_box.info("📚 **Agent 3 (Technical Writer):** Designing clean markdown documentation profiles...")
            readme_prompt = f"Write a professional GitHub README.md markdown file for a project built around this user request: '{user_prompt}'. Document this clean code:\n\n{final_clean_code}"
            
            readme_response = client.chat.completions.create(model=CLOUD_MODEL, messages=[{'role': 'user', 'content': readme_prompt}])
            final_readme = readme_response.choices[0].message.content
            
            status_box.empty()
            st.success("🎉 Architecture Lifecycle Complete! Your dynamic project assets are ready.")
            
            # ==========================================================
            # UI ELEMENT DISPLAY GENERATED OUTPUTS TO VISITOR
            # ==========================================================
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("⚙️ Final Executable Code")
                st.code(final_clean_code, language="python")
                st.download_button("Download Python Code", data=final_clean_code, file_name="final_verified_code.py")
                
            with col2:
                st.subheader("📄 AI-Generated Project Documentation")
                st.markdown(final_readme)
                st.download_button("Download README.md", data=final_readme, file_name="README.md")
                
        except Exception as e:
            status_box.empty()
            st.error(f"❌ Pipeline Execution Crash: {e}")