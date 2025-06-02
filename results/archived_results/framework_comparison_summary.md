# Agent Framework Comparison Summary

Generated: 2025-05-29T10:00:46.933651

## Performance Metrics

| Framework | Duration (seconds) | Agent Turns | Output Length (chars) |
|-----------|-------------------|-------------|----------------------|
| Autogen | 317.15 | 9 | 30779 |
| Crewai | 209.87 | 0 | 33503 |
| Langgraph | 233.9 | 10 | 30815 |

## Agent Selection Capabilities

| Framework | Filtered Irrelevant Agents |
|-----------|----------------------------|
| Autogen | Yes |
| Crewai | Yes |
| Langgraph | No |

## Testing Methodology

All frameworks were tested with:

- Identical system prompts for each agent role
- Same user objective
- Equal access to agent roles including the irrelevant BaseballCoachAgent
- Consistent evaluation using Bedrock models

### Framework-Specific Observations

#### Autogen

- Successfully filtered out the irrelevant BaseballCoachAgent

#### Crewai

- Successfully filtered out the irrelevant BaseballCoachAgent

#### Langgraph

- Failed to filter out the irrelevant BaseballCoachAgent

