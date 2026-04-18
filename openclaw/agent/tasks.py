from crewai import Task

def create_debug_tasks(code, planner, debugger, coder, tester):
    plan_task = Task(
        description=f"Analyze for architectural bugs:\n{code}",
        expected_output="Detailed bug list",
        agent=planner
    )
    debug_task = Task(
        description="Write specific fixes for found bugs.",
        expected_output="Patches",
        agent=debugger
    )
    code_task = Task(
        description="Rebuild code with fixes.",
        expected_output="Fixed python code",
        agent=coder
    )
    test_task = Task(
        description=f"Write pytest tests. STRICT: Import 'add' from 'homework'.\nCode: {code}",
        expected_output="Pytest code",
        agent=tester
    )
    return [plan_task, debug_task, code_task, test_task]

def create_analyze_tasks(code, planner, debugger):
    analysis_task = Task(
        description=f"Perform a deep architectural review of this logic:\n{code}",
        expected_output="Vulnerability and optimization report",
        agent=planner
    )
    suggestion_task = Task(
        description="Provide a list of 5 concrete improvements for this code.",
        expected_output="Implementation roadmaps",
        agent=debugger
    )
    return [analysis_task, suggestion_task]

def create_explain_tasks(code, planner):
    explain_task = Task(
        description=f"Explain exactly how this code works to a junior developer:\n{code}",
        expected_output="Simple, clear walkthrough with examples",
        agent=planner
    )
    return [explain_task]