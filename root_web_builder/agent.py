import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from google.adk.agents import SequentialAgent
from agents.req_writer.agent import requirements_writer_agent
from agents.designer.agent import designer_agent
from agents.code_writer.agent import coder_agent
from utils.file_loader import load_instructions_file

root_agent = SequentialAgent(
    name="root_web_builder_agent",
    description=load_instructions_file("agents/root_web_builder/description.txt"),
    sub_agents=[requirements_writer_agent,
                designer_agent,
                coder_agent]  
        # List of sub-agents to be executed in order
    )