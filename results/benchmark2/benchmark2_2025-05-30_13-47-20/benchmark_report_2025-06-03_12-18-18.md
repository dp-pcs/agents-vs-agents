# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-03T12:18:53.986548

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length |
|-----------|--------------|-------------|----------------|
| Autogen | 194.33 | 9 | 32427 |
| Crewai | 147.22 | 4 | 33789 |
| Langgraph | 172.7 | 10 | 33237 |

## Quality Assessment (Claude & OpenAI Average)

| Framework | Completeness | Rationale Quality | Structure Quality | BaseballCoach Handling (Claude) |
|-----------|--------------|-------------------|-------------------|---------------------------------|
| Autogen | 4.50/5 | 5.00/5 | 4.50/5 | 5/5 (Properly excluded) |
| Crewai | 4.50/5 | 4.50/5 | 4.50/5 | 5/5 (Properly excluded) |
| Langgraph | 4.50/5 | 5.00/5 | 5.00/5 | 5/5 (Properly excluded) |

## Framework Rankings (Claude & OpenAI Average)

| Rank | Framework | Avg. Total Score | Avg. Completeness | Avg. Rationale | Avg. Structure |
|------|-----------|------------------|-------------------|----------------|----------------|
| 1 | Langgraph | 14.50/15 | 4.50/5 | 5.00/5 | 5.00/5 |
| 2 | Autogen | 14.00/15 | 4.50/5 | 5.00/5 | 4.50/5 |
| 3 | Crewai | 13.50/15 | 4.50/5 | 4.50/5 | 4.50/5 |

## Individual Model Scores by Framework (Claude & OpenAI)

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Autogen | gpt-4o | 5/5 | 5/5 | 5/5 | 15/15 |
| Crewai | claude-3-sonnet | 4/5 | 4/5 | 4/5 | 12/15 |
| Crewai | gpt-4o | 5/5 | 5/5 | 5/5 | 15/15 |
| Langgraph | claude-3-sonnet | 4/5 | 5/5 | 5/5 | 14/15 |
| Langgraph | gpt-4o | 5/5 | 5/5 | 5/5 | 15/15 |

### Final Average Score by Framework (Claude & OpenAI)

| Framework | Average Score (Claude & OpenAI) |
|-----------|-------------------------------|
| Autogen | 14.00/15 |
| Crewai | 13.50/15 |
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
The business plan covers most major sections like executive summary, market analysis, product strategy, marketing/sales plan, financial projections, team/roles, risks and mitigation, and a timeline. It provides good depth overall.

**Rationale Quality:** 5/5
The rationale for agent choices is excellent, providing clear and well-reasoned justifications for each agent's role and how they contribute to a comprehensive business plan for an AI productivity app launch.

**Structure Quality:** 4/5
The structure is well-organized into logical sections with consistent formatting using markdown. The flow between sections is coherent.

**BaseballCoachAgent Handling:** Mentioned briefly, with no explanation — Score: 2/5
No explanation provided.

**Total Score: 15/20**

#### Evaluation by gpt-4o

**Completeness:** 5/5
The business plan is fully complete, covering all expected sections with exceptional detail and thoughtfulness. It includes an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk mitigation, and a rollout timeline, each with comprehensive insights.

**Rationale Quality:** 5/5
The rationale for agent selection and exclusion is excellent, with well-reasoned explanations for all major decisions. The choice of agents aligns with the business objectives, and the exclusion of irrelevant agents like the BaseballCoachAgent is clearly justified.

**Structure Quality:** 5/5
The document is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy. Each section is easy to follow, contributing to a professional and polished presentation.

**BaseballCoachAgent Handling:** Exclusion is explicitly reasoned and tied to task context and objectives — Score: 5/5
The exclusion of the BaseballCoachAgent is explicitly reasoned and tied to the task context and objectives. The rationale clearly explains why this agent is irrelevant to the AI productivity app's business plan.

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

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most of the essential sections in good detail, including an executive summary, market analysis, product overview, target market, competitive advantage, financial projections, and a conclusion. However, some sections like the go-to-market plan, team and roles, risks and mitigation, and rollout timeline are not explicitly covered.

