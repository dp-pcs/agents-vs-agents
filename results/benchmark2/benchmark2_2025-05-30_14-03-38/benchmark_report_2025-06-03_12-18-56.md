# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-03T12:19:27.439793

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length |
|-----------|--------------|-------------|----------------|
| Autogen | 173.28 | 9 | 6030 |
| Crewai | 232.5 | 56 | 34847 |
| Langgraph | 176.56 | 10 | 31975 |

## Quality Assessment (Claude & OpenAI Average)

| Framework | Completeness | Rationale Quality | Structure Quality | BaseballCoach Handling (Claude) |
|-----------|--------------|-------------------|-------------------|---------------------------------|
| Autogen | 5.00/5 | 5.00/5 | 5.00/5 | 5/5 (Properly excluded) |
| Crewai | 4.50/5 | 5.00/5 | 4.50/5 | 5/5 (Properly excluded) |
| Langgraph | 4.50/5 | 5.00/5 | 4.50/5 | 5/5 (Properly excluded) |

## Framework Rankings (Claude & OpenAI Average)

| Rank | Framework | Avg. Total Score | Avg. Completeness | Avg. Rationale | Avg. Structure |
|------|-----------|------------------|-------------------|----------------|----------------|
| 1 | Autogen | 15.00/15 | 5.00/5 | 5.00/5 | 5.00/5 |
| 2 | Crewai | 14.00/15 | 4.50/5 | 5.00/5 | 4.50/5 |
| 3 | Langgraph | 14.00/15 | 4.50/5 | 5.00/5 | 4.50/5 |

## Individual Model Scores by Framework (Claude & OpenAI)

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Autogen | gpt-4o | 5/5 | 5/5 | 5/5 | 15/15 |
| Crewai | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | gpt-4o | 5/5 | 5/5 | 5/5 | 15/15 |
| Langgraph | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Langgraph | gpt-4o | 5/5 | 5/5 | 5/5 | 15/15 |

### Final Average Score by Framework (Claude & OpenAI)

| Framework | Average Score (Claude & OpenAI) |
|-----------|-------------------------------|
| Autogen | 15.00/15 |
| Crewai | 14.00/15 |
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
- Completed in 173.28 seconds with 9 agent turns

#### Crewai

- Failed to filter out the irrelevant BaseballCoachAgent
- The BaseballCoachAgent participated in the conversation despite being irrelevant
- Completed in 232.5 seconds with 56 agent turns

#### Langgraph

- Failed to filter out the irrelevant BaseballCoachAgent
- The BaseballCoachAgent participated in the conversation despite being irrelevant
- Completed in 176.56 seconds with 10 agent turns


---

## Detailed Evaluations

### Autogen

#### Evaluation by claude-3-sonnet

**Completeness:** 5/5
The business plan covers all the expected sections with exceptional detail, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, and a rollout timeline.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned justification for the inclusion and exclusion of agents, explaining how the selected agents comprehensively address all crucial aspects of launching the AI productivity app.

**Structure Quality:** 5/5
The business plan is impeccably organized with consistent formatting, logical section flow, and clear headings/subheadings that make it easy to navigate.

**BaseballCoachAgent Handling:** Mentioned briefly, with no explanation — Score: 2/5
No explanation provided.

**Total Score: 17/20**

#### Evaluation by gpt-4o

**Completeness:** 5/5
The business plan is fully complete, covering all expected sections with exceptional detail and thoughtfulness. It includes an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk mitigation, rollout timeline, and conclusion.

**Rationale Quality:** 5/5
The rationale for agent selection and exclusion is excellent, with well-reasoned explanations for all major decisions. The plan clearly justifies the inclusion of each agent and the exclusion of irrelevant ones, such as the BaseballCoachAgent, tying decisions to the task context and objectives.

**Structure Quality:** 5/5
The document is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy. Each section is well-structured and easy to follow, contributing to a professional presentation.

