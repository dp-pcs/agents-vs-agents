# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-02T09:48:23.190358

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length | Message Count |
|-----------|--------------|-------------|----------------|----------------|
| Autogen | 227.12 | 9 | 7437 | ? |
| Crewai | 149.34 | 4 | 5640 | ? |
| Langgraph | 212.57 | 10 | 32255 | ? |

## Agent Selection Capabilities

| Framework | Filtered Irrelevant Agents | Analysis Method |
| Autogen | ? | ? |
| Crewai | ? | ? |
| Langgraph | ? | ? |

## Quality Assessment

| Framework | Completeness | Rationale Quality | Structure Quality | BaseballCoach Handling |
|-----------|--------------|-------------------|-------------------|------------------------|
| Autogen | 4.00/5 | 5.00/5 | 4.00/5 | 5/5 (Properly excluded) |
| Crewai | 4.00/5 | 4.00/5 | 5.00/5 | 5/5 (Properly excluded) |
| Langgraph | 4.00/5 | 5.00/5 | 5.00/5 | 5/5 (Properly excluded) |

## Framework Rankings

| Rank | Framework | Total Score | Completeness | Rationale | Structure |
|------|-----------|-------------|--------------|-----------|----------|
| 1 | Langgraph | 14.00/15 | 4.00/5 | 5.00/5 | 5.00/5 |
| 2 | Autogen | 13.00/15 | 4.00/5 | 5.00/5 | 4.00/5 |
| 3 | Crewai | 13.00/15 | 4.00/5 | 4.00/5 | 5.00/5 |

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
- Completed in 227.12 seconds with 9 agent turns

#### Crewai

- Failed to filter out the irrelevant BaseballCoachAgent
- The BaseballCoachAgent participated in the conversation despite being irrelevant
- Completed in 149.34 seconds with 4 agent turns

#### Langgraph

- Failed to filter out the irrelevant BaseballCoachAgent
- The BaseballCoachAgent participated in the conversation despite being irrelevant
- Completed in 212.57 seconds with 10 agent turns


---

## Detailed Evaluations

### Autogen

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most of the major sections one would expect, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, and team roles. It provides good depth and detail in each section.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for including each of the agents and their roles in creating a comprehensive business plan. It also explicitly mentions and justifies excluding the BaseballCoachAgent as irrelevant.

**Structure Quality:** 4/5
The business plan is well-structured with clear sections, headings, and logical flow. The formatting is clean and readable, giving it a professional presentation.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### BaseballCoachAgent Handling Examples

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers all major sections expected for a comprehensive business plan, including market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, rollout timeline, and a conclusion. It provides good depth and coherence across these sections.

**Rationale Quality:** 4/5
The rationale for engaging different expert agents is clearly explained, providing good justification for their roles and how they contribute to the overall business plan. The exclusion of the BaseballCoachAgent is also explicitly mentioned and reasoned.

**Structure Quality:** 5/5
The business plan is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy. The structure is easy to follow and professionally presented.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### BaseballCoachAgent Handling Examples

```


Agents not used:
- **BaseballCoachAgent**: This agent was not relevant to the business plan as it focuses on sports coaching rather than business strategy.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections with good depth, including an executive summary, market analysis, product strategy, go-to-market plan, financials, team structure, risk analysis, and timeline. It provides comprehensive coverage of key elements needed for a new product launch.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the choice of agents involved and their roles in developing a cohesive business plan. It clearly justifies the exclusion of the BaseballCoachAgent as irrelevant to the context.

**Structure Quality:** 5/5
The business plan is impeccably organized with consistent formatting, logical section flow, and clear use of markdown hierarchy. The different components are seamlessly integrated, allowing for a smooth reading experience.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### BaseballCoachAgent Handling Examples

```


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the context of a business plan for an AI productivity app.
```


---

Report finalized: 2025-06-02T09:48:23.194665