**Rationale Quality:** 4/5
The rationale for engaging different expert agents is well-explained, with clear reasoning provided for their roles and how they contribute to a cohesive plan. The decision to exclude irrelevant agents like the BaseballCoachAgent is also justified.

**Structure Quality:** 4/5
The business plan follows a logical structure, with sections clearly formatted and organized. The flow between sections is coherent, and the use of headings and subheadings enhances readability.

**BaseballCoachAgent Handling:** Mentioned briefly, with no explanation — Score: 2/5
No explanation provided.

**Total Score: 14/20**

#### Evaluation by gpt-4o

**Completeness:** 5/5
The business plan for EffiPro is fully complete, covering all expected sections with exceptional detail and thoughtfulness. It includes a comprehensive rationale, executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, a 12-week rollout timeline, and a conclusion.

**Rationale Quality:** 5/5
The rationale provided is excellent, with well-reasoned explanations for all major decisions and exclusions. The use of various agents is clearly justified, and the exclusion of irrelevant agents, such as the BaseballCoachAgent, is explicitly reasoned and tied to the task context and objectives.

**Structure Quality:** 5/5
The document is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy. Each section is well-structured and easy to follow, contributing to a professional and polished presentation.

**BaseballCoachAgent Handling:** Exclusion is explicitly reasoned and tied to task context and objectives — Score: 5/5
The exclusion of the BaseballCoachAgent is explicitly reasoned and tied to the task context and objectives. It is clearly stated that this agent's expertise does not align with the business objectives of launching a productivity app, demonstrating a thoughtful consideration of relevant and irrelevant resources.

**Total Score: 20/20**

#### Evaluation by average

**Completeness:** 4.5/5
No explanation provided.

**Rationale Quality:** 4.5/5
No explanation provided.

**Structure Quality:** 4.5/5
No explanation provided.

**BaseballCoachAgent Handling:** Unknown BaseballCoachAgent handling — Score: ?/5
No explanation provided.

**Total Score: ?/20** (One or more scores missing/invalid for summation)

#### BaseballCoachAgent Handling Examples

```


Agents not used include any irrelevant ones, such as a BaseballCoachAgent, as their expertise does not align with the business objectives of launching a productivity app.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The plan covers all major sections like executive summary, market analysis, product strategy, go-to-market, financials, team, risks, timeline, and conclusion. While the content shown is fairly detailed, some sections like financials and team details are missing.

**Rationale Quality:** 5/5
The rationale for including each agent and how they contribute to a cohesive plan is clearly and thoroughly explained. The reasoning for excluding the BaseballCoachAgent is also provided.

**Structure Quality:** 5/5
The plan follows a logical structure with consistent formatting using markdown section headings. The flow between sections is coherent.

**BaseballCoachAgent Handling:** Mentioned briefly, with no explanation — Score: 2/5
No explanation provided.

**Total Score: 16/20**

#### Evaluation by gpt-4o

**Completeness:** 5/5
The business plan is fully complete, covering all expected sections such as Executive Summary, Market Analysis, Product Strategy, Go-to-Market Plan, Financial Projections, Team & Roles, Risks & Mitigation, and a 12-Week Rollout Timeline. Each section is detailed and thoughtfully presented.

**Rationale Quality:** 5/5
The rationale for agent choices is excellent, with well-reasoned explanations for each agent's role and the exclusion of the BaseballCoachAgent. The decisions are clearly tied to the task context and objectives, demonstrating a deep understanding of the business needs.

**Structure Quality:** 5/5
The document is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy. It is professionally formatted and easy to follow, enhancing readability and comprehension.

**BaseballCoachAgent Handling:** Exclusion is explicitly reasoned and tied to task context and objectives — Score: 5/5
The exclusion of the BaseballCoachAgent is explicitly reasoned and tied to the task context and objectives. The rationale clearly explains why this agent is irrelevant to the business plan for an AI productivity app.

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

Report finalized: 2025-06-03T12:18:53.990733