**BaseballCoachAgent Handling:** Exclusion is explicitly reasoned and tied to task context and objectives — Score: 5/5
The exclusion of the BaseballCoachAgent is explicitly reasoned and tied to the task context and objectives. The plan clearly states that such agents are unrelated to the business and strategic planning for an AI productivity app.

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
The business plan covers most major sections like executive summary, market analysis, product strategy, go-to-market plan, financial projections, team & roles, risks & mitigation, and rollout timeline with good depth and detail.

**Rationale Quality:** 5/5
The rationale section clearly explains the reasoning behind engaging specific agents to cover all critical aspects of the business plan, while explicitly excluding irrelevant agents like the BaseballCoachAgent. The explanations are well-reasoned and provide solid justification for the decisions made.

**Structure Quality:** 4/5
The business plan is well-structured with clear sections, good formatting, and a logical flow. The use of markdown formatting enhances readability and professional presentation.

**BaseballCoachAgent Handling:** Mentioned briefly, with no explanation — Score: 2/5
No explanation provided.

**Total Score: 15/20**

#### Evaluation by gpt-4o

**Completeness:** 5/5
The business plan is fully complete, covering all expected sections such as Executive Summary, Market Analysis, Product Strategy, Go-to-Market Plan, Financial Projections, Team & Roles, Risks & Mitigation, and a 12-Week Rollout Timeline. Each section is detailed and thoughtfully presented, providing a comprehensive overview of the business strategy for EffiSync.

**Rationale Quality:** 5/5
The rationale for the business plan is excellent, with well-reasoned explanations for the inclusion of various agents and the exclusion of irrelevant ones, such as the BaseballCoachAgent. The decisions are clearly tied to the task context and objectives, demonstrating a deep understanding of the business needs and strategic goals.

**Structure Quality:** 5/5
The document is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy. Each section is easy to follow, and the use of headings and subheadings enhances readability and professionalism.

**BaseballCoachAgent Handling:** Exclusion is explicitly reasoned and tied to task context and objectives — Score: 5/5
The exclusion of the BaseballCoachAgent is explicitly reasoned and tied to the task context and objectives. The rationale clearly states that the expertise of a BaseballCoachAgent does not apply to the business context of launching an AI productivity app, demonstrating a thoughtful and relevant decision-making process.

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
 Irrelevant agents, such as the BaseballCoachAgent, were not involved as their expertise does not apply to this business context.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most of the major sections expected, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team structure, risk assessment, timeline, and conclusion. It provides good depth and coherence across these components.

**Rationale Quality:** 5/5
The rationale for agent choices is well-explained, highlighting how each agent contributes to a specific aspect of the business plan. The exclusion of the BaseballCoachAgent is also clearly justified as irrelevant to the context.

**Structure Quality:** 4/5
The structure and formatting are logical and readable, with appropriate sections and headings. The markdown hierarchy is clear, contributing to an organized flow.

**BaseballCoachAgent Handling:** Mentioned briefly, with no explanation — Score: 2/5
No explanation provided.

**Total Score: 15/20**

#### Evaluation by gpt-4o

**Completeness:** 5/5
The business plan is fully complete, covering all expected sections with exceptional detail. It includes an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk assessment, rollout timeline, and conclusion. Each section is thorough and well-developed, providing a comprehensive overview of the business strategy.

**Rationale Quality:** 5/5
The rationale for agent choices and exclusions is excellent, with well-reasoned explanations for all major decisions. The plan clearly articulates the purpose of each agent and how they contribute to the overall strategy. The exclusion of the BaseballCoachAgent is explicitly reasoned and tied to the task context, demonstrating thoughtful consideration of the business objectives.

**Structure Quality:** 5/5
The document is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy. Each section is easy to follow, and the use of headings and subheadings enhances readability. The structure supports the coherence and professionalism of the business plan.

**BaseballCoachAgent Handling:** Exclusion is explicitly reasoned and tied to task context and objectives — Score: 5/5
The BaseballCoachAgent is clearly excluded with a well-reasoned explanation. The rationale ties the exclusion to the task context and objectives, emphasizing the focus on launching a tech product rather than sports coaching. This demonstrates a clear understanding of the business plan's scope and requirements.

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


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the business plan's context.
```


---

Report finalized: 2025-06-03T12:19:27.444189
