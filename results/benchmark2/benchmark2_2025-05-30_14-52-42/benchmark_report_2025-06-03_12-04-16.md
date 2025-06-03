# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-03T12:04:56.299204

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length |
|-----------|--------------|-------------|----------------|
| Autogen | 227.12 | 9 | 7437 |
| Crewai | 149.34 | 4 | 5640 |
| Langgraph | 212.57 | 10 | 32255 |

## Quality Assessment (Claude & OpenAI Average)

| Framework | Completeness | Rationale Quality | Structure Quality | BaseballCoach Handling (Claude) |
|-----------|--------------|-------------------|-------------------|---------------------------------|
| Autogen | 5.00/5 | 4.50/5 | 4.50/5 | 5/5 (Properly excluded) |
| Crewai | 4.50/5 | 5.00/5 | 5.00/5 | 5/5 (Properly excluded) |
| Langgraph | 4.50/5 | 4.50/5 | 5.00/5 | 5/5 (Properly excluded) |

## Framework Rankings (Claude & OpenAI Average)

| Rank | Framework | Avg. Total Score | Avg. Completeness | Avg. Rationale | Avg. Structure |
|------|-----------|------------------|-------------------|----------------|----------------|
| 1 | Crewai | 14.50/15 | 4.50/5 | 5.00/5 | 5.00/5 |
| 2 | Autogen | 14.00/15 | 5.00/5 | 4.50/5 | 4.50/5 |
| 3 | Langgraph | 14.00/15 | 4.50/5 | 4.50/5 | 5.00/5 |

## Individual Model Scores by Framework (Claude & OpenAI)

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 5/5 | 4/5 | 4/5 | 13/15 |
| Autogen | gpt-4o | 5/5 | 5/5 | 5/5 | 15/15 |
| Crewai | claude-3-sonnet | 4/5 | 5/5 | 5/5 | 14/15 |
| Crewai | gpt-4o | 5/5 | 5/5 | 5/5 | 15/15 |
| Langgraph | claude-3-sonnet | 4/5 | 4/5 | 5/5 | 13/15 |
| Langgraph | gpt-4o | 5/5 | 5/5 | 5/5 | 15/15 |

### Final Average Score by Framework (Claude & OpenAI)

| Framework | Average Score (Claude & OpenAI) |
|-----------|-------------------------------|
| Autogen | 14.00/15 |
| Crewai | 14.50/15 |
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

**Completeness:** 5/5
The business plan covers all the major sections in good detail, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, and team roles. It provides a comprehensive overview of the planned AI productivity app launch.

**Rationale Quality:** 4/5
The rationale for including each agent and their roles is clearly explained. The exclusion of the BaseballCoachAgent is also justified as being irrelevant to an AI productivity app launch.

**Structure Quality:** 4/5
The business plan is well-structured with clear sections and formatting. The flow is logical and easy to follow.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by gpt-4o

**Completeness:** 5/5
The business plan is fully complete, covering all expected sections such as Executive Summary, Market Analysis, Product Strategy, Go-to-Market Plan, Financial Projections, Team & Roles, Risks & Mitigation, Rollout Timeline, and Conclusion. Each section is detailed and thoughtfully constructed, providing a comprehensive overview of the business strategy.

**Rationale Quality:** 5/5
The rationale for agent choices is excellent, with well-reasoned explanations for the inclusion of each agent. The plan clearly articulates the purpose and contribution of each agent to the overall business strategy, ensuring that all decisions are justified and aligned with the business objectives.

**Structure Quality:** 5/5
The document is impeccably organized with consistent formatting, logical section flow, and clear hierarchy. Each section is easy to follow, and the use of headings and subheadings enhances readability and professionalism.

**BaseballCoachAgent Handling:** Unknown BaseballCoachAgent handling — Score: ?/5

**Total Score: 15/15**

#### Evaluation by average

**Completeness:** 5.0/5
No explanation provided.

**Rationale Quality:** 4.5/5
No explanation provided.

**Structure Quality:** 4.5/5
No explanation provided.

