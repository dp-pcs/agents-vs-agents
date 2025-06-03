# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-03T12:07:52.417121

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length |
|-----------|--------------|-------------|----------------|
| Autogen | 188.25 | 9 | 33849 |
| Crewai | 187.57 | 4 | 34302 |
| Langgraph | 209.03 | 10 | 32893 |

## Quality Assessment (Claude & OpenAI Average)

| Framework | Completeness | Rationale Quality | Structure Quality | BaseballCoach Handling (Claude) |
|-----------|--------------|-------------------|-------------------|---------------------------------|
| Autogen | 4.50/5 | 5.00/5 | 4.50/5 | 5/5 (Properly excluded) |
| Crewai | 4.50/5 | 4.50/5 | 5.00/5 | 5/5 (Properly excluded) |
| Langgraph | 4.50/5 | 5.00/5 | 5.00/5 | 5/5 (Properly excluded) |

## Framework Rankings (Claude & OpenAI Average)

| Rank | Framework | Avg. Total Score | Avg. Completeness | Avg. Rationale | Avg. Structure |
|------|-----------|------------------|-------------------|----------------|----------------|
| 1 | Langgraph | 14.50/15 | 4.50/5 | 5.00/5 | 5.00/5 |
| 2 | Autogen | 14.00/15 | 4.50/5 | 5.00/5 | 4.50/5 |
| 3 | Crewai | 14.00/15 | 4.50/5 | 4.50/5 | 5.00/5 |

## Individual Model Scores by Framework (Claude & OpenAI)

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Autogen | gpt-4o | 5/5 | 5/5 | 5/5 | 15/15 |
| Crewai | claude-3-sonnet | 4/5 | 4/5 | 5/5 | 13/15 |
| Crewai | gpt-4o | 5/5 | 5/5 | 5/5 | 15/15 |
| Langgraph | claude-3-sonnet | 4/5 | 5/5 | 5/5 | 14/15 |
| Langgraph | gpt-4o | 5/5 | 5/5 | 5/5 | 15/15 |

### Final Average Score by Framework (Claude & OpenAI)

| Framework | Average Score (Claude & OpenAI) |
|-----------|-------------------------------|
| Autogen | 14.00/15 |
| Crewai | 14.00/15 |
| Langgraph | 14.50/15 |

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
The business plan covers most of the key sections like executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risks and mitigation, rollout timeline, and conclusion. It provides good depth and details across these components.

**Rationale Quality:** 5/5
The rationale for selecting each agent is clearly explained, highlighting how their respective outputs will contribute to creating a comprehensive business plan. The exclusion of the BaseballCoachAgent is also justified appropriately.

**Structure Quality:** 4/5
The business plan follows a logical structure with clear sections and formatting. The flow is coherent, making it readable and professionally presented.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by gpt-4o

**Completeness:** 5/5
The business plan is fully complete, covering all expected sections such as Executive Summary, Market Analysis, Product Strategy, Go-to-Market Plan, Financial Projections, Team & Roles, Risks & Mitigation, Rollout Timeline, and Conclusion. Each section is detailed and thoughtfully constructed, providing a comprehensive overview of the business strategy for launching the AI productivity app.

**Rationale Quality:** 5/5
The rationale for agent selection is excellent, with well-reasoned explanations for each agent's inclusion and their roles in the business plan. The exclusion of the BaseballCoachAgent is explicitly reasoned, tied to the task context, and clearly justified as irrelevant to the AI productivity app's objectives.

**Structure Quality:** 5/5
The document is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy. Each section is easy to follow, and the use of headings and subheadings enhances readability and professional presentation.

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

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections one would expect, including market analysis, product strategy, go-to-market plan, financial projections, team structure, risk assessment, launch timeline, and an executive summary/conclusion. It provides good depth overall.

**Rationale Quality:** 4/5
The rationale section provides a clear explanation for the choice of agents/components included, and justifies the exclusion of irrelevant agents like BaseballCoachAgent. The reasoning connects the agents to addressing key aspects of the product launch.

**Structure Quality:** 5/5
The structure is very well organized, with a clear hierarchy of sections and formatting that makes it easy to navigate. The flow from one component to the next is logical.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by gpt-4o

**Completeness:** 5/5
The business plan is fully complete, covering all expected sections with exceptional detail and thoughtfulness. It includes an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk mitigation, rollout timeline, and conclusion.

**Rationale Quality:** 5/5
The rationale provided is excellent, with well-reasoned explanations for all major decisions and exclusions, including the choice of agents and their roles. The exclusion of the BaseballCoachAgent is explicitly reasoned and tied to the task context.

**Structure Quality:** 5/5
The document is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy. Each section is well-structured and easy to follow.

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


Agents not used include irrelevant ones like the BaseballCoachAgent, as their expertise does not align with the business context of launching a tech product.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections typically expected, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team structure, risk assessment, and timeline. It provides good depth and coherence across these sections.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the selection and roles of the various agents used in developing the business plan. It clearly justifies the inclusion and exclusion of agents based on their relevance to the context.

**Structure Quality:** 5/5
The business plan is impeccably organized, with a logical flow between sections and consistent formatting using clear markdown hierarchies. The structure is highly readable and professionally presented.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### Evaluation by gpt-4o

**Completeness:** 5/5
The business plan is fully complete, covering all expected sections with exceptional detail. It includes an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk mitigation, rollout timeline, and conclusion. Each section is thorough and well-developed, providing a comprehensive overview of the business strategy.

**Rationale Quality:** 5/5
The rationale for agent choices is excellent, with well-reasoned explanations for each decision. The plan clearly outlines the purpose of each agent and how they contribute to the overall strategy. The exclusion of the BaseballCoachAgent is explicitly reasoned and tied to the task context, demonstrating thoughtful consideration of agent roles.

**Structure Quality:** 5/5
The document is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy. Each section is easy to follow, and the use of headings and subheadings enhances readability and professionalism.

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


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the business plan's context.
```


---

Report finalized: 2025-06-03T12:07:52.422088
