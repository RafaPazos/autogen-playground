import asyncio
import logging
import os
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_core import EVENT_LOGGER_NAME
from agentchat_key_quickstart import agent, model_client

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(EVENT_LOGGER_NAME)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)
# main.py

# Run the agent and stream the messages to the console.
async def main() -> None:
    # Load the environment variables from the .env file.
    load_dotenv()  # Loads variables from .env into environment

    await Console(agent.run_stream(task="What is the weather in New York?"))
    # Close the connection to the model client.
    await model_client.close()


# NOTE: if running this inside a Python script you'll need to use asyncio.run(main()).
asyncio.run(main())