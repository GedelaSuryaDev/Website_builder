# Website Builder - Multi-Agent System

An intelligent website creation system powered by Google ADK Agents framework. This system uses a sequential workflow of specialized AI agents to transform user requirements into complete, functional websites.

## 🚀 Overview

The Website Builder employs three specialized agents working in sequence:

1. **Requirements Agent** (Business Analyst)
   - Analyzes user input and generates comprehensive website requirements
   - Defines scope, features, pages, technical constraints, and business logic
   - Output: Structured requirements document

2. **Designer Agent** (UI/UX Designer)  
   - Creates design specifications based on requirements
   - Generates layout suggestions, component structure, styling guidelines
   - Output: Design artifacts and component specifications

3. **Coder Agent** (Full-Stack Developer)
   - Implements the website based on design and requirements
   - Generates frontend, backend, or full-stack code as needed
   - Output: Complete, deployable website code

## 🏗️ Architecture

```
User Input → Requirements Agent → Designer Agent → Coder Agent → Website
```

**Supporting Components:**
- `tools/` - Shared tools and integrations used by agents
- `utils/` - Common utility functions and helpers
- Agent orchestration handles data flow between stages

## 🛠️ Getting Started

### Prerequisites
- Python 3.8+
- Google ADK Agents framework access

### Installation

```powershell
# Clone the repository
git clone https://github.com/GedelaSuryaDev/Website_builder.git
cd Website_builder

# Create virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```python
from google.adk.agents import LlmAgent
from website_builder import WebsiteBuilderWorkflow

# Initialize the workflow
workflow = WebsiteBuilderWorkflow()

# Create a website from user requirements
user_input = "I need an e-commerce site for selling handmade jewelry"
website = workflow.create_website(user_input)

print(f"Website created: {website.output_path}")
```

## 📁 Project Structure

```
agents/
├── requirements_agent.py    # Business analyst agent
├── designer_agent.py        # UI/UX designer agent  
├── coder_agent.py          # Full-stack developer agent
├── tools/                  # Shared agent tools
├── utils/                  # Common utilities
├── workflows/              # Orchestration logic
└── examples/               # Usage examples
```

## 🔧 Configuration

Create a `.env` file with required API keys:

```env
GOOGLE_ADK_API_KEY=your-adk-key
OPENAI_API_KEY=your-openai-key  # if using OpenAI models
# Add other service keys as needed
```

## 🚦 Development

### Adding New Agents
1. Create agent module in appropriate directory
2. Implement using `LlmAgent` base class
3. Add to workflow orchestration
4. Update documentation

### Security Best Practices
- Store credentials in environment variables or secrets manager
- Never commit API keys to version control
- Use `.gitignore` for sensitive files
- Pin dependency versions for production deployments

## 📝 Examples

See `examples/` directory for:
- Basic website creation
- E-commerce site generation  
- Blog/portfolio sites
- Custom workflow implementations

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request
