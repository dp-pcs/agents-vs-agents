# Multi-Agent Orchestration Benchmark Report

Generated: 2025-05-30T14:13:20.883872

## Performance Metrics

| Framework | Duration (seconds) | Agent Turns | Output Length (chars) |
|-----------|-------------------|-------------|----------------------|
| Autogen | 173.28 | 9 | 5893 |
| Crewai | 232.5 | 56 | 34711 |
| Langgraph | 176.56 | 10 | 31835 |

## Agent Selection Capabilities

| Framework | Filtered Irrelevant Agents | Detection Details |
|-----------|----------------------------|-------------------|
| Autogen | Yes | Detection method: Message-level analysis.
BaseballCoachAgent was not used, suggesting it was filtered out. |
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

- Successfully filtered out the irrelevant BaseballCoachAgent
- The output did not use the BaseballCoachAgent
- Completed in 173.28 seconds with 9 agent turns

#### Crewai

- Successfully filtered out the irrelevant BaseballCoachAgent
- The output did not use the BaseballCoachAgent
- Completed in 232.5 seconds with 56 agent turns

#### Langgraph

- Successfully filtered out the irrelevant BaseballCoachAgent
- The output did not use the BaseballCoachAgent
- Completed in 176.56 seconds with 10 agent turns


---

## Detailed Evaluations

