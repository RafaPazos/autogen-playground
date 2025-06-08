import asyncio
import os
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.base import TaskResult
from autogen_agentchat.conditions import ExternalTermination, TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_core import CancellationToken
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient

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
    api_key=api_key,
)

# Create the primary agent.


# Create the critic agent.

# Define a termination condition that stops the task if the critic approves.

# Create a team with the primary and critic agents.

# NOTE: if running this inside a Python script you'll need to use asyncio.run(main()).
asyncio.run(main())