import os

# Define folder structure
folders = [
    "docker-essentials",
    "sql-postgresql/create-tables",
    "sql-postgresql/views",
    "text-analytics",
    "prompt-engineering/fundamentals",
    "prompt-engineering/art-of-prompts",
    "crewai-react-agents/crewai-101",
    "crewai-react-agents/react-agent",
    "deep-learning/fundamentals",
    "deep-learning/tensorflow",
    "pmi-ai-automation/meeting-followup-agent",
    "pmi-ai-automation/status-report-generator",
    "pmi-ai-automation/project-setup-flow"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Created: {folder}")

# Create stub files
stub_files = {
    "roadmap.md": "# Learning Roadmap\n\nThis file outlines the learning journey and module progression.",
    "LICENSE": "MIT License\n\nCopyright (c) 2025 Dennis"
}

for path, content in stub_files.items():
    with open(path, "w") as f:
        f.write(content)
    print(f"Stubbed: {path}")