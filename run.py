import os
import re
import socket
from dotenv import load_dotenv

# 1. Load the hidden variables from your local .env file
load_dotenv()

# Force CPU fallback rules to prevent local CUDA crashes
os.environ["OLLAMA_LLM_LIBRARY"] = "cpu_avx2"  

# 2. Secretly pull the API key from your computer's memory
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# High-tier performance model parameters
CLOUD_MODEL = "llama-3.3-70b-versatile"
LOCAL_MODEL = "llama3"

def is_online():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

def extract_clean_code(text):
    code_blocks = re.findall(r'```python\s*(.*?)\s*```', text, re.DOTALL)
    if not code_blocks:
        code_blocks = re.findall(r'```\s*(.*?)\s*```', text, re.DOTALL)
    return code_blocks[0].strip() if code_blocks else text.strip()

print("================================================================")
print("🤖 Welcome to the Hybrid Smart-Routing Multi-Agent Coding Engine 🤖")
print("================================================================\n")

# Verify API key placement before attempting execution
if is_online() and not GROQ_API_KEY:
    print("❌ SECURITY ERROR: GROQ_API_KEY not found inside your hidden .env file!")
    print("Please create a .env file and add your key: GROQ_API_KEY=your_key")
    exit()

ONLINE_STATUS = is_online()

if ONLINE_STATUS:
    from groq import Groq
    print("📡 Network Status: ONLINE")
    print(f"⚡ Routing architecture to Groq Cloud Infrastructure ({CLOUD_MODEL})...")
    client = Groq(api_key=GROQ_API_KEY)
else:
    import ollama
    print("🔌 Network Status: OFFLINE")
    print(f"🏠 Routing architecture to local storage via Ollama Engine ({LOCAL_MODEL})...")
    print("👉 Make sure your background 'ollama serve' window is currently open!")

user_prompt = input("\nWhat would you like me to build today? (e.g., 'build a simple calculator'): ")

try:
    # ==========================================================
    # STEP 1: AGENT 1 WRITES THE INITIAL CODE
    # ==========================================================
    print(f"\n💻 Agent 1 (Developer): Compiling first-pass logic matrices...")
    coding_prompt = f"Write a complete, working Python script for this exact task: '{user_prompt}'. Provide only the code wrapped in standard markdown triple backticks. Do not add casual conversation."

    if ONLINE_STATUS:
        response = client.chat.completions.create(model=CLOUD_MODEL, messages=[{'role': 'user', 'content': coding_prompt}])
        initial_raw_text = response.choices[0].message.content
    else:
        response = ollama.chat(model=LOCAL_MODEL, messages=[{'role': 'user', 'content': coding_prompt}])
        initial_raw_text = response['message']['content']
        
    initial_code = extract_clean_code(initial_raw_text)

    # ==========================================================
    # STEP 2: AGENT 2 VERIFIES AND FINDS BUGS
    # ==========================================================
    print("\n🔍 Agent 2 (Reviewer): Running structural optimization pass...")
    review_prompt = f"Analyze this Python code for bugs or syntax errors:\n{initial_code}\n\nIf perfect with zero flaws, reply with exactly one word: 'PERFECT'. Otherwise, list the bugs."

    if ONLINE_STATUS:
        response = client.chat.completions.create(model=CLOUD_MODEL, messages=[{'role': 'user', 'content': review_prompt}])
        bug_report = response.choices[0].message.content.strip()
    else:
        response = ollama.chat(model=LOCAL_MODEL, messages=[{'role': 'user', 'content': review_prompt}])
        bug_report = response['message']['content'].strip()

    # ==========================================================
    # STEP 3: CONDITIONAL SELF-CORRECTION LOOP
    # ==========================================================
    if "PERFECT" in bug_report.upper() and len(bug_report) < 20:
        print("✨ Agent 2 (Reviewer): Code structure verified! Zero execution errors isolated.")
        final_clean_code = initial_code
    else:
        print("\n⚠️ Agent 2 (Reviewer): Execution warning anomalies found. Compiling error logs...")
        print("\n🛠️ Agent 1 (Developer): Programmatically refactoring code baseline parameters...")
        fix_prompt = f"Fix this Python code based on the error report below:\nOriginal: {initial_code}\nErrors: {bug_report}\nReturn ONLY the finalized Python code block inside code fences."
        
        if ONLINE_STATUS:
            response = client.chat.completions.create(model=CLOUD_MODEL, messages=[{'role': 'user', 'content': fix_prompt}])
            final_clean_code = extract_clean_code(response.choices[0].message.content)
        else:
            response = ollama.chat(model=LOCAL_MODEL, messages=[{'role': 'user', 'content': fix_prompt}])
            final_clean_code = extract_clean_code(response['message']['content'])

    # ==========================================================
    # STEP 4: AGENT 3 GENERATES THE README DOCUMENTATION
    # ==========================================================
    print("\n📚 Agent 3 (Technical Writer): Designing clean markdown documentation profiles...")
    readme_prompt = f"Write a professional GitHub README.md markdown file for a project built around this user request: '{user_prompt}'. Document this clean code:\n\n{final_clean_code}"

    if ONLINE_STATUS:
        response = client.chat.completions.create(model=CLOUD_MODEL, messages=[{'role': 'user', 'content': readme_prompt}])
        final_readme = response.choices[0].message.content
    else:
        response = ollama.chat(model=LOCAL_MODEL, messages=[{'role': 'user', 'content': readme_prompt}])
        final_readme = response['message']['content']

    # ==========================================================
    # STEP 5: ISOLATE CODE ELEMENTS INTO DYNAMIC LOCAL DIRECTORIES
    # ==========================================================
    folder_name = user_prompt.replace(" ", "_").lower()
    folder_name = re.sub(r'[^a-zA-Z0-9_]', '', folder_name)

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    with open(f"{folder_name}/initial_draft_code.py", "w", encoding="utf-8") as f:
        f.write(initial_code)
    with open(f"{folder_name}/final_verified_code.py", "w", encoding="utf-8") as f:
        f.write(final_clean_code)
    with open(f"{folder_name}/README.md", "w", encoding="utf-8") as f:
        f.write(final_readme)

    print("\n================================================================")
    print("🎉 ARCHITECTURE LIFECYCLE COMPLETE: GENERATED ENGINE ASSETS STORED.")
    print(f"📁 Isolated Project Location: /{folder_name}")
    print("================================================================")

except Exception as e:
    print(f"\n❌ PIPELINE CRASH DETECTED: {e}")