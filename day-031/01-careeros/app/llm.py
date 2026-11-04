"""Optional OpenAI-compatible provider adapter; deterministic mode is the default."""
import httpx
from .config import LLM_BASE_URL, LLM_API_KEY, LLM_MODEL

async def refine_plan(prompt: str):
    if not (LLM_BASE_URL and LLM_API_KEY and LLM_MODEL):
        return None
    url = LLM_BASE_URL if LLM_BASE_URL.endswith("/chat/completions") else LLM_BASE_URL + "/chat/completions"
    headers = {"Authorization": f"Bearer {LLM_API_KEY}", "Content-Type":"application/json"}
    payload = {"model":LLM_MODEL,"messages":[
        {"role":"system","content":"You are a cautious career planning assistant. Do not invent credentials, guarantee hiring outcomes, or claim skills are verified. Return concise actionable guidance."},
        {"role":"user","content":prompt}
    ],"temperature":0.2}
    async with httpx.AsyncClient(timeout=25) as client:
        response = await client.post(url,headers=headers,json=payload)
        response.raise_for_status()
        data=response.json()
        return data["choices"][0]["message"]["content"]
