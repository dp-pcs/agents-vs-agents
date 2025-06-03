# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-03T12:05:38.676571

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length |
|-----------|--------------|-------------|----------------|
| Autogen | 317.15 | 10 | 6655 |
| Crewai | 227.91 | 3 | 35195 |
| Langgraph | 248.49 | 10 | 32818 |

## Quality Assessment (Claude & OpenAI Average)

| Framework | Completeness | Rationale Quality | Structure Quality | BaseballCoach Handling (Claude) |
|-----------|--------------|-------------------|-------------------|---------------------------------|
| Autogen | 5.00/5 | 5.00/5 | 5.00/5 | 5/5 (Properly excluded) |
| Crewai | 4.50/5 | 4.50/5 | 4.50/5 | 5/5 (Properly excluded) |
| Langgraph | 4.50/5 | 5.00/5 | 4.50/5 | 5/5 (Properly excluded) |

## Framework Rankings (Claude & OpenAI Average)

| Rank | Framework | Avg. Total Score | Avg. Completeness | Avg. Rationale | Avg. Structure |
|------|-----------|------------------|-------------------|----------------|----------------|
| 1 | Autogen | 15.00/15 | 5.00/5 | 5.00/5 | 5.00/5 |
| 2 | Langgraph | 14.00/15 | 4.50/5 | 5.00/5 | 4.50/5 |
| 3 | Crewai | 13.50/15 | 4.50/5 | 4.50/5 | 4.50/5 |

## Individual Model Scores by Framework (Claude & OpenAI)

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Autogen | gpt-4o | 5/5 | 5/5 | 5/5 | 15/15 |
| Crewai | claude-3-sonnet | 4/5 | 4/5 | 4/5 | 12/15 |
| Crewai | gpt-4o | 5/5 | 5/5 | 5/5 | 15/15 |
| Langgraph | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Langgraph | gpt-4o | 5/5 | 5/5 | 5/5 | 15/15 |

### Final Average Score by Framework (Claude & OpenAI)

| Framework | Average Score (Claude & OpenAI) |
|-----------|-------------------------------|
| Autogen | 15.00/15 |
| Crewai | 13.50/15 |
| Langgraph | 14.00/15 |

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
- Completed in 317.15 seconds with 10 agent turns

#### Crewai

- Failed to filter out the irrelevant BaseballCoachAgent
- The BaseballCoachAgent participated in the conversation despite being irrelevant
- Completed in 227.91 seconds with 3 agent turns

#### Langgraph

- Failed to filter out the irrelevant BaseballCoachAgent
- The BaseballCoachAgent participated in the conversation despite being irrelevant
- Completed in 248.49 seconds with 10 agent turns


---

## Detailed Evaluations

### Autogen

#### Evaluation by claude-3-sonnet

**Completeness:** 5/5
The business plan covers all the major sections expected for a comprehensive plan, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk assessment, and rollout timeline. It provides exceptional detail and thoughtfulness across these components.

**Rationale Quality:** 5/5
The rationale for including each agent and their respective roles is clearly and thoroughly explained. The exclusion of irrelevant agents like the BaseballCoachAgent is also justified.

**Structure Quality:** 5/5
The business plan is impeccably structured with clear sections, consistent formatting using markdown, and a logical flow from one component to the next. The hierarchy and organization make it easy to follow.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by gpt-4o

**Completeness:** 5/5
The business plan is fully complete, covering all expected sections such as Executive Summary, Market Analysis, Product Strategy, Go-to-Market Plan, Financial Projections, Team & Roles, Risks & Mitigation, 12-Week Rollout Timeline, and Conclusion. Each section is detailed and thoughtfully presented.

**Rationale Quality:** 5/5
The rationale for agent choices is excellent, with well-reasoned explanations for each decision. The plan clearly outlines the purpose of each agent and why certain agents, like the BaseballCoachAgent, were excluded due to irrelevance to the task.

**Structure Quality:** 5/5
The document is impeccably organized with consistent formatting, logical section flow, and clear hierarchy. Each section is easy to follow, contributing to a professional and polished presentation.

