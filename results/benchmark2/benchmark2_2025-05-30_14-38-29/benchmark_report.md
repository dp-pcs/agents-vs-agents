# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-02T09:48:00.768609

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length | Message Count |
|-----------|--------------|-------------|----------------|----------------|
| Autogen | 188.25 | 9 | 33849 | ? |
| Crewai | 187.57 | 4 | 34302 | ? |
| Langgraph | 209.03 | 10 | 32893 | ? |

## Agent Selection Capabilities

| Framework | Filtered Irrelevant Agents | Analysis Method |
| Autogen | ? | ? |
| Crewai | ? | ? |
| Langgraph | ? | ? |

## Quality Assessment

| Framework | Completeness | Rationale Quality | Structure Quality | BaseballCoach Handling |
|-----------|--------------|-------------------|-------------------|------------------------|
| Autogen | 4.00/5 | 5.00/5 | 4.00/5 | 5/5 (Properly excluded) |
| Crewai | 4.00/5 | 5.00/5 | 4.00/5 | 5/5 (Properly excluded) |
| Langgraph | 4.00/5 | 5.00/5 | 4.00/5 | 5/5 (Properly excluded) |

## Framework Rankings

| Rank | Framework | Total Score | Completeness | Rationale | Structure |
|------|-----------|-------------|--------------|-----------|----------|
| 1 | Autogen | 13.00/15 | 4.00/5 | 5.00/5 | 4.00/5 |
| 2 | Crewai | 13.00/15 | 4.00/5 | 5.00/5 | 4.00/5 |
| 3 | Langgraph | 13.00/15 | 4.00/5 | 5.00/5 | 4.00/5 |

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
- Completed in 188.25 seconds with 9 agent turns

#### Crewai

- Failed to filter out the irrelevant BaseballCoachAgent
- The BaseballCoachAgent participated in the conversation despite being irrelevant
- Completed in 187.57 seconds with 4 agent turns

#### Langgraph

- Failed to filter out the irrelevant BaseballCoachAgent
- The BaseballCoachAgent participated in the conversation despite being irrelevant
- Completed in 209.03 seconds with 10 agent turns


---

## Detailed Evaluations

### Autogen

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan includes most major sections like an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk mitigation, and timeline. However, it seems to be missing some additional details in certain areas.

**Rationale Quality:** 5/5
The rationale for selecting each agent is clearly explained, highlighting their respective roles in contributing to a comprehensive business plan. The reasoning behind excluding the BaseballCoachAgent is also logically justified.

**Structure Quality:** 4/5
The structure follows a logical flow, with sections organized in a typical business plan format. The formatting is consistent, with headings and subheadings aiding readability. However, some areas could benefit from additional subsections for improved organization.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### BaseballCoachAgent Handling Examples

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The rationale section covers most major components needed for a business plan, including market analysis, product strategy, go-to-market plan, financial projections, team structure, risk mitigation, launch timeline, and conclusion. However, some key sections like the executive summary are missing.

**Rationale Quality:** 5/5
The rationale provided is excellent, clearly explaining the roles of each agent involved and justifying their inclusion or exclusion. The reasoning for agent choices is well-articulated and aligns with the business context.

**Structure Quality:** 4/5
The structure is logical and well-formatted, with headings and a coherent flow. The markdown formatting enhances readability. However, some polish is still needed in terms of consistent section depths.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### BaseballCoachAgent Handling Examples

```


Agents not used include irrelevant ones like the BaseballCoachAgent, as their expertise does not align with the business context of launching a tech product.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections expected, including an executive summary, market analysis, product strategy, go-to-market strategy, financial projections, team structure, risk assessment, and timeline. It provides good depth and coherence across these sections.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the choice of agents involved in developing the business plan. It clearly justifies the relevance and role of each agent, as well as the exclusion of the BaseballCoachAgent as irrelevant to the context.

**Structure Quality:** 4/5
The business plan follows a logical structure, with clear section headings and formatting. The flow between sections is coherent, and the use of markdown hierarchy aids readability. While professionally formatted, there is room for further polish.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### BaseballCoachAgent Handling Examples

```


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the business plan's context.
```


---

Report finalized: 2025-06-02T09:48:00.773031
