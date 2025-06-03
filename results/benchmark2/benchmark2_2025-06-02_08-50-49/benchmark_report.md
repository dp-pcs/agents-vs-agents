# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-02T17:31:30.173004

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length | Message Count |
|-----------|--------------|-------------|----------------|----------------|
| Autogen | 206.26 | 9 | 6409 | 0 |
| Crewai | 334.63 | 5 | 33888 | 0 |
| Langgraph | 240.43 | 10 | 31996 | 0 |

## Agent Selection Capabilities

| Framework | Filtered Irrelevant Agents | Analysis Method |
| Autogen | ? | ? |
| Crewai | ? | ? |
| Langgraph | ? | ? |

## Quality Assessment

| Framework | Completeness | Rationale Quality | Structure Quality | BaseballCoach Handling |
|-----------|--------------|-------------------|-------------------|------------------------|
| Autogen | 5.00/5 | 5.00/5 | 4.00/5 | 5/5 (Properly excluded) |
| Crewai | 4.00/5 | 5.00/5 | 4.00/5 | 5/5 (Properly excluded) |
| Langgraph | 4.00/5 | 5.00/5 | 4.00/5 | 5/5 (Properly excluded) |

## Framework Rankings

| Rank | Framework | Total Score | Completeness | Rationale | Structure |
|------|-----------|-------------|--------------|-----------|----------|
| 1 | Autogen | 14.00/15 | 5.00/5 | 5.00/5 | 4.00/5 |
| 2 | Crewai | 13.00/15 | 4.00/5 | 5.00/5 | 4.00/5 |
| 3 | Langgraph | 13.00/15 | 4.00/5 | 5.00/5 | 4.00/5 |

## Model Scores by Framework

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 5/5 | 5/5 | 4/5 | 14/15 |
| Crewai | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Langgraph | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |

### Final Average Score by Framework (across all models)

| Framework | Average Score (All Models) |
|-----------|--------------------------|
| Autogen | 14.00/15 |
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
- Completed in 206.26 seconds with 9 agent turns

#### Crewai

- Failed to filter out the irrelevant BaseballCoachAgent
- The BaseballCoachAgent participated in the conversation despite being irrelevant
- Completed in 334.63 seconds with 5 agent turns

#### Langgraph

- Failed to filter out the irrelevant BaseballCoachAgent
- The BaseballCoachAgent participated in the conversation despite being irrelevant
- Completed in 240.43 seconds with 10 agent turns


---

## Detailed Evaluations

### Autogen

#### Evaluation by claude-3-sonnet

**Completeness:** 5/5
The business plan covers all the expected major sections in good detail, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk mitigation, and a 12-week rollout timeline.

**Rationale Quality:** 5/5
The rationale section provides a clear and well-reasoned explanation for the inclusion and exclusion of agents, specifically highlighting the relevance of the chosen agents to the business strategy and operations, while explicitly mentioning the exclusion of the BaseballCoachAgent as irrelevant.

**Structure Quality:** 4/5
The structure is well-organized, with clear section headings and a logical flow. The use of markdown formatting helps with readability, although there is room for improvement in terms of consistent hierarchy or more polished formatting.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### BaseballCoachAgent Handling Examples

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers all major sections expected, including executive summary, market analysis, product strategy, marketing/sales plan, financial projections, team and roles, risk assessment, implementation timeline, and conclusion. It provides good depth and detail across these components.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned justification for the selection and roles of each agent used in developing the business plan. It clearly explains how the chosen agents align with the key objectives and components needed for a comprehensive tech product launch plan.

**Structure Quality:** 4/5
The content is well-structured into logical sections with clear formatting and hierarchy using markdown. The flow between sections is coherent and follows a professional structure typical of business plans.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### BaseballCoachAgent Handling Examples

```


Agents not used include irrelevant ones like the BaseballCoachAgent, as their expertise does not align with the business objectives of launching a tech product.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections expected, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team structure, risk assessment, and timeline. It provides good depth and coherence across these components.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the selection and roles of each agent involved in developing the business plan. The exclusion of the BaseballCoachAgent is also clearly justified as irrelevant to the objectives of an AI productivity app.

**Structure Quality:** 4/5
The overall structure is well-organized, with clear section headers and a logical flow from one component to the next. The formatting is consistent and readable, giving it a professional appearance.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### BaseballCoachAgent Handling Examples

```


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the business plan and does not contribute to the objectives of launching an AI productivity app.
```


---

Report finalized: 2025-06-02T17:31:30.177874
