import os
# Force CPU mode to avoid the CUDA crash loop
os.environ["OLLAMA_LLM_LIBRARY"] = "cpu_avx2"  

import ollama
import re

# Helper function to extract ONLY python code blocks from the AI text
def extract_clean_code(text):
    code_blocks = re.findall(r'```python\s*(.*?)\s*```', text, re.DOTALL)
    if not code_blocks:
        code_blocks = re.findall(r'```\s*(.*?)\s*```', text, re.DOTALL)
    return code_blocks[0].strip() if code_blocks else text.strip()

print("====================================================")
print("🤖 Welcome to the Dynamic Self-Correcting AI Coding Assistant 🤖")
print("====================================================\n")

# 1. Ask the user dynamically what they want to build
user_prompt = input("What would you like me to build today? (e.g., 'build a simple calculator'): ")

print("\n🚀 Connecting to Ollama server...")

try:
    # ==========================================
    # STEP 2: AGENT 1 WRITES THE INITIAL CODE
    # ==========================================
    print(f"\n💻 Agent 1 (Developer): Generating initial code for: '{user_prompt}'...")
    coding_prompt = f"Write a complete, working Python script for this exact task: '{user_prompt}'. Provide only the code wrapped in standard markdown triple backticks. Do not add casual conversation."

    dev_response = ollama.chat(
        model='llama3', 
        messages=[{'role': 'user', 'content': coding_prompt}]
    )
    initial_raw_text = dev_response['message']['content']
    initial_code = extract_clean_code(initial_raw_text)

    # Save the first draft code to a file
    with open("initial_draft_code.py", "w", encoding="utf-8") as f:
        f.write(initial_code)
    print("Code blocks isolated! Saved first draft to 'initial_draft_code.py'")

    # ==========================================
    # STEP 3: AGENT 2 VERIFIES AND FINDS BUGS
    # ==========================================
    print("\n🔍 Agent 2 (Reviewer): Verifying code quality, bugs, and errors...")
    review_prompt = f"""
    Analyze this Python code. Check for syntax errors, logical bugs, or missing blocks.
    
    Code to analyze:
    {initial_code}
    
    If the code is completely functional and correct, reply with exactly one word: 'PERFECT'.
    Otherwise, clearly list what needs to be fixed.
    """

    reviewer_response = ollama.chat(
        model='llama3', 
        messages=[{'role': 'user', 'content': review_prompt}]
    )
    bug_report = reviewer_response['message']['content'].strip()

    # ==========================================
    # STEP 4: CONDITIONAL SELF-CORRECTION LOOP
    # ==========================================
    if "PERFECT" in bug_report.upper() and len(bug_report) < 20:
        print("✨ Agent 2 (Reviewer): Code verified! Absolutely zero errors found.")
        final_clean_code = initial_code
    else:
        print("\n⚠️ Agent 2 (Reviewer): Issues detected. Generating error logs...")
        print("----------------------------------------------------")
        print(bug_report)
        print("----------------------------------------------------")
        
        print("\n🛠️ Agent 1 (Developer): Refactoring code based on reviewer logs...")
        fix_prompt = f"""
        Fix this Python code based on the error report below. 
        Original Code:
        {initial_code}
        
        Error Report:
        {bug_report}
        
        Return ONLY the finalized, executable Python code block wrapped inside code fences.
        """
        
        fix_response = ollama.chat(
            model='llama3', 
            messages=[{'role': 'user', 'content': fix_prompt}]
        )
        final_clean_code = extract_clean_code(fix_response['message']['content'])

    # Save the final, verified code
    with open("final_verified_code.py", "w", encoding="utf-8") as f:
        f.write(final_clean_code)
    print("✅ Final executable code saved to 'final_verified_code.py'!")

    # ==========================================
    # STEP 5: AGENT 3 GENERATES THE README DOCUMENTATION
    # ==========================================
    print("\n📚 Agent 3 (Technical Writer): Compiling professional project documentation...")
    readme_prompt = f"Write a professional GitHub README.md markdown file for a project built around this user request: '{user_prompt}'. Document this clean code:\n\n{final_clean_code}"

    readme_response = ollama.chat(
        model='llama3', 
        messages=[{'role': 'user', 'content': readme_prompt}]
    )
    final_readme = readme_response['message']['content']

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(final_readme)

    print("\n🎉 Process complete! Your dynamic project is ready.")

except Exception as e:
    print("\n❌ CRITICAL ERROR: The script couldn't get a proper answer from the Ollama app.")
    print(f"Error details: {e}")
    print("Please make sure your other command prompt window running 'ollama serve' hasn't closed!")