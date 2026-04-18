from crewai import Agent, LLM
import os

def get_llm(provider="local"):
    if provider == "cloud":
        # OpenRouter Integration via CrewAI native OpenAI-compatible LLM
        return LLM(
            model="openrouter/anthropic/claude-3-haiku",
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY")
        )
    else:
        # High-performance local routing
        return LLM(model="ollama/qwen2.5-coder", base_url="http://localhost:11434")

def create_agents(provider="local"):
    shared_llm = get_llm(provider)

    planner = Agent(
        role="Planner",
        goal="Analyze the codebase and predict architectural failures.",
        backstory="Senior Solutions Architect",
        llm=shared_llm
    )

    coder = Agent(
        role="Coder",
        goal="Write optimize, secure, and production-ready Python code.",
        backstory="Expert Software Engineer",
        llm=shared_llm
    )

    debugger = Agent(
        role="Debugger",
        goal="Identify complex logic bugs and provide minimal patches.",
        backstory="Security Researcher & Debugging Expert",
        llm=shared_llm
    )

    tester = Agent(
        role="Tester",
        goal="Implement strict pytest suites with high logic coverage.",
        backstory="QA Automation Lead",
        llm=shared_llm
    )

    return planner, coder, debugger, tester