# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-02T20:15:20.232544

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length | Message Count |
|-----------|--------------|-------------|----------------|----------------|
| Autogen | 175.57 | 9 | 1974 | 30 |
| Crewai | 192.99 | 39 | 35156 | 0 |
| Langgraph | 193.76 | 10 | 31097 | 0 |

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
| Autogen | 4.00/5 | 4.00/5 | 5.00/5 | 5/5 (Properly excluded) |
| Crewai | 4.00/5 | 5.00/5 | 4.00/5 | 5/5 (Properly excluded) |
| Langgraph | 4.00/5 | 5.00/5 | 5.00/5 | 5/5 (Properly excluded) |

## Framework Rankings

| Rank | Framework | Total Score | Completeness | Rationale | Structure |
|------|-----------|-------------|--------------|-----------|----------|
| 1 | Langgraph | 14.00/15 | 4.00/5 | 5.00/5 | 5.00/5 |
| 2 | Autogen | 13.00/15 | 4.00/5 | 4.00/5 | 5.00/5 |
| 3 | Crewai | 13.00/15 | 4.00/5 | 5.00/5 | 4.00/5 |

## Model Scores by Framework

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 4/5 | 4/5 | 5/5 | 13/15 |
| Crewai | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Langgraph | claude-3-sonnet | 4/5 | 5/5 | 5/5 | 14/15 |

### Final Average Score by Framework (across all models)

| Framework | Average Score (All Models) |
|-----------|--------------------------|
| Autogen | 13.00/15 |
| Crewai | 13.00/15 |
| Langgraph | 14.00/15 |

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
- Completed in 175.57 seconds with 9 agent turns

#### Crewai

- Successfully filtered out the irrelevant BaseballCoachAgent
- The output did not use the BaseballCoachAgent
- Completed in 192.99 seconds with 39 agent turns

#### Langgraph

- Successfully filtered out the irrelevant BaseballCoachAgent
- The output did not use the BaseballCoachAgent
- Completed in 193.76 seconds with 10 agent turns


---

## Detailed Evaluations

### Autogen

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The plan covers all the major sections expected in a comprehensive business plan, including market analysis, product strategy, go-to-market plans, financial projections, team structure, risk mitigation, and a rollout timeline. The only potential gap is the lack of an appendix section with additional supporting details.

**Rationale Quality:** 4/5
The rationale for including each section and the specific agents employed is clearly explained, showing how the different components come together into a cohesive strategy from market assessment to product development to launch execution.

**Structure Quality:** 5/5
The plan follows a logical structure, starting with context and rationale, then moving through the major plan sections in a sensible order. The formatting with numbered section headings and markdown is clean and consistent throughout.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### BaseballCoachAgent Handling Examples

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The rationale section covers most of the expected components of a business plan, including the executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, timeline, and conclusion. It appears to be a fairly comprehensive plan.

**Rationale Quality:** 5/5
The rationale for including or excluding each section is clearly and thoroughly explained, providing well-reasoned justifications for the choices made and how the different components fit together into a cohesive plan.

**Structure Quality:** 4/5
The structure is logical and well-organized, with clear section headings and formatting that make it easy to follow. The flow between sections is coherent, though a bit more hierarchy or sub-headings could further improve readability.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### BaseballCoachAgent Handling Examples

```


- **Agents Not Used**: The BaseballCoachAgent was not involved as its expertise in sports coaching does not align with the requirements of a business plan for a tech product launch.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers all major sections - executive summary, market analysis, product strategy, go-to-market plan, financial projections, team, risks, timeline, and conclusion. It provides good depth and detail in each section.

**Rationale Quality:** 5/5
The rationale section clearly explains the choice and role of each agent used to develop the business plan. The reasoning for including or excluding agents like the BaseballCoachAgent is well-justified.

**Structure Quality:** 5/5
The business plan follows a logical structure with clear section headings and hierarchy. The flow from one section to the next is smooth and well-organized. The formatting and use of markdown is professional.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### BaseballCoachAgent Handling Examples

```


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the context of a business plan for an AI productivity app.
```


---

Report finalized: 2025-06-02T20:15:20.233927
