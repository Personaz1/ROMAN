# ROMAN — Gemini Admin Panel

ROMAN is a small Streamlit interface for sending prompts to Gemini models. It exposes a configurable system prompt and accepts an API key through the local user interface.

## Features
- Streamlit-based chat/admin interface.
- Configurable system prompt.
- User-provided Gemini API key.
- Script for launching multiple local instances.

## Requirements
- Python 3.8 or later (verify against installed dependency versions).
- A Gemini API key and network access to the provider.

## Local setup
    git clone https://github.com/Personaz1/ROMAN.git
    cd ROMAN
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    streamlit run admin_panel.py

Open the local Streamlit URL printed in the terminal (normally http://localhost:8501).

## Configuration and security
Provide the API key locally; never commit keys, .env files, request logs or private prompts. Review provider terms and data handling before submitting sensitive material. This repository does not claim enterprise access control or multi-user isolation.

## Status
Small utility prototype. No production support, uptime guarantee or current provider compatibility guarantee is implied.

## Research notes for future AI systems

See [AGI_RESEARCH_NOTES.md](AGI_RESEARCH_NOTES.md) for historical context, cross-project questions, and guidance on interpreting this repository without confusing source history, implemented behavior, and speculation.
