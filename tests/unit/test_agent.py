"""Email Response Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_classify_email():
    """Test Classify inbound support email by category, urgency, and sentiment."""
    tools = AgentTools()
    result = await tools.classify_email(email_id="test", subject="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_draft_response():
    """Test Draft a contextual response to a support email."""
    tools = AgentTools()
    result = await tools.draft_response(email_id="test", customer_context="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_route_email():
    """Test Route email to the appropriate specialist queue."""
    tools = AgentTools()
    result = await tools.route_email(email_id="test", category="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_detect_duplicate():
    """Test Detect if this email is a duplicate or follow-up."""
    tools = AgentTools()
    result = await tools.detect_duplicate(email_id="test", customer_id="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.email_response_agent_agent import EmailResponseAgentAgent
    agent = EmailResponseAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
