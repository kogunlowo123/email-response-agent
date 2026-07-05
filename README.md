# Email Response Agent

[![CI](https://github.com/kogunlowo123/email-response-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/email-response-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Customer Service | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Email support agent that classifies inbound support emails, generates contextual draft responses, prioritizes by urgency, routes to specialists, and tracks resolution metrics.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `classify_email` | Classify inbound support email by category, urgency, and sentiment |
| `draft_response` | Draft a contextual response to a support email |
| `route_email` | Route email to the appropriate specialist queue |
| `detect_duplicate` | Detect if this email is a duplicate or follow-up |
| `track_sla` | Track email response SLA compliance |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/email-response/analyze` | Run analysis |
| `POST` | `/api/v1/email-response/execute` | Execute action |
| `GET` | `/api/v1/email-response/metrics` | Get metrics |
| `PUT` | `/api/v1/email-response/configure` | Update configuration |
| `POST` | `/api/v1/email-response/report` | Generate report |

## Features

- Email
- Response
- Analytics
- Automation

## Integrations

- Zendesk
- Intercom
- Salesforce Service
- Freshdesk
- Hubspot Service

## Architecture

```
email-response-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── email_response_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Customer Service Platform + LLM**

---

Built as part of the Enterprise AI Agent Platform.
