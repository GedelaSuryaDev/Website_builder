import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from google.adk.agents import LlmAgent
from utils.file_loader import load_instructions_file


requirements_writer_agent = LlmAgent(
    name="requirements_writer",
    model ="gemini-2.5-flash",
    description=load_instructions_file("agents/req_writer/description.txt"),
    instruction=load_instructions_file("agents/req_writer/instruction.txt"),
    output_key="requirements_writer_output"
)