import asyncio
import logging
import os
import PIL
import requests

from io import BytesIO
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import StructuredMessage
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient
from autogen_core.models import UserMessage
from autogen_core import EVENT_LOGGER_NAME
from autogen_agentchat.messages import MultiModalMessage
from autogen_core import Image

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(EVENT_LOGGER_NAME)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.ERROR)

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

# Define a tool that searches the web for information.
# For simplicity, we will use a mock function here that returns a static string.
async def web_search(query: str) -> str:
    """Find information on the web"""
    return "AutoGen is a programming framework for building multi-agent applications."

# Create an assistant agent that uses the model client and web search tool.
agent = AssistantAgent(
    name="assistant",
    model_client=model_client,
    tools=[web_search],
    system_message="Use tools to solve tasks.",
)

# Create a multi-modal message with random image and text.
# this is the image to be used in the multimodal message
pil_image = PIL.Image.open(BytesIO(requests.get("https://picsum.photos/300/200").content))
img = Image(pil_image)

# and here you creatte the multimodal message with the image
multi_modal_message = MultiModalMessage(content=["Can you describe the content of this image?", img], source="user")

# Run the agent and stream the messages to the console.
async def main() -> None:
    # Create a console UI to stream messages whitout agents, simply iuse the model_client and send a UserMessage
    print(" ======================================== ")
    print("Running the model directly...")
    print(" ======================================== ")
    result1 = await model_client.create([UserMessage(content="What is the capital of France?", source="user")])
    print(result1)

    # Here we run the agent with the console UI, this agent use a tool to search the web
    print(" ======================================== ")
    print("Running the agent...")
    print(" ======================================== ")
    result2 = await agent.run(task="Find information on AutoGen")
    length = len(result2.messages)
    print(f"The task returned {length} messages.")
    print(" ======================================== ")
    print(f"The task returned {result2.messages[length-1].to_text } messages.")
    print(result2.messages[-1].content)
    print(" ======================================== ")

    # and here we use the same agent but with a multimodal message with an image
    print("Running the multimodal agent...")
    result3 = await agent.run(task=multi_modal_message)
    print(" ======================================== ")
    length = len(result3.messages)
    print(f"The task returned {length} messages.")
    print(" ======================================== ")
    print(f"The task returned {result3.messages[length-1].to_text } messages.")
    print(result3.messages[-1].content)  # type: ignore

    await model_client.close()

# NOTE: if running this inside a Python script you'll need to use asyncio.run(main()).
asyncio.run(main())