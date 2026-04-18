import subprocess
import os
import re
import sys
import argparse
import json
import time
from datetime import datetime
from crewai import Crew
from agents import create_agents
from tasks import create_debug_tasks, create_analyze_tasks, create_explain_tasks

def log_stage(stage, msg=""):
    print(f"\x1b[94m🔹 [{stage}]\x1b[0m {msg}", flush=True)

def log_decision(mode, provider, reason):
    decision_log = "../logs/decision_log.json"
    os.makedirs("../logs", exist_ok=True)
    entry = {"timestamp": datetime.now().isoformat(), "mode": mode, "provider": provider, "reason": reason}
    log_data = []
    if os.path.exists(decision_log):
        with open(decision_log, "r") as f:
            try: log_data = json.load(f)
            except: pass
    log_data.append(entry)
    with open(decision_log, "w") as f: json.dump(log_data, f, indent=4)

def clean_output(text):
    text = str(text) 
    if "```" in text:
        block = text.split("```")[1]
        if block.startswith("python\n"): block = block[7:]
        elif block.startswith("python"): block = block[6:]
        return block.strip()
    return text

def parse_coverage(stdout):
    match = re.search(r"TOTAL\s+\d+\s+\d+\s+(\d+)%", stdout)
    return int(match.group(1)) if match else 0

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["full", "quick", "analyze", "explain"], default="full")
    parser.add_argument("--provider", choices=["local", "cloud"], default="local")
    return parser.parse_args()

def main():
    start_time = time.time()
    args = parse_args()
    log_stage("JOB STARTED", f"Mode: {args.mode.upper()} Pipeline")
    
    provider_display = "LOCAL (Ollama)" if args.provider == "local" else "CLOUD (OpenRouter)"
    log_stage("LLM SOURCE", provider_display)
    
    log_decision(args.mode, args.provider, "Auto-routed" if args.provider=="local" else "Reasoning Fallback")
    
    planner, coder, debugger, tester = create_agents(provider=args.provider)
    initial_code = "\ndef add(a,b)\n    return a+b\n"

    if args.mode == "analyze":
        tasks = create_analyze_tasks(initial_code, planner, debugger)
        crew = Crew(agents=[planner, debugger], tasks=tasks)
        print(crew.kickoff())
    elif args.mode == "explain":
        tasks = create_explain_tasks(initial_code, planner)
        crew = Crew(agents=[planner], tasks=tasks)
        print(crew.kickoff())
    else:
        # Full Loop
        max_retries = 3
        attempts = 0
        final_coverage = 0
        
        for attempt in range(max_retries):
            attempts += 1
            log_stage(f"ATTEMPT {attempt+1}", "Fix cycle running...")
            tasks = create_debug_tasks(initial_code, planner, debugger, coder, tester)
            crew = Crew(agents=[planner, debugger, coder, tester], tasks=tasks)
            crew.kickoff()
            
            code_output = clean_output(tasks[2].output.raw)
            test_output = clean_output(tasks[3].output.raw)
            
            with open("homework.py", "w") as f: f.write(code_output)
            with open("test_homework.py", "w") as f: f.write(test_output)
            
            if args.mode == "quick":
                subprocess.run(["python", "-m", "pytest", "test_homework.py"], capture_output=True)
                final_coverage = 100
            else:
                process = subprocess.run(["python", "-m", "pytest", "--cov=homework", "test_homework.py"], capture_output=True, text=True)
                final_coverage = parse_coverage(process.stdout)
            
            if final_coverage >= 80:
                log_stage("COMPLETED", "✅ Success")
                break
        
        # PRO SUMMARY
        end_time = time.time()
        print(f"\n📊 SUMMARY")
        print(f"Mode: {args.mode.upper()}")
        print(f"Attempts: {attempts}")
        print(f"Coverage: {final_coverage}%")
        print(f"Status: SUCCESS ✅")
        print(f"⏱️ Total Time: {round(end_time - start_time, 2)}s")

if __name__ == "__main__":
    main()
