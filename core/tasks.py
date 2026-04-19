from crewai import Task

def create_debug_tasks(code, coder, tester):
    code_task = Task(
        description=f"Analyze and fix the architecture and bugs in the following code. YOU MUST OUTPUT ONLY PURE EXECUTABLE PYTHON CODE, NO CHAT, NO EXPLANATIONS, NO MARKDOWN BACKTICKS:\n{code}",
        expected_output="Pure raw python code without backticks",
        agent=coder
    )
    test_task = Task(
        description=f"Write pytest tests for the code. STRICT: Import 'add' from 'homework'. YOU MUST OUTPUT ONLY PURE EXECUTABLE PYTHON CODE, NO CHAT, NO EXPLANATIONS, NO MARKDOWN BACKTICKS.\nCode: {code}",
        expected_output="Pure raw python code without backticks",
        agent=tester
    )
    return [code_task, test_task]

def create_analyze_tasks(code, coder, tester):
    analysis_task = Task(
        description=f"Perform a deep architectural review of this logic:\n{code}",
        expected_output="Vulnerability and optimization report",
        agent=coder
    )
    suggestion_task = Task(
        description="Provide a list of 5 concrete improvements for this code.",
        expected_output="Implementation roadmaps",
        agent=tester
    )
    return [analysis_task, suggestion_task]

def create_explain_tasks(code, coder):
    explain_task = Task(
        description=f"Explain exactly how this code works to a junior developer:\n{code}",
        expected_output="Simple, clear walkthrough with examples",
        agent=coder
    )
    return [explain_task]

def create_universal_debug_tasks(code, universal_agent):
    task = Task(
        description=f"""You are a senior multi-lingual debugging architect.
Analyze the following code, detect its language natively, and fix syntax, logic, runtime, and cross-execution bugs.

STRICT OUTPUT CONTROL PROMPT (Telegram Safe Mode):

1. HARD LIMIT RULE
- NEVER generate output longer than 3000 characters in a single response.
- If content is large, you MUST shorten it.

2. OUTPUT STRUCTURE (MANDATORY)
Always respond in this format:

1. 🔍 Summary (max 2-3 lines)
2. 🔧 Fixed Code (ONLY essential code, no extra explanation)
3. 💡 Key Issues (max 3-5 bullet points)

3. AUTO-COMPRESSION RULE
If the response is getting long:
- Remove unnecessary explanations
- Keep only: final fixed code, most important errors
- DO NOT include verbose reasoning

4. NO OVERFLOW POLICY
- DO NOT return full logs or full analysis dumps.
- DO NOT exceed safe message size. PRIORITIZE SHORT, USEFUL OUTPUT.

5. FAILSAFE
If still too large, respond ONLY with:
“📄 Output too large. Summary provided. Request ‘full report’ to receive file.”

Code to analyze:
{code}""",
        expected_output="Short Telegram-safe debug structure.",
        agent=universal_agent
    )
    return [task]