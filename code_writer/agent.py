import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from google.adk.agents import LlmAgent
from tools.file_writer_tool import write_to_file
from utils.file_loader import load_instructions_file


coder_agent = LlmAgent(
    name="coder_agent",
    model ="gemini-2.5-flash",
    description=load_instructions_file("agents/coder/description.txt"),
    instruction=load_instructions_file("agents/coder/instruction.txt"),
    tools = [write_to_file]
)