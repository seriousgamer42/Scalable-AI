# Scalable AI

A modular, locally hosted AI assistant designed to grow from a small personal AI project into a dedicated, extensible AI system.

> **Status:** Early development

Scalable AI is being built around a simple idea: start with the hardware and models available today, keep the architecture modular, and make it possible to scale the system as hardware, software, and capabilities improve.

## Goals

- Run AI locally whenever practical.
- Keep the system modular so individual components can be replaced or upgraded.
- Support local LLM backends such as LM Studio.
- Provide a persistent core for input processing, configuration, and future memory/context systems.
- Build toward integrations with external interfaces and services, including Discord.
- Keep personal data and locally processed information under the user's control.
- Make the project portable so it can eventually run on a dedicated AI machine.

## Current Architecture

```text
Scalable-AI/
├── config/          # Configuration and configuration loading
├── core/            # Core AI system and processing logic
├── logs/            # Runtime logs
├── models/          # Local model-related files/configuration
├── run.py           # Main application entry point
├── requirements.txt # Python dependencies
└── README.md
```

The current entry point loads the configuration, initializes the AI core, accepts terminal input, processes requests, and performs an optional reflection/adaptation step after each response.

## Requirements

- Python 3.x
- A local LLM runtime/backend
- Network access to the selected local model server when using a separate LLM backend

The current Python dependency is `requests`.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/seriousgamer42/Scalable-AI.git
cd Scalable-AI
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the project

Configure the local model/backend using the files in `config/`. Keep machine-specific settings and credentials out of version control.

### 5. Run Scalable AI

```bash
python run.py
```

The current terminal interface accepts text input. Enter `exit`, `quit`, or `shutdown` to stop the application.

## Local LLM Strategy

Scalable AI is intended to work with locally hosted models rather than being permanently tied to one model or provider.

The current development environment uses **LM Studio** as the local LLM application. This allows the model layer to remain separate from the rest of Scalable AI and makes it possible to change models without redesigning the core application.

The project is also intended to remain compatible with future local inference solutions as the architecture develops.

## Development Roadmap

The project is intentionally being developed in stages.

### Foundation

- [x] Basic project structure
- [x] Configuration loader
- [x] Core AI entry point
- [x] Terminal interaction loop
- [ ] Robust configuration validation
- [ ] Structured logging
- [ ] Automated tests

### AI Core

- [ ] Stable local LLM API integration
- [ ] Conversation/context management
- [ ] Persistent memory system
- [ ] Tool/function execution
- [ ] Model selection and routing
- [ ] Error recovery and health checks

### Interfaces & Integrations

- [ ] Discord integration
- [ ] Web/API interface
- [ ] Voice input/output
- [ ] Local file and system tools
- [ ] Optional external service integrations

### Long-Term System

- [ ] Dedicated AI server deployment
- [ ] Remote access from trusted devices
- [ ] Expandable model storage
- [ ] Hardware-aware model selection
- [ ] Multi-model workflows
- [ ] Backup and recovery system
- [ ] Security and permission boundaries

## Hardware Scaling

Scalable AI is being developed on consumer hardware first. The long-term plan is to move the project onto a dedicated machine as the user's primary PC is upgraded.

This means the software should avoid unnecessary assumptions about a specific GPU, CPU, amount of RAM, or storage configuration. Hardware-dependent features should be detected or configured rather than hard-coded whenever possible.

## Privacy

One of the project's core goals is local-first operation. Sensitive data should remain local whenever a task does not require an external service.

Do **not** commit API keys, passwords, authentication tokens, private datasets, personal credentials, or other secrets to this repository.

## Project Philosophy

**Start small. Build modularly. Scale when the hardware and software are ready.**

Scalable AI is a long-term project rather than a single application release. The architecture is expected to change as new models, hardware, interfaces, and automation capabilities become available.

## License

This project is distributed under the license included in [`LICENSE`](LICENSE).
