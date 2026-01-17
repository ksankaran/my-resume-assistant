# My Resume Assistant

AI-powered resume Q&A agent built with LangGraph.

## Overview

- **Purpose:** Answer questions about Velu Sankaran's professional background
- **Live Backend:** Deployed via LangGraph Cloud (auto-deploys on push)
- **Frontend:** https://velu.dev (resume-assistant-ui repo)

## Tech Stack

- **Framework:** LangGraph
- **LLM:** OpenAI (via LangChain)
- **Deployment:** LangGraph Cloud
- **Package Manager:** uv

## Key Files

| File | Purpose |
|------|---------|
| `agent/my_prompt.py` | Main prompt with resume data and security hardening |
| `agent/agent.py` | LangGraph agent definition |
| `langgraph.json` | LangGraph deployment config |

## Running Locally

```bash
cd /usr/local/workspace/my-resume-assistant

# Set environment variables (from ~/.zshrc)
source ~/.zshrc

# Start LangGraph dev server
uv run langgraph dev --port 2024
```

Server runs at `http://localhost:2024`

## Prompt Security

The prompt in `agent/my_prompt.py` is hardened against injection attacks:
- XML-style tags separate system instructions from user input
- Strict boundaries prevent role-play or instruction override attempts
- Refuses off-topic requests politely

## Resume Content

The prompt contains Velu's full resume including:
- **Experience:** 19+ years
- **Companies:** Walmart, ADP, Weather Channel, IHG, Akamai, Amazon, Best Buy
- **Skills:** React, Node.js, LangGraph, Google ADK, MCP Tools, and more
- **Publications:** "Zero to AI Agent" book (Amazon: https://a.co/d/hfp7DYr)
- **Recent AI Work:** Support agents for ADP API Clients using Google ADK, LangGraph, MCP Tools

## Updating Resume

Edit `agent/my_prompt.py` and push to main. LangGraph Cloud auto-deploys.

## Related Repos

- **UI:** `/usr/local/workspace/resume-assistant-ui` (https://github.com/ksankaran/resume-assistant-ui)
- **Book:** `/usr/local/workspace/ztaa-book` (Zero to AI Agent)
