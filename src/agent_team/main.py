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
primary_agent = AssistantAgent(
    "primary",
    model_client=model_client,
    system_message="You are a helpful AI assistant.",
)

## Create the jokes agent, this is optional and shown how the interaction between agents may provide quite unexpected results
##jokes_agent = AssistantAgent(
##    "jokes",
##    model_client=model_client,
##    system_message="You are a funny AI assistant that don't like poems but makes funny comments on them.",
##)

# Create the critic agent.
critic_agent = AssistantAgent(
    "critic",
    model_client=model_client,
    system_message="Provide constructive feedback. Respond with 'APPROVE' to when your feedbacks are addressed.",
)

# Define a termination condition that stops the task if the critic approves.
text_termination = TextMentionTermination("APPROVE")

# Create a team with the primary and critic agents.
team = RoundRobinGroupChat([primary_agent, critic_agent], termination_condition=text_termination)

## adding the jokes agent makes the team more fun and interesting, you don't even know how the whole thing will end up.
## team = RoundRobinGroupChat([primary_agent, jokes_agent,critic_agent], termination_condition=text_termination)

async def main() -> None:
    await team.reset()  # Reset the team for a new task.
    await Console(team.run_stream(task="Write a short poem about the fall season."))  # Stream the messages to the console.

# NOTE: if running this inside a Python script you'll need to use asyncio.run(main()).
asyncio.run(main())