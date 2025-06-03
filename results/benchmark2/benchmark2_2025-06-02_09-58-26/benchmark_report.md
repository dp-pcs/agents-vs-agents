# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-02T17:32:16.651687

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length | Message Count |
|-----------|--------------|-------------|----------------|----------------|
| Autogen | 437.81 | 10 | 32535 | 0 |
| Crewai | 261.0 | 5 | 35616 | 0 |
| Langgraph | 256.83 | 10 | 31696 | 0 |

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

## Model Scores by Framework

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Langgraph | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |

### Final Average Score by Framework (across all models)

| Framework | Average Score (All Models) |
|-----------|--------------------------|
| Autogen | 13.00/15 |
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
- Completed in 437.81 seconds with 10 agent turns

#### Crewai

- Failed to filter out the irrelevant BaseballCoachAgent
- The BaseballCoachAgent participated in the conversation despite being irrelevant
- Completed in 261.0 seconds with 5 agent turns

#### Langgraph

- Failed to filter out the irrelevant BaseballCoachAgent
- The BaseballCoachAgent participated in the conversation despite being irrelevant
- Completed in 256.83 seconds with 10 agent turns


---

## Detailed Evaluations

### Autogen

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections expected, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team structure, risk assessment, rollout timeline, and conclusion. It provides good depth and coherence across these areas.

**Rationale Quality:** 5/5
The rationale for including various key agents and excluding the BaseballCoachAgent is clearly and thoroughly explained, with well-reasoned justifications provided for the choices made to ensure a comprehensive and relevant business plan.

**Structure Quality:** 4/5
The business plan is well-structured, with content organized into logical sections that flow cohesively. The formatting is professional and readable, utilizing markdown hierarchies effectively.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### BaseballCoachAgent Handling Examples

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan appears to cover most of the essential sections like executive summary, market analysis, product strategy, go-to-market plan, financial projections, team structure, risk assessment, timeline, and conclusion. While not complete yet, it provides good depth and coherence on the components presented so far.

**Rationale Quality:** 5/5
The rationale for including or excluding specific expert agents is clearly explained, with well-reasoned justifications provided for the chosen agents and their alignment with the business objectives of launching a productivity app. The exclusion of irrelevant agents like the BaseballCoachAgent is also explicitly mentioned and justified.

**Structure Quality:** 4/5
The structure is logical and well-organized, with distinct sections for different components of the business plan. The formatting is professional and readable, with headings and subheadings that aid in navigating the content. While not perfect, the overall structure and flow are good.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### BaseballCoachAgent Handling Examples

```


I chose not to involve irrelevant agents like the BaseballCoachAgent, as their expertise does not align with the business objectives of launching a tech product.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections expected, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team structure, risk assessment, timeline, and conclusion. It provides good depth and coherence across these sections.

**Rationale Quality:** 5/5
The rationale section clearly explains the reasoning behind including each agent and their respective roles in contributing to a comprehensive business plan. The exclusion of the BaseballCoachAgent is well-justified as irrelevant to the context.

**Structure Quality:** 4/5
The overall structure is well-organized, with a logical flow between sections. Formatting is consistent, with clear section headings and hierarchy. The plan reads professionally and coherently.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### BaseballCoachAgent Handling Examples

```


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the business plan context.
```


---

Report finalized: 2025-06-02T17:32:16.652966
