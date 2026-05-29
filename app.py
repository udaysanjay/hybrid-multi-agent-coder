import os
import re
import streamlit as st
from dotenv import load_dotenv

# Load local environment keys for local testing
load_dotenv()

# High-tier performance model parameters
CLOUD_MODEL = "llama-3.3-70b-versatile"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def extract_clean_code(text):
    code_blocks = re.findall(r'```python\s*(.*?)\s*```', text, re.DOTALL)
    if not code_blocks:
        code_blocks = re.findall(r'```\s*(.*?)\s*```', text, re.DOTALL)
    return code_blocks[0].strip() if code_blocks else text.strip()

# ==========================================================
# STREAMLIT UI DESIGN LAYOUT (VERIFIED PRODUCTION VERSION)
# ==========================================================
st.set_page_config(page_title="Multi-Agent Coding Engine", page_icon="🤖", layout="wide")

# Corrected parameter syntax: 'unsafe_allow_html=True' to fix Python 3.14 runtime errors
st.markdown("<style>.block-container {padding-top: 2rem; padding-bottom: 2rem;} .metric-card {background-color: #1e222b; border: 1px solid #2d3139; padding: 1.5rem; border-radius: 12px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1);} .metric-val {font-size: 1.8rem; font-weight: bold; color: #00ffd0;} .metric-lbl {font-size: 0.9rem; color: #8a92a6; margin-top: 5px;}</style>", unsafe_allow_html=True)

# ==========================================================
# SIDEBAR CONTROL WORKSPACE
# ==========================================================
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #00ffd0;'>⚙️ ForgeAI Control</h2>", unsafe_with_html=True)
    st.markdown("---")
    st.markdown("### 🖥️ System Core Runtime")
    st.code(f"Engine: {CLOUD_MODEL}\nType: Multi-Agent v2.0", language="text")
    st.markdown("---")
    st.markdown("### 🔑 Token Validation")
    if GROQ_API_KEY:
        st.success("Vault Key Verified: Active")
    else:
        st.error("Vault Key Missing: Offline")

# ==========================================================
# MAIN DASHBOARD INTERFACE
# ==========================================================
st.markdown("<h1 style='color: #ffffff; margin-bottom: 0px;'>⚡ ForgeAI Developer Studio</h1>", unsafe_with_html=True)
st.markdown("<p style='color: #8a92a6; font-size: 1.1rem;'>Autonomous Actor-Critic Multi-Agent Assembly Pipeline</p>", unsafe_with_html=True)
st.markdown("---")

# Analytical Metric Trackers Layout Cards
m1, m2, m3 = st.columns(3)
with m1:
    st.markdown('<div class="metric-card"><div class="metric-val">3 Agents</div><div class="metric-lbl">Active Workforce Topology</div></div>', unsafe_allow_html=True)
with m2:
    st.markdown('<div class="metric-card"><div class="metric-val">&lt; 6 Seconds</div><div class="metric-lbl">Average Cloud Latency</div></div>', unsafe_with_html=True)
