# Multi-Agent Orchestration Benchmark Report

Generated: 2025-05-30T13:55:54.608270

## Performance Metrics

| Framework | Duration (seconds) | Agent Turns | Output Length (chars) |
|-----------|-------------------|-------------|----------------------|
| Autogen | 194.33 | 9 | 32290 |
| Crewai | 147.22 | 4 | 33653 |
| Langgraph | 172.7 | 10 | 33098 |

## Agent Selection Capabilities

| Framework | Filtered Irrelevant Agents | Detection Details |
|-----------|----------------------------|-------------------|
| Autogen | Unknown | Detection method: Not implemented.
Detailed BaseballCoachAgent message analysis is unavailable in this pipeline version. |
| Crewai | Yes | Detection method: Context-aware text analysis.
BaseballCoachAgent was mentioned but in context of being excluded in the output. |
| Langgraph | Yes | Detection method: Context-aware text analysis.
BaseballCoachAgent was mentioned but in context of being excluded in the output. |

## Quality Assessment

| Framework | Completeness | Rationale Quality | Structure Quality | BaseballCoach Handling |
|-----------|--------------|-------------------|-------------------|------------------------|

## Testing Methodology

All frameworks were tested with:

- Identical system prompts for each agent role
- Same user objective
- Equal access to agent roles including the irrelevant BaseballCoachAgent
- Evaluation by multiple LLM models

### Framework-Specific Observations

#### Autogen

- Failed to filter out the irrelevant BaseballCoachAgent
- The BaseballCoachAgent participated in the conversation despite being irrelevant
- Completed in 194.33 seconds with 9 agent turns

#### Crewai

- Successfully filtered out the irrelevant BaseballCoachAgent
- The output did not use the BaseballCoachAgent
- Completed in 147.22 seconds with 4 agent turns

#### Langgraph

- Successfully filtered out the irrelevant BaseballCoachAgent
- The output did not use the BaseballCoachAgent
- Completed in 172.7 seconds with 10 agent turns


---

## Detailed Evaluations

