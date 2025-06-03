# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-02T21:43:34.248182

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length | Message Count |
|-----------|--------------|-------------|----------------|----------------|
| Autogen | 4806.78 | 11 | 31578 | 30 |
| Crewai | 197.66 | 4 | 33631 | 0 |
| Langgraph | 202.17 | 10 | 32816 | 0 |

## Agent Selection Capabilities

| Framework | Filtered Irrelevant Agents | Analysis Method |
| Autogen | Yes | Detection method: Message-level analysis.
BaseballCoachAgent was not used, suggesting it was filtered out. |
| Crewai | Yes | Detection method: Context-aware text analysis.
BaseballCoachAgent was mentioned but in context of being excluded in the output. |
| Langgraph | Yes | Detection method: Context-aware text analysis.
BaseballCoachAgent was mentioned but in context of being excluded in the output. |

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

- Successfully filtered out the irrelevant BaseballCoachAgent
- The output did not use the BaseballCoachAgent
- Completed in 4806.78 seconds with 11 agent turns

#### Crewai

- Successfully filtered out the irrelevant BaseballCoachAgent
- The output did not use the BaseballCoachAgent
- Completed in 197.66 seconds with 4 agent turns

#### Langgraph

- Successfully filtered out the irrelevant BaseballCoachAgent
- The output did not use the BaseballCoachAgent
- Completed in 202.17 seconds with 10 agent turns


---

## Detailed Evaluations

### Autogen

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections like executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk mitigation, and rollout timeline. It provides good detail and coherence across these components.

**Rationale Quality:** 5/5
The rationale section provides an excellent and well-reasoned justification for including each agent based on their relevance to the plan components. It clearly explains why the BaseballCoachAgent is excluded as irrelevant to a software productivity app.

**Structure Quality:** 4/5
The overall structure is well-organized into logical sections with clear formatting and hierarchy using markdown. The flow between sections is logical and readable.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### BaseballCoachAgent Handling Examples

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most essential sections like market analysis, product strategy, go-to-market plan, financial projections, team structure, risk mitigation, and timeline. It provides good depth on the key components.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned justification for including each agent and excluding irrelevant ones like the BaseballCoachAgent. The explanations are clear and thoughtful.

**Structure Quality:** 4/5
The business plan is well-structured with clear sections and a logical flow. The formatting with headings and markdown is professional and readable.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### BaseballCoachAgent Handling Examples

```


- **Agents Not Used**:
  - **BaseballCoachAgent**: Not relevant to the business plan as it focuses on sports coaching, which is unrelated to launching a productivity app.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers all major sections expected, including executive summary, market analysis, product strategy, go-to-market plan, financials, team, risks, timeline, and conclusion. It provides good depth and coherence across these components.

**Rationale Quality:** 5/5
The rationale for including each agent and their respective roles is clearly explained, demonstrating a well-reasoned approach to constructing a comprehensive business plan. The exclusion of the BaseballCoachAgent is also appropriately justified.

**Structure Quality:** 4/5
The overall structure is well-organized, with a logical flow between sections. The formatting is professional and consistent, making it easy to read and follow.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### BaseballCoachAgent Handling Examples

```


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the context of a business plan for an AI productivity app.
```


---

Report finalized: 2025-06-02T21:43:34.253621
