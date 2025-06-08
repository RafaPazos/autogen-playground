import os
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.auth.azure import AzureTokenProvider
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient
from azure.identity import DefaultAzureCredential

load_dotenv()  # Loads variables from .env into environment
api_key = os.environ.get("AZURE_KEY")
if api_key is None:
    raise ValueError("AZURE_KEY environment variable is not set.")

project_name = os.environ.get("AZURE_ENDPOINT_NAME")

endpoint = f"https://{project_name}.openai.azure.com/"
model_name = "gpt-4.1-mini"
deployment = "gpt-4.1-mini"
api_version = "2024-12-01-preview"

model_client = AzureOpenAIChatCompletionClient(
    azure_deployment=deployment,
    model=model_name,
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=api_key
)

# Define a simple function tool that the agent can use.
# For this example, we use a fake weather tool for demonstration purposes.
async def get_weather(city: str) -> str:
    """Get the weather for a given city."""
    return f"The weather in {city} is 73 degrees and Sunny."


# Define an AssistantAgent with the model, tool, system message, and reflection enabled.
# The system message instructs the agent via natural language.
agent = AssistantAgent(
    name="weather_agent",
    model_client=model_client,
    tools=[get_weather],
    system_message="You are a helpful assistant.",
    reflect_on_tool_use=True,
    model_client_stream=True,  # Enable streaming tokens from the model client.
)