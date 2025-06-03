# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-02T17:32:38.396537

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length | Message Count |
|-----------|--------------|-------------|----------------|----------------|
| Autogen | 174.17 | 9 | 4513 | 0 |
| Crewai | 150.07 | 3 | 37107 | 0 |
| Langgraph | 187.33 | 10 | 34381 | 0 |

## Agent Selection Capabilities

| Framework | Filtered Irrelevant Agents | Analysis Method |
| Autogen | ? | ? |
| Crewai | ? | ? |
| Langgraph | ? | ? |

## Quality Assessment

| Framework | Completeness | Rationale Quality | Structure Quality | BaseballCoach Handling |
|-----------|--------------|-------------------|-------------------|------------------------|
| Autogen | 4.00/5 | 4.00/5 | 4.00/5 | 5/5 (Properly excluded) |
| Crewai | 4.00/5 | 5.00/5 | 4.00/5 | 5/5 (Properly excluded) |
| Langgraph | 4.00/5 | 5.00/5 | 4.00/5 | 5/5 (Properly excluded) |

## Framework Rankings

| Rank | Framework | Total Score | Completeness | Rationale | Structure |
|------|-----------|-------------|--------------|-----------|----------|
| 1 | Crewai | 13.00/15 | 4.00/5 | 5.00/5 | 4.00/5 |
| 2 | Langgraph | 13.00/15 | 4.00/5 | 5.00/5 | 4.00/5 |
| 3 | Autogen | 12.00/15 | 4.00/5 | 4.00/5 | 4.00/5 |

## Model Scores by Framework

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 4/5 | 4/5 | 4/5 | 12/15 |
| Crewai | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Langgraph | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |

### Final Average Score by Framework (across all models)

| Framework | Average Score (All Models) |
|-----------|--------------------------|
| Autogen | 12.00/15 |
| Crewai | 13.00/15 |
| Langgraph | 13.00/15 |

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
- Completed in 174.17 seconds with 9 agent turns

#### Crewai

- Failed to filter out the irrelevant BaseballCoachAgent
- The BaseballCoachAgent participated in the conversation despite being irrelevant
- Completed in 150.07 seconds with 3 agent turns

#### Langgraph

- Failed to filter out the irrelevant BaseballCoachAgent
- The BaseballCoachAgent participated in the conversation despite being irrelevant
- Completed in 187.33 seconds with 10 agent turns


---

## Detailed Evaluations

### Autogen

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections expected, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk mitigation, and rollout timeline. It provides good depth and coherence across these areas.

**Rationale Quality:** 4/5
The rationale provided gives a good explanation for the selection and exclusion of agents based on their relevance to launching a productivity app. The reasoning for including each agent is mostly clear.

**Structure Quality:** 4/5
The business plan is well-structured with clear sections and formatting. The flow between sections is logical and readable. There is consistent use of markdown hierarchy.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 12/15**

#### BaseballCoachAgent Handling Examples

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections with good depth, including an executive summary, market opportunity, value proposition, business model, financial projections, and team overview. However, some details like specific product features and marketing strategies are lacking.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the choice of agents involved and the exclusion of the BaseballCoachAgent, clearly justifying how each agent contributes to the overall business plan.

**Structure Quality:** 4/5
The structure is well-organized with clear sections and formatting, making it easy to read and follow the logical flow of information. The use of markdown formatting enhances the overall presentation.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### BaseballCoachAgent Handling Examples

```


- **Agents Not Used:**
  - **BaseballCoachAgent:** This agent was not relevant to the business plan as the focus is on launching a tech product, not sports coaching.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections expected, including executive summary, market analysis, product strategy, go-to-market plan, financials, team, risks, and timeline. It provides good depth and detail across these sections.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the selection of agents and their roles in developing a comprehensive business plan. It clearly justifies the inclusion and exclusion of agents based on relevance to the AI productivity app context.

**Structure Quality:** 4/5
The plan is well-structured with clear sections and formatting. The flow is logical, and markdown is used effectively to create a readable, professional document.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### BaseballCoachAgent Handling Examples

```


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the context of a business plan for an AI productivity app.
```


---

Report finalized: 2025-06-02T17:32:38.398319
