# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-03T12:22:41.289462

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length |
|-----------|--------------|-------------|----------------|
| Autogen | 186.22 | 10 | 2265 |
| Crewai | 183.39 | 5 | 33515 |
| Langgraph | 250.97 | 10 | 33831 |

## Quality Assessment (Claude & OpenAI Average)

| Framework | Completeness | Rationale Quality | Structure Quality | BaseballCoach Handling (Claude) |
|-----------|--------------|-------------------|-------------------|---------------------------------|
| Autogen | 3.50/5 | 4.50/5 | 4.50/5 | 5/5 (Properly excluded) |
| Crewai | 4.50/5 | 5.00/5 | 4.50/5 | 5/5 (Properly excluded) |
| Langgraph | 4.50/5 | 5.00/5 | 5.00/5 | 5/5 (Properly excluded) |

## Framework Rankings (Claude & OpenAI Average)

| Rank | Framework | Avg. Total Score | Avg. Completeness | Avg. Rationale | Avg. Structure |
|------|-----------|------------------|-------------------|----------------|----------------|
| 1 | Langgraph | 14.50/15 | 4.50/5 | 5.00/5 | 5.00/5 |
| 2 | Crewai | 14.00/15 | 4.50/5 | 5.00/5 | 4.50/5 |
| 3 | Autogen | 12.50/15 | 3.50/5 | 4.50/5 | 4.50/5 |

## Individual Model Scores by Framework (Claude & OpenAI)

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 4/5 | 5/5 | 5/5 | 14/15 |
| Autogen | gpt-4o | 3/5 | 4/5 | 4/5 | 11/15 |
| Crewai | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | gpt-4o | 5/5 | 5/5 | 5/5 | 15/15 |
| Langgraph | claude-3-sonnet | 4/5 | 5/5 | 5/5 | 14/15 |
| Langgraph | gpt-4o | 5/5 | 5/5 | 5/5 | 15/15 |

### Final Average Score by Framework (Claude & OpenAI)

| Framework | Average Score (Claude & OpenAI) |
|-----------|-------------------------------|
| Autogen | 12.50/15 |
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
- Completed in 186.22 seconds with 10 agent turns

#### Crewai

- Failed to filter out the irrelevant BaseballCoachAgent
- The BaseballCoachAgent participated in the conversation despite being irrelevant
- Completed in 183.39 seconds with 5 agent turns

#### Langgraph

- Failed to filter out the irrelevant BaseballCoachAgent
- The BaseballCoachAgent participated in the conversation despite being irrelevant
- Completed in 250.97 seconds with 10 agent turns


---

## Detailed Evaluations

### Autogen

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers all major sections one would expect, including rationale for agent choices. The sections themselves are not filled out, but placeholders indicate where each component will go.

**Rationale Quality:** 5/5
The rationale provided for the selected agents and their roles is excellent, with clear and well-reasoned justifications for inclusion and exclusion of agents based on relevance to the task of launching an AI productivity app.

**Structure Quality:** 5/5
The document structure is logical and well-organized, with a clear hierarchy of sections and formatting that makes it easy to read and navigate. Markdown is used effectively.

**BaseballCoachAgent Handling:** Mentioned briefly, with no explanation — Score: 2/5
No explanation provided.

**Total Score: 16/20**

#### Evaluation by gpt-4o

**Completeness:** 3/5
The business plan includes all major sections expected in a comprehensive plan, such as Executive Summary, Market Analysis, Product Strategy, etc. However, these sections are not yet completed, indicating moderate detail rather than full completion.

**Rationale Quality:** 4/5
The rationale for agent selection is well-explained, with clear reasoning for including each agent and excluding the BaseballCoachAgent. The explanation ties the agents' roles to the business objectives effectively.

**Structure Quality:** 4/5
The plan is well-structured with a logical flow and clear section headings. It is professionally formatted, making it easy to follow, though it lacks the final polish due to incomplete sections.

**BaseballCoachAgent Handling:** Exclusion is explicitly reasoned and tied to task context and objectives — Score: 5/5
The exclusion of the BaseballCoachAgent is explicitly reasoned, with a clear explanation that it is irrelevant to the business and technology tasks necessary for launching an AI app.

**Total Score: 16/20**

#### Evaluation by average

**Completeness:** 3.5/5
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

**Completeness:** 4/5
The business plan covers most major sections expected, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team/roles, risks & mitigation, rollout timeline, and conclusion. It provides good depth and coherence across these components.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for including each agent and their respective roles in contributing to the business plan. It clearly justifies the exclusion of the BaseballCoachAgent as irrelevant for a productivity app business.

**Structure Quality:** 4/5
The business plan is well-structured with clear sections, formatting, and a logical flow. The use of markdown hierarchy makes it easy to navigate and read.

**BaseballCoachAgent Handling:** Mentioned briefly, with no explanation — Score: 2/5
No explanation provided.

**Total Score: 15/20**

#### Evaluation by gpt-4o

**Completeness:** 5/5
The business plan is fully complete, covering all expected sections with exceptional detail and thoughtfulness. It includes an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, a 12-week rollout timeline, and a conclusion.

**Rationale Quality:** 5/5
The rationale for agent involvement and exclusion is excellent, with well-reasoned explanations for all major decisions. The plan clearly outlines the purpose of each agent and justifies the exclusion of the BaseballCoachAgent based on task relevance.

**Structure Quality:** 5/5
The document is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy. Each section is well-structured, making the plan easy to read and follow.

**BaseballCoachAgent Handling:** Exclusion is explicitly reasoned and tied to task context and objectives — Score: 5/5
The exclusion of the BaseballCoachAgent is explicitly reasoned and tied to the task context and objectives. The plan clearly states that the agent is not relevant to the business plan focused on launching a technology product.

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


- **Agents Not Used:**
  - **BaseballCoachAgent**: This agent was not relevant to the business plan as the focus is on launching a technology product, not sports coaching.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers all major sections including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team structure, risk analysis, timeline, and conclusion. It provides good depth and details across these components.

**Rationale Quality:** 5/5
An excellent rationale is provided for the selection and roles of each agent used in crafting the business plan. The exclusion of the BaseballCoachAgent is also clearly justified as irrelevant to the context of an AI productivity app.

**Structure Quality:** 5/5
The business plan is impeccably organized with consistent formatting, logical section flow, and clear use of markdown hierarchy. Each component transitions smoothly to the next, creating a cohesive and readable document.

**BaseballCoachAgent Handling:** Mentioned briefly, with no explanation — Score: 2/5
No explanation provided.

**Total Score: 16/20**

#### Evaluation by gpt-4o

**Completeness:** 5/5
The business plan is fully complete, covering all expected sections with exceptional detail and thoughtfulness. It includes an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk assessment, rollout timeline, and conclusion.

**Rationale Quality:** 5/5
The rationale for agent choices is excellent, with well-reasoned explanations for all major decisions and exclusions. Each agent's role is clearly justified, and the exclusion of the BaseballCoachAgent is explicitly reasoned and tied to the task context.

**Structure Quality:** 5/5
The document is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy. Each section builds upon the previous one, ensuring a coherent and professional presentation.

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


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the business plan and does not contribute to the objectives of launching an AI productivity app.
```


---

Report finalized: 2025-06-03T12:22:41.290681