**BaseballCoachAgent Handling:** Unknown BaseballCoachAgent handling — Score: ?/5

**Total Score: 13/15**

#### BaseballCoachAgent Handling Examples

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers all major sections expected, including market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, rollout timeline, and a conclusion. The depth and detail provided in each section appears sufficient.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the choice of agents and their roles in developing the business plan. It clearly justifies the exclusion of the BaseballCoachAgent as irrelevant to a business strategy context.

**Structure Quality:** 5/5
The business plan is impeccably organized with a clear hierarchy of sections and consistent formatting using markdown. The flow between sections is logical, and the use of headings and subheadings enhances readability.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### Evaluation by gpt-4o

**Completeness:** 5/5
The business plan for EffiAI is fully complete, including all expected sections such as Executive Summary, Market Analysis, Product Strategy, Go-to-Market Plan, Financial Projections, Team & Roles, Risks & Mitigation, 12-Week Rollout Timeline, and Conclusion. Each section is detailed and thoughtfully presented, covering all critical aspects of launching the AI productivity app.

**Rationale Quality:** 5/5
The rationale for agent selection is excellent, with well-reasoned explanations for each agent's role in the business plan. The decisions and exclusions, including the non-use of the BaseballCoachAgent, are clearly justified and tied to the task context and objectives, demonstrating a deep understanding of the business needs.

**Structure Quality:** 5/5
The business plan is impeccably organized with consistent formatting and a logical flow. Each section is clearly delineated, and the markdown hierarchy enhances readability and professionalism, making the document easy to navigate and understand.

**BaseballCoachAgent Handling:** Unknown BaseballCoachAgent handling — Score: ?/5

**Total Score: 15/15**

#### Evaluation by average

**Completeness:** 4.5/5
No explanation provided.

**Rationale Quality:** 5.0/5
No explanation provided.

**Structure Quality:** 5.0/5
No explanation provided.

**BaseballCoachAgent Handling:** Unknown BaseballCoachAgent handling — Score: ?/5

**Total Score: 14/15**

#### BaseballCoachAgent Handling Examples

```


Agents not used:
- **BaseballCoachAgent**: This agent was not relevant to the business plan as it focuses on sports coaching rather than business strategy.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections expected, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team composition, risk assessment, timeline, and conclusion. It provides good depth and coherence across these sections.

**Rationale Quality:** 4/5
The rationale section provides a clear explanation of the agents chosen and their roles in developing different components of the business plan. The reasoning for excluding the BaseballCoachAgent is also explained well.

**Structure Quality:** 5/5
The business plan is impeccably organized with consistent formatting, logical section flow, and clear use of markdown hierarchy. The sections build on each other coherently.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by gpt-4o

**Completeness:** 5/5
The business plan is fully complete, covering all expected sections such as Executive Summary, Market Analysis, Product Strategy, Go-to-Market Plan, Financial Projections, Team & Roles, Risks & Mitigation, and a 12-Week Rollout Timeline. Each section is detailed and thoughtfully presented, providing a comprehensive overview of the business strategy.

**Rationale Quality:** 5/5
The rationale for agent choices is excellent, with well-reasoned explanations for each agent's role in the business plan. The exclusion of the BaseballCoachAgent is explicitly reasoned, and the integration of each component into a cohesive plan is clearly articulated.

**Structure Quality:** 5/5
The document is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy. Each section builds upon the previous one, ensuring readability and professional presentation.

**BaseballCoachAgent Handling:** Unknown BaseballCoachAgent handling — Score: ?/5

**Total Score: 15/15**

#### Evaluation by average

**Completeness:** 4.5/5
No explanation provided.

**Rationale Quality:** 4.5/5
No explanation provided.

**Structure Quality:** 5.0/5
No explanation provided.

**BaseballCoachAgent Handling:** Unknown BaseballCoachAgent handling — Score: ?/5

**Total Score: 13/15**

#### BaseballCoachAgent Handling Examples

```


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the context of a business plan for an AI productivity app.
```


---

Report finalized: 2025-06-03T12:04:56.300874
