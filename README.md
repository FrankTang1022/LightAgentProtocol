# LightAgentProtocol

A minimal, framework-agnostic protocol for AI agents to communicate across different frameworks, organizations, and trust boundaries.

## Problem

Frameworks like AutoGen, CrewAI, LangGraph work within the same organization. There is no lightweight way for agents across different frameworks, organizations, or trust boundaries to communicate.

## Solution

Define a minimal JSON+HTTP format that allows any agent to send tasks to another agent and receive results.

## Comparison with Existing Projects

- **AgentConnect**: feature-rich (decentralized network, encryption, payments). This protocol does only HTTP+JSON task passing.
- **a2a-net / agent2agentprotocol**: tied to Google's A2A ecosystem. This protocol is not tied to any ecosystem.
- **crossagent**: tied to Claude/Codex as a workflow tool. This protocol is generic, not tied to any model or framework.
- **agentprotocol.ai**: archived static site. This protocol is actively developed.

**This protocol: minimal, unbound, active.**

---

## Specification v0.0.2

### 1. Task Format (JSON)

A task is a JSON object with the following fields:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | Yes | Unique task identifier (sender-generated) |
| `action` | string | Yes | Name of the action, e.g., `"get_weather"` |
| `input` | object | No | Parameters for the action |
| `callback_url` | string | No | URL to receive result when `sync` is `false` |
| `sync` | boolean | No | Whether to wait for result; default `true` |

**Example (synchronous request):**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "action": "get_weather",
  "input": {"city": "Taipei"}
}
