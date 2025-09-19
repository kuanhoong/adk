from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm 

AGENT_MODEL="ollama/gemma3" 

root_agent = Agent(
    name="question_answer_agent", # Required: Unique agent name
    model=LiteLlm(AGENT_MODEL), # Required: Specify the LLM 
    description="A helpful assistant agent that can answer travel related questions.",
    instruction="You are a travel agent assistant that able to provide relevant travel information.",
)
