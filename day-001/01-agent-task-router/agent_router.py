from dataclasses import dataclass

@dataclass
class AgentResult:
    agent: str
    answer: str

def route(task: str) -> str:
    text = task.lower()
    if any(x in text for x in ("sql", "database", "query")):
        return "data_agent"
    if any(x in text for x in ("lead", "sales", "campaign", "crm")):
        return "gtm_agent"
    if any(x in text for x in ("api", "endpoint", "backend")):
        return "api_agent"
    return "general_agent"

def run_agent(agent: str, task: str) -> AgentResult:
    answers = {
        "data_agent": "Analyze the data model, query, and validation requirements.",
        "gtm_agent": "Identify the buyer, qualify the lead, and propose the next sales action.",
        "api_agent": "Design the endpoint contract, validation, errors, and integration flow.",
        "general_agent": "Break the task into context, reasoning, execution, and verification steps.",
    }
    return AgentResult(agent, f"{answers[agent]} Task: {task}")

if __name__ == "__main__":
    task = input("Task: ").strip()
    agent = route(task)
    result = run_agent(agent, task)
    print(f"\nRouted to: {result.agent}\n{result.answer}")
