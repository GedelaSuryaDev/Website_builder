# ADK Agents Suite

A collection of AI agents built with the Google ADK Agents framework. This repo is organized for composing multiple task-focused agents (e.g., content, media, research) that can be orchestrated together or used standalone.

## Features
- Modular agent design using `LlmAgent`
- Tool-first approach for reliable actions (search, image ops, I/O)
- Ready to integrate into larger multi-agent systems

## Structure
- `agents/` (this folder): repository root
  - `.gitignore` – ignores caches, build artifacts, and virtual envs
  - `requirements.txt` – minimal dependencies to run typical agents
  - Add your agent modules and tools alongside this file

## Getting Started
```powershell
# Clone the repo
git clone https://github.com/GedelaSuryaDev/Website_builder.git
cd Website_builder

# Create & activate a virtual environment (Windows PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

## Usage
- Create an agent in a module (e.g., `my_agent.py`) that imports `LlmAgent` and any tools you need.
- Example (pseudo-code):
```python
from google.adk.agents import LlmAgent
from google.adk.tools import google_search

my_agent = LlmAgent(
    name="demo_agent",
    model="gemini-2.5-flash",
    description="Demo agent",
    instruction="Use google_search to answer the query concisely.",
    tools=[google_search]
)

# In your runtime/orchestrator
# result = my_agent.run("Find top resources for X")
# print(result)
```

## Website Builder: Multi-Agent Sequential Workflow
This project includes a multi-agent system that uses a sequential workflow to create a website. It contains three agents in the pipeline:

1) Requirement Agent (Business Analyst)
   - Takes high-level user inputs about the website and produces complete, structured requirements.
   - Acts like a business analyst to clarify scope, features, pages, and constraints.

2) Designer Agent
   - Consumes the output from the Requirement Agent.
   - Produces design artifacts (e.g., layout suggestions, component structure, styles) for the website.

3) Coder Agent
   - Consumes the Designer Agent output and cross-checks the Requirement Agent output.
   - Generates code for frontend, backend, or both, based on user needs.

Utilities
- These agents use tools from the `tools/` folder and shared utilities from the `utils/` folder.

## Development Notes
- Keep credentials out of source (use env vars or a secrets manager)
- Add project-specific ignores to `.gitignore`
- Pin dependency versions when moving to production