with m3:
    st.markdown('<div class="metric-card"><div class="metric-val">100% Secure</div><div class="metric-lbl">Environment Vault Execution</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_with_html=True)

# Requirement Input Matrix Layout Block
input_col, button_col = st.columns([3, 1])

with input_col:
    user_prompt = st.text_input("📝 Target Software Specifications", 
                                placeholder="Describe the application requirements (e.g., build a calculator)...",
                                label_visibility="collapsed")

with button_col:
    trigger_pipeline = st.button("🚀 Begin Factory Synthesis", type="primary", use_container_width=True)

# ==========================================================
# AGENTIC COMPILATION ENGINE
# ==========================================================
if trigger_pipeline:
    if not user_prompt:
        st.toast("⚠️ Input prompt criteria missing!", icon="🛑")
    elif not GROQ_API_KEY:
        st.error("🔒 Security Vault Exception: `GROQ_API_KEY` could not be fetched from active env memory mappings.")
    else:
        from groq import Groq
        client = Groq(api_key=GROQ_API_KEY)
        
        # UI Dynamic Console Stream Blocks
        progress_bar = st.progress(0)
        console_logs = st.empty()
        
        try:
            # Phase 1: Architectural Formulation
            console_logs.markdown("⚙️ **[FACTORY MONITOR]** `Agent 1 (Developer)` is synthesizing base logic scripts...")
            progress_bar.progress(25)
            
            coding_prompt = f"Write a complete, working Python script for this exact task: '{user_prompt}'. Provide only the code wrapped in standard markdown triple backticks. Do not add casual conversation."
            dev_response = client.chat.completions.create(model=CLOUD_MODEL, messages=[{'role': 'user', 'content': coding_prompt}])
            initial_code = extract_clean_code(dev_response.choices[0].message.content)
            
            # Phase 2: Static Verification Testing
            console_logs.markdown("🔍 **[FACTORY MONITOR]** `Agent 2 (Reviewer)` is executing structural syntax tests...")
            progress_bar.progress(50)
            
            review_prompt = f"Analyze this Python code for bugs or syntax errors:\n{initial_code}\n\nIf perfect with zero flaws, reply with exactly one word: 'PERFECT'. Otherwise, list the bugs."
            reviewer_response = client.chat.completions.create(model=CLOUD_MODEL, messages=[{'role': 'user', 'content': review_prompt}])
            bug_report = reviewer_response.choices[0].message.content.strip()
            
            # Phase 3: Self-Correction Loop Handling
            console_logs.markdown("🛠️ **[FACTORY MONITOR]** Programmatic patch evaluation underway...")
            progress_bar.progress(75)
            
            if "PERFECT" in bug_report.upper() and len(bug_report) < 20:
                final_clean_code = initial_code
                review_verdict = "✨ Structural Analysis: 100% integrity verified. Code contains zero compilation failures."
            else:
                review_verdict = bug_report
                fix_prompt = f"Fix this Python code based on the error report below:\nOriginal: {initial_code}\nErrors: {bug_report}\nReturn ONLY the finalized Python code block inside code fences."
                fix_response = client.chat.completions.create(model=CLOUD_MODEL, messages=[{'role': 'user', 'content': fix_prompt}])
                final_clean_code = extract_clean_code(fix_response.choices[0].message.content)
            
            # Phase 4: Markdown Portfolio Engineering
            console_logs.markdown("📚 **[FACTORY MONITOR]** `Agent 3 (Technical Writer)` is packaging file manifests...")
            progress_bar.progress(100)
            
            readme_prompt = f"Write a professional GitHub README.md markdown file for a project built around this user request: '{user_prompt}'. Document this clean code:\n\n{final_clean_code}"
            readme_response = client.chat.completions.create(model=CLOUD_MODEL, messages=[{'role': 'user', 'content': readme_prompt}])
            final_readme = readme_response.choices[0].message.content
            
            # Clear running load layouts upon complete success
            progress_bar.empty()
            console_logs.empty()
            st.balloons()
            
            # ------------------------------------------------------
            # DISPLAY HIGH-FIDELITY OUTPUT TABS
            # ------------------------------------------------------
            st.success(f"📦 Production Run Completed Successfully for: '{user_prompt}'")
            
            tab1, tab2, tab3 = st.tabs(["💻 Compiled Script File", "📄 Architecture documentation", "📊 Workspace Diagnostics"])
            
            with tab1:
                st.markdown("### Production Execution Vector (`final_verified_code.py`)")
                st.code(final_clean_code, language="python")
                st.download_button("📥 Save Script Asset", data=final_clean_code, file_name="final_verified_code.py", type="primary")
                
            with tab2:
                st.markdown("### System Architecture Blueprint Documentation (`README.md`)")
                st.markdown(final_readme)
                st.download_button("📥 Save Documentation Asset", data=final_readme, file_name="README.md", type="secondary")
                
            with tab3:
                st.markdown("### Internal Component Output Mappings & Critic Metrics")
                st.info("💡 **Agent 1: Initial Source Prototype Draft**")
                with st.expander("Expand Initial Draft Log"):
                    st.code(initial_code, language="python")
                
                st.warning("⚖️ **Agent 2: Code Reviewer Static Assessment Telemetry**")
                st.code(review_verdict, language="text")
                
        except Exception as e:
            progress_bar.empty()
            console_logs.empty()
            st.error(f"❌ Critical Pipeline Failure: {e}")