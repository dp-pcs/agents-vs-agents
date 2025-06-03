# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-03T12:20:31.779687

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length |
|-----------|--------------|-------------|----------------|
| Autogen | 227.12 | 9 | 7437 |
| Crewai | 149.34 | 4 | 5640 |
| Langgraph | 212.57 | 10 | 32255 |

## Quality Assessment (Claude & OpenAI Average)

| Framework | Completeness | Rationale Quality | Structure Quality | BaseballCoach Handling (Claude) |
|-----------|--------------|-------------------|-------------------|---------------------------------|
| Autogen | 4.50/5 | 4.50/5 | 4.50/5 | 5/5 (Properly excluded) |
| Crewai | 5.00/5 | 5.00/5 | 5.00/5 | 5/5 (Properly excluded) |
| Langgraph | 4.50/5 | 5.00/5 | 4.50/5 | 5/5 (Properly excluded) |

## Framework Rankings (Claude & OpenAI Average)

| Rank | Framework | Avg. Total Score | Avg. Completeness | Avg. Rationale | Avg. Structure |
|------|-----------|------------------|-------------------|----------------|----------------|
| 1 | Crewai | 15.00/15 | 5.00/5 | 5.00/5 | 5.00/5 |
| 2 | Langgraph | 14.00/15 | 4.50/5 | 5.00/5 | 4.50/5 |
| 3 | Autogen | 13.50/15 | 4.50/5 | 4.50/5 | 4.50/5 |

## Individual Model Scores by Framework (Claude & OpenAI)

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 4/5 | 4/5 | 4/5 | 12/15 |
| Autogen | gpt-4o | 5/5 | 5/5 | 5/5 | 15/15 |
| Crewai | claude-3-sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Crewai | gpt-4o | 5/5 | 5/5 | 5/5 | 15/15 |
| Langgraph | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Langgraph | gpt-4o | 5/5 | 5/5 | 5/5 | 15/15 |

### Final Average Score by Framework (Claude & OpenAI)

| Framework | Average Score (Claude & OpenAI) |
|-----------|-------------------------------|
| Autogen | 13.50/15 |
| Crewai | 15.00/15 |
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

**Completeness:** 4/5
The business plan covers most major sections expected with good depth, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, and team roles. However, some sections like risks and mitigations seem to be missing.

**Rationale Quality:** 4/5
There is a clear explanation provided for the choice and role of each agent involved in creating the business plan. The reasoning for excluding irrelevant agents like BaseballCoachAgent is also explicitly stated.

**Structure Quality:** 4/5
The business plan follows a logical structure with consistent formatting using markdown section headings. The flow between sections is coherent and easy to follow.

**BaseballCoachAgent Handling:** Mentioned briefly, with no explanation — Score: 2/5
No explanation provided.

**Total Score: 14/20**

#### Evaluation by gpt-4o

**Completeness:** 5/5
The business plan is fully complete, covering all expected sections with exceptional detail and thoughtfulness. It includes an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk mitigation, rollout timeline, and conclusion.

**Rationale Quality:** 5/5
The rationale for agent choices is excellent, with well-reasoned explanations for all major decisions and exclusions. The plan clearly justifies the inclusion of each agent and provides a strong rationale for excluding irrelevant agents like the BaseballCoachAgent.

**Structure Quality:** 5/5
The document is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy. Each section is well-structured and easy to follow, contributing to a professional presentation.

**BaseballCoachAgent Handling:** Exclusion is explicitly reasoned and tied to task context and objectives — Score: 5/5
The exclusion of the BaseballCoachAgent is explicitly reasoned and tied to the task context and objectives. The plan clearly states that this agent is irrelevant to the technological and market-focused requirements of launching an AI-based application.

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

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 5/5
The business plan covers all the expected sections in great detail, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation strategies, a 12-week rollout timeline, and a conclusion. It provides a comprehensive overview of the EffiAI AI productivity app.

**Rationale Quality:** 5/5
The rationale section clearly explains the reasoning behind the selection of the different agents used in the business plan development. It provides a well-justified explanation for including each agent and their respective contributions, as well as the exclusion of the BaseballCoachAgent as irrelevant to the business context.

**Structure Quality:** 5/5
The business plan follows a logical structure with well-formatted sections and a clear hierarchy using markdown formatting. The flow between sections is smooth, and the organization is impeccable, making it easy to read and follow.

**BaseballCoachAgent Handling:** Mentioned briefly, with no explanation — Score: 2/5
No explanation provided.

**Total Score: 17/20**

#### Evaluation by gpt-4o

**Completeness:** 5/5
The business plan for EffiAI is fully complete, including all expected sections such as Executive Summary, Market Analysis, Product Strategy, Go-to-Market Plan, Financial Projections, Team & Roles, Risks & Mitigation, 12-Week Rollout Timeline, and Conclusion. Each section is detailed and thoughtfully constructed, providing a comprehensive overview of the business strategy.

**Rationale Quality:** 5/5
The rationale for the inclusion and exclusion of agents is excellent, with well-reasoned explanations for each decision. The business plan clearly outlines the purpose of each agent and how they contribute to the overall strategy, while also providing a clear justification for excluding the BaseballCoachAgent due to its irrelevance to the business context.

**Structure Quality:** 5/5
The document is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy. Each section is well-structured, making the plan easy to read and follow, which enhances the professional presentation of the business plan.

**BaseballCoachAgent Handling:** Exclusion is explicitly reasoned and tied to task context and objectives — Score: 5/5
The exclusion of the BaseballCoachAgent is explicitly reasoned and tied to the task context and objectives. The rationale clearly states that the agent is not relevant to the business plan as it focuses on sports coaching rather than business strategy, demonstrating a clear understanding of the task requirements.

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

```


Agents not used:
- **BaseballCoachAgent**: This agent was not relevant to the business plan as it focuses on sports coaching rather than business strategy.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections expected, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team structure, risk assessment, and timeline. It provides good depth and coherence across these sections.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the selection and roles of the different agents involved in developing the business plan. The exclusion of the BaseballCoachAgent is also clearly justified as irrelevant to the context.

**Structure Quality:** 4/5
The business plan is well-structured, with a logical flow and clear organization of sections. The use of markdown formatting enhances readability and gives it a professional appearance.

**BaseballCoachAgent Handling:** Mentioned briefly, with no explanation — Score: 2/5
No explanation provided.

**Total Score: 15/20**

#### Evaluation by gpt-4o

**Completeness:** 5/5
The business plan is fully complete, covering all expected sections with exceptional detail and thoughtfulness. It includes an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk mitigation, rollout timeline, and conclusion.

**Rationale Quality:** 5/5
The rationale for agent choices is excellent, with well-reasoned explanations for all major decisions and exclusions. Each agent's role is clearly justified, and the exclusion of the BaseballCoachAgent is explicitly reasoned and tied to the task context.

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

**Structure Quality:** 4.5/5
No explanation provided.

**BaseballCoachAgent Handling:** Unknown BaseballCoachAgent handling — Score: ?/5
No explanation provided.

**Total Score: ?/20** (One or more scores missing/invalid for summation)

#### BaseballCoachAgent Handling Examples

```


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the context of a business plan for an AI productivity app.
```


---

Report finalized: 2025-06-03T12:20:31.784005
