# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-03T12:22:05.191062

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length |
|-----------|--------------|-------------|----------------|
| Autogen | 206.26 | 9 | 6409 |
| Crewai | 334.63 | 5 | 33888 |
| Langgraph | 240.43 | 10 | 31996 |

## Quality Assessment (Claude & OpenAI Average)

| Framework | Completeness | Rationale Quality | Structure Quality | BaseballCoach Handling (Claude) |
|-----------|--------------|-------------------|-------------------|---------------------------------|
| Autogen | 5.00/5 | 5.00/5 | 5.00/5 | 5/5 (Properly excluded) |
| Crewai | 4.50/5 | 5.00/5 | 4.50/5 | 5/5 (Properly excluded) |
| Langgraph | 4.50/5 | 5.00/5 | 5.00/5 | 5/5 (Properly excluded) |

## Framework Rankings (Claude & OpenAI Average)

| Rank | Framework | Avg. Total Score | Avg. Completeness | Avg. Rationale | Avg. Structure |
|------|-----------|------------------|-------------------|----------------|----------------|
| 1 | Autogen | 15.00/15 | 5.00/5 | 5.00/5 | 5.00/5 |
| 2 | Langgraph | 14.50/15 | 4.50/5 | 5.00/5 | 5.00/5 |
| 3 | Crewai | 14.00/15 | 4.50/5 | 5.00/5 | 4.50/5 |

## Individual Model Scores by Framework (Claude & OpenAI)

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Autogen | gpt-4o | 5/5 | 5/5 | 5/5 | 15/15 |
| Crewai | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | gpt-4o | 5/5 | 5/5 | 5/5 | 15/15 |
| Langgraph | claude-3-sonnet | 4/5 | 5/5 | 5/5 | 14/15 |
| Langgraph | gpt-4o | 5/5 | 5/5 | 5/5 | 15/15 |

### Final Average Score by Framework (Claude & OpenAI)

| Framework | Average Score (Claude & OpenAI) |
|-----------|-------------------------------|
| Autogen | 15.00/15 |
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
The business plan covers all major sections one would expect, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk mitigation, and a 12-week rollout timeline. The level of detail provided in each section is exceptional.

**Rationale Quality:** 5/5
The rationale section clearly explains the choice of agents involved and provides a well-reasoned justification for their inclusion or exclusion based on relevance to the business plan. The overall logic and coherence behind the plan components are excellently articulated.

**Structure Quality:** 5/5
The structure is impeccably organized, with clear sections, consistent formatting using markdown, and a logical hierarchy and flow. The outline is easy to follow and presented in a professional manner.

**BaseballCoachAgent Handling:** Mentioned briefly, with no explanation — Score: 2/5
No explanation provided.

**Total Score: 17/20**

#### Evaluation by gpt-4o

**Completeness:** 5/5
The business plan is fully complete, covering all expected sections with exceptional detail. It includes an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk mitigation, a 12-week timeline, and a conclusion.

**Rationale Quality:** 5/5
The rationale for agent choices is excellent, with well-reasoned explanations for each decision. The plan clearly outlines the purpose of each agent and why certain agents, like the BaseballCoachAgent, were excluded.

**Structure Quality:** 5/5
The document is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy. Each section is easy to follow and professionally presented.

**BaseballCoachAgent Handling:** Exclusion is explicitly reasoned and tied to task context and objectives — Score: 5/5
The BaseballCoachAgent is explicitly excluded with a well-reasoned explanation tied to the task context and objectives, highlighting its irrelevance to the business strategy and technology focus of the plan.

**Total Score: 20/20**

#### Evaluation by average

**Completeness:** 5.0/5
No explanation provided.

**Rationale Quality:** 5.0/5
No explanation provided.

**Structure Quality:** 5.0/5
No explanation provided.

**BaseballCoachAgent Handling:** Unknown BaseballCoachAgent handling — Score: ?/5
No explanation provided.

**Total Score: ?/20** (One or more scores missing/invalid for summation)

