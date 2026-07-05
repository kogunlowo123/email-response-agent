"""Test configuration for Email Response Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "email-response-agent", "category": "Customer Service"}
