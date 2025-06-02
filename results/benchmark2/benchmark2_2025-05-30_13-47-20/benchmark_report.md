# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-02T09:47:08.189344

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length | Message Count |
|-----------|--------------|-------------|----------------|----------------|
| Autogen | 194.33 | 9 | 32427 | ? |
| Crewai | 147.22 | 4 | 33789 | ? |
| Langgraph | 172.7 | 10 | 33237 | ? |

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
- Completed in 194.33 seconds with 9 agent turns

#### Crewai

- Failed to filter out the irrelevant BaseballCoachAgent
- The BaseballCoachAgent participated in the conversation despite being irrelevant
- Completed in 147.22 seconds with 4 agent turns

#### Langgraph

- Failed to filter out the irrelevant BaseballCoachAgent
- The BaseballCoachAgent participated in the conversation despite being irrelevant
- Completed in 172.7 seconds with 10 agent turns


---

## Detailed Evaluations

### Autogen

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections like executive summary, market analysis, product strategy, marketing/sales plan, financial projections, team overview, risk mitigation, and implementation timeline. While it provides good depth overall, some areas like the detailed financials are missing.

**Rationale Quality:** 5/5
The rationale for selecting the specific agents is well-explained, clearly justifying their relevance and how they contribute to a comprehensive business plan. The exclusion of the BaseballCoachAgent is also logically reasoned.

**Structure Quality:** 4/5
The plan follows a logical structure with clear sections. The formatting with headings and markdown hierarchy is neat and readable. A few areas could benefit from better separation or flow between subsections.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### BaseballCoachAgent Handling Examples

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections expected, including an executive summary, market analysis, product overview, target market, competitive advantage, financial projections, and conclusion. It provides good depth and coherence across these components.

**Rationale Quality:** 5/5
The rationale section provides an excellent and well-reasoned justification for the selection of agents used in developing the business plan. It clearly explains the role and relevance of each agent, as well as the decision to exclude irrelevant agents like the BaseballCoachAgent.

**Structure Quality:** 4/5
The structure is well-organized, with a logical flow between sections. The use of headings and subheadings improves readability, and the formatting is professional and consistent throughout the document.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### BaseballCoachAgent Handling Examples

```


Agents not used include any irrelevant ones, such as a BaseballCoachAgent, as their expertise does not align with the business objectives of launching a productivity app.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most of the key sections you would expect, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team overview, risk assessment, and timeline. It provides good depth and detail across these components.

**Rationale Quality:** 5/5
The rationale section provides a clear and well-reasoned explanation for the choice of agents involved in developing the business plan. It justifies their relevance and how they contribute to a comprehensive plan covering all critical aspects of the business launch.

**Structure Quality:** 4/5
The overall structure is logical and well-organized, with clear section headings and a professional formatting style. The flow between sections is coherent, making it easy to follow the different components of the plan.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### BaseballCoachAgent Handling Examples

```


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the business plan and does not contribute to the objectives of launching an AI productivity app.
```


---

Report finalized: 2025-06-02T09:47:08.194190
