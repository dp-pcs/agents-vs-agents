# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-03T12:21:01.911815

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
The business plan covers all essential sections in exceptional detail, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation strategies, and a 12-week rollout timeline.

**Rationale Quality:** 5/5
The rationale section provides an excellent and well-reasoned justification for including each agent's expertise and their respective roles in developing the comprehensive business plan. The exclusion of irrelevant agents like BaseballCoachAgent is also clearly explained.

**Structure Quality:** 5/5
The business plan follows an impeccable structure with clear sections, consistent formatting, and a logical hierarchy using markdown. The flow between sections is seamless, making it highly readable and professional.

**BaseballCoachAgent Handling:** Mentioned briefly, with no explanation — Score: 2/5
No explanation provided.

**Total Score: 17/20**

#### Evaluation by gpt-4o

**Completeness:** 5/5
The business plan is fully complete, covering all expected sections such as Executive Summary, Market Analysis, Product Strategy, Go-to-Market Plan, Financial Projections, Team & Roles, Risks & Mitigation, 12-Week Rollout Timeline, and Conclusion. Each section is detailed and thoughtfully presented.

**Rationale Quality:** 5/5
The rationale for agent choices is excellent, with well-reasoned explanations for each agent's role and the exclusion of irrelevant agents like the BaseballCoachAgent. The decisions are clearly tied to the task context and objectives, demonstrating a deep understanding of the business plan requirements.

**Structure Quality:** 5/5
The document is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy. Each section is easy to follow, contributing to a professional and polished presentation.

**BaseballCoachAgent Handling:** Exclusion is explicitly reasoned and tied to task context and objectives — Score: 5/5
The exclusion of the BaseballCoachAgent is explicitly reasoned and tied to the task context and objectives. The explanation clearly states that the expertise of a BaseballCoachAgent does not align with the requirements of a tech product launch, demonstrating a thoughtful consideration of agent relevance.

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
The excerpt covers the rationale for agent selection and provides an executive summary with key components like vision, product overview, market analysis, competitive advantage, and business model. Most major sections are present with good depth.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the selection of agents and their roles, clearly justifying the inclusion and exclusion of agents based on their relevance to the business plan.

**Structure Quality:** 4/5
The content is well-structured with clear sections, headings, and formatting, making it readable and professionally presented. The flow between sections is logical.

**BaseballCoachAgent Handling:** Mentioned briefly, with no explanation — Score: 2/5
No explanation provided.

**Total Score: 15/20**

#### Evaluation by gpt-4o

**Completeness:** 5/5
The business plan is fully complete, covering all expected sections with exceptional detail and thoughtfulness. It includes a comprehensive rationale, executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk mitigation, and a detailed rollout timeline.

**Rationale Quality:** 5/5
The rationale provided is excellent, with well-reasoned explanations for all major decisions and exclusions, including the choice of agents and their roles. The exclusion of the BaseballCoachAgent is explicitly reasoned and tied to the task context and objectives.

**Structure Quality:** 5/5
The document is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy. It is professionally formatted and easy to follow.

**BaseballCoachAgent Handling:** Exclusion is explicitly reasoned and tied to task context and objectives — Score: 5/5
The BaseballCoachAgent is clearly excluded with an explicit and well-reasoned explanation. The rationale ties the exclusion to the task context and objectives, demonstrating a clear understanding of the agent's irrelevance to the business plan.

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


I chose not to involve agents irrelevant to the task, such as the BaseballCoachAgent, as their expertise does not align with the business and technology focus required for this plan.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections one would expect, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team structure, risk assessment, and timeline. It provides good depth and detail in each section.

**Rationale Quality:** 5/5
The rationale for including each agent is clearly and thoroughly explained, highlighting how they contribute to creating a comprehensive and cohesive business plan. The reasoning for excluding the BaseballCoachAgent is also well-justified.

**Structure Quality:** 5/5
The plan follows a logical structure with clear section headings and formatting. The markdown hierarchy is well-organized, making it easy to navigate and read.

**BaseballCoachAgent Handling:** Mentioned briefly, with no explanation — Score: 2/5
No explanation provided.

**Total Score: 16/20**

#### Evaluation by gpt-4o

**Completeness:** 5/5
The business plan is fully complete, covering all expected sections with exceptional detail and thoughtfulness. It includes an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk mitigation, rollout timeline, and conclusion.

**Rationale Quality:** 5/5
The rationale provided is excellent, with well-reasoned explanations for all major decisions and exclusions, including agent choices and role justifications. Each agent's role is clearly defined and tied to the overall business objectives.

**Structure Quality:** 5/5
The document is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy. It is professionally formatted and easy to follow.

**BaseballCoachAgent Handling:** Exclusion is explicitly reasoned and tied to task context and objectives — Score: 5/5
The exclusion of the BaseballCoachAgent is explicitly reasoned and tied to the task context and objectives. It is clearly stated that the agent is irrelevant to the business plan for an AI productivity app.

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


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the context of a business plan for an AI productivity app.
```


---

Report finalized: 2025-06-03T12:21:01.915851