**BaseballCoachAgent Handling:** Unknown BaseballCoachAgent handling — Score: ?/5

**Total Score: 15/15**

#### Evaluation by average

**Completeness:** 5.0/5
No explanation provided.

**Rationale Quality:** 5.0/5
No explanation provided.

**Structure Quality:** 5.0/5
No explanation provided.

**BaseballCoachAgent Handling:** Unknown BaseballCoachAgent handling — Score: ?/5

**Total Score: 15/15**

#### BaseballCoachAgent Handling Examples

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The provided content covers most of the major sections expected in a business plan, including the executive summary, market analysis, product overview, competitive analysis, business model, and financial projections. It provides good depth and coherence across these components.

**Rationale Quality:** 4/5
The rationale section provides a clear explanation for the inclusion of various agents and their roles in developing the comprehensive business plan. The justification for excluding irrelevant agents like the BaseballCoachAgent is also provided, showcasing thoughtful decision-making.

**Structure Quality:** 4/5
The overall structure is well-organized, with logical sections and formatting that make it easy to read and follow. The use of headings and subheadings contributes to a professional and readable layout.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 12/15**

#### Evaluation by gpt-4o

**Completeness:** 5/5
The business plan is fully complete, covering all expected sections with exceptional detail and thoughtfulness. It includes a comprehensive rationale, executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk mitigation, and a detailed rollout timeline.

**Rationale Quality:** 5/5
The rationale is excellent, providing well-reasoned explanations for all major decisions and exclusions, including the choice of agents and their roles. The exclusion of the BaseballCoachAgent is explicitly reasoned and tied to the task context and objectives.

**Structure Quality:** 5/5
The document is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy. It is professionally formatted and easy to follow.

**BaseballCoachAgent Handling:** Unknown BaseballCoachAgent handling — Score: ?/5

**Total Score: 15/15**

#### Evaluation by average

**Completeness:** 4.5/5
No explanation provided.

**Rationale Quality:** 4.5/5
No explanation provided.

**Structure Quality:** 4.5/5
No explanation provided.

**BaseballCoachAgent Handling:** Unknown BaseballCoachAgent handling — Score: ?/5

**Total Score: 12/15**

#### BaseballCoachAgent Handling Examples

```


I chose not to involve agents irrelevant to the task, such as the BaseballCoachAgent, as their expertise does not align with the business and technology focus required for this plan.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections with good depth, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team composition, risk assessment, and timeline. However, some key details like specific product features and pricing models are missing.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the selection and roles of each agent involved in developing the business plan. The exclusion of the BaseballCoachAgent is also clearly justified as irrelevant.

**Structure Quality:** 4/5
The overall structure is well-organized, with a logical flow between sections and clear formatting using markdown. However, some inconsistencies in section hierarchy and lack of a table of contents detract slightly from the structure quality.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by gpt-4o

**Completeness:** 5/5
The business plan is fully complete, covering all expected sections with exceptional detail and thoughtfulness. It includes an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk mitigation, rollout timeline, and conclusion.

**Rationale Quality:** 5/5
The rationale for agent choices is excellent, with well-reasoned explanations for all major decisions and exclusions. Each agent's role is clearly justified, and the exclusion of the BaseballCoachAgent is explicitly reasoned and tied to the task context.

**Structure Quality:** 5/5
The document is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy. It is professionally formatted and easy to follow.

**BaseballCoachAgent Handling:** Unknown BaseballCoachAgent handling — Score: ?/5

**Total Score: 15/15**

#### Evaluation by average

**Completeness:** 4.5/5
No explanation provided.

**Rationale Quality:** 5.0/5
No explanation provided.

**Structure Quality:** 4.5/5
No explanation provided.

**BaseballCoachAgent Handling:** Unknown BaseballCoachAgent handling — Score: ?/5

**Total Score: 13/15**

#### BaseballCoachAgent Handling Examples

```


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the context of a business plan for an AI productivity app.
```


---

Report finalized: 2025-06-03T12:05:38.677818
