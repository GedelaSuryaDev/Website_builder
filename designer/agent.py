import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from google.adk.agents import LlmAgent
from utils.file_loader import load_instructions_file


designer_agent = LlmAgent(
    name="designer_agent",
    model ="gemini-2.5-flash",
    description=load_instructions_file("agents/designer/description.txt"),
    instruction=load_instructions_file("agents/designer/instruction.txt"),
    output_key="designer_output"
)