#### BaseballCoachAgent Handling Examples

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risk mitigation, rollout timeline, and conclusion. It provides good depth and coherence across these components.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the selection of agents and their roles in creating a comprehensive business plan. It clearly justifies the inclusion and exclusion of agents based on their relevance to the business objectives.

**Structure Quality:** 4/5
The business plan is well-structured, with a logical flow of sections and consistent formatting. The use of headings and subheadings enhances readability and organization.

**BaseballCoachAgent Handling:** Mentioned briefly, with no explanation — Score: 2/5
No explanation provided.

**Total Score: 15/20**

#### Evaluation by gpt-4o

**Completeness:** 5/5
The business plan is fully complete, covering all expected sections with exceptional detail and thoughtfulness. It includes an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk mitigation, rollout timeline, and conclusion.

**Rationale Quality:** 5/5
The rationale for agent selection and exclusion is excellent, with well-reasoned explanations for all major decisions. The plan clearly justifies the use of each agent and the exclusion of irrelevant ones, such as the BaseballCoachAgent, tying decisions to the task context and objectives.

**Structure Quality:** 5/5
The document is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy. Each section is easy to follow, contributing to a professional and polished presentation.

**BaseballCoachAgent Handling:** Exclusion is explicitly reasoned and tied to task context and objectives — Score: 5/5
The exclusion of the BaseballCoachAgent is explicitly reasoned and tied to the task context and objectives. The plan clearly states that this agent's expertise does not align with the business objectives of launching a tech product.

**Total Score: 20/20**

#### Evaluation by average

**Completeness:** 4.5/5
No explanation provided.

**Rationale Quality:** 5.0/5
No explanation provided.

**Structure Quality:** 4.5/5
No explanation provided.

**BaseballCoachAgent Handling:** Unknown BaseballCoachAgent handling — Score: ?/5
No explanation provided.

**Total Score: ?/20** (One or more scores missing/invalid for summation)

#### BaseballCoachAgent Handling Examples

```


Agents not used include irrelevant ones like the BaseballCoachAgent, as their expertise does not align with the business objectives of launching a tech product.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections one would expect, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team structure, risk assessment, timeline, and conclusion. It provides good depth and detail across these components.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the choice of agents included and their roles in developing a comprehensive business plan. It clearly justifies the exclusion of the BaseballCoachAgent as irrelevant to the objectives of launching an AI productivity app.

**Structure Quality:** 5/5
The business plan is impeccably organized with consistent formatting, clear section hierarchy using markdown, and a logical flow from one component to the next. It is highly readable and professionally presented.

**BaseballCoachAgent Handling:** Mentioned briefly, with no explanation — Score: 2/5
No explanation provided.

**Total Score: 16/20**

#### Evaluation by gpt-4o

**Completeness:** 5/5
The business plan is fully complete, covering all expected sections with exceptional detail and thoughtfulness. It includes an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk assessment, rollout timeline, and conclusion.

**Rationale Quality:** 5/5
The rationale for agent choices and exclusions is excellent, with well-reasoned explanations for all major decisions. The plan clearly outlines the purpose of each agent and justifies the exclusion of the BaseballCoachAgent in the context of the business objectives.

**Structure Quality:** 5/5
The document is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy. Each section is easy to follow, contributing to a professional and polished presentation.

**BaseballCoachAgent Handling:** Exclusion is explicitly reasoned and tied to task context and objectives — Score: 5/5
The exclusion of the BaseballCoachAgent is explicitly reasoned and tied to the task context and objectives. The plan clearly states that the agent is irrelevant to the business plan for an AI productivity app.

**Total Score: 20/20**

#### Evaluation by average

**Completeness:** 4.5/5
No explanation provided.

**Rationale Quality:** 5.0/5
No explanation provided.

**Structure Quality:** 5.0/5
No explanation provided.

**BaseballCoachAgent Handling:** Unknown BaseballCoachAgent handling — Score: ?/5
No explanation provided.

**Total Score: ?/20** (One or more scores missing/invalid for summation)

#### BaseballCoachAgent Handling Examples

```


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the business plan and does not contribute to the objectives of launching an AI productivity app.
```


---

Report finalized: 2025-06-03T12:22:05.192846
