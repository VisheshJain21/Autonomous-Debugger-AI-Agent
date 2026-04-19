from crewai import Agent, LLM
import os

def get_llm(model_name="deepseek-coder", provider="local"):
    if provider == "cloud":
        return LLM(
            model="openrouter/google/gemini-2.5-flash",
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"),
            max_tokens=1000,
            timeout=10
        )
    return LLM(
        model=f"ollama/{model_name}",
        base_url="http://localhost:11434",
        max_tokens=1000,
        timeout=10
    )

def create_agents(provider="local"):
    shared_llm = get_llm("deepseek-coder", provider)
    
    coder = Agent(
        role="Coder",
        goal="Write and fix Python code. ONLY output valid Python.",
        backstory="Expert Python Engineer. No markdown, no explanations.",
        llm=shared_llm,
        verbose=False
    )
    tester = Agent(
        role="Tester",
        goal="Implement strict pytest suites. ONLY output valid Python.",
        backstory="QA Lead. No markdown, no stories, pure code.",
        llm=shared_llm,
        verbose=False
    )
    return coder, tester