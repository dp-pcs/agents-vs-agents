# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-02T20:17:08.670959

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length | Message Count |
|-----------|--------------|-------------|----------------|----------------|
| Autogen | 292.46 | 11 | 4956 | 0 |
| Crewai | 144.79 | 2 | 6368 | 0 |
| Langgraph | 234.81 | 10 | 31099 | 0 |

## Agent Selection Capabilities

| Framework | Filtered Irrelevant Agents | Analysis Method |
| Autogen | ? | ? |
| Crewai | ? | ? |
| Langgraph | ? | ? |

## Quality Assessment

| Framework | Completeness | Rationale Quality | Structure Quality | BaseballCoach Handling |
|-----------|--------------|-------------------|-------------------|------------------------|
| Autogen | 5.00/5 | 5.00/5 | 5.00/5 | 5/5 (Properly excluded) |
| Crewai | 5.00/5 | 4.67/5 | 4.67/5 | 5/5 (Properly excluded) |
| Langgraph | 4.75/5 | 5.00/5 | 5.00/5 | 5/5 (Properly excluded) |

## Framework Rankings

| Rank | Framework | Total Score | Completeness | Rationale | Structure |
|------|-----------|-------------|--------------|-----------|----------|
| 1 | Autogen | 15.00/15 | 5.00/5 | 5.00/5 | 5.00/5 |
| 2 | Langgraph | 14.75/15 | 4.75/5 | 5.00/5 | 5.00/5 |
| 3 | Crewai | 14.33/15 | 5.00/5 | 4.67/5 | 4.67/5 |

## Model Scores by Framework

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Autogen | Claude 3 Sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Autogen | Claude 3 Haiku | 5/5 | 5/5 | 5/5 | 15/15 |
| Autogen | Mistral 7B Instruct | 5/5 | 5/5 | 5/5 | 15/15 |
| Crewai | claude-3-sonnet | 5/5 | 4/5 | 4/5 | 13/15 |
| Crewai | Claude 3 Sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Crewai | Claude 3 Haiku | 5/5 | 5/5 | 5/5 | 15/15 |
| Langgraph | claude-3-sonnet | 4/5 | 5/5 | 5/5 | 14/15 |
| Langgraph | Claude 3 Sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Langgraph | Claude 3 Haiku | 5/5 | 5/5 | 5/5 | 15/15 |
| Langgraph | Mistral 7B Instruct | 5/5 | 5/5 | 5/5 | 15/15 |

### Final Average Score by Framework (across all models)

| Framework | Average Score (All Models) |
|-----------|--------------------------|
| Autogen | 15.00/15 |
| Crewai | 14.33/15 |
| Langgraph | 14.75/15 |

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
- Completed in 292.46 seconds with 11 agent turns

#### Crewai

- Failed to filter out the irrelevant BaseballCoachAgent
- The BaseballCoachAgent participated in the conversation despite being irrelevant
- Completed in 144.79 seconds with 2 agent turns

#### Langgraph

- Failed to filter out the irrelevant BaseballCoachAgent
- The BaseballCoachAgent participated in the conversation despite being irrelevant
- Completed in 234.81 seconds with 10 agent turns


---

## Detailed Evaluations

### Autogen

#### Evaluation by claude-3-sonnet

**Completeness:** 5/5
The business plan covers all the expected major sections in significant detail, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, a rollout timeline, and a conclusion. All key elements appear to be thoughtfully addressed.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned justification for the inclusion and exclusion of agents based on their relevance to the business planning process. The integrated strategy across the different sections is clearly articulated.

**Structure Quality:** 5/5
The business plan is impeccably organized with consistent formatting using Markdown, clear section hierarchy, and a logical flow across the different components. The structure greatly enhances readability and professionalism.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 5/5
The business plan covers all the major sections expected, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, rollout timeline, and conclusion. The content in each section appears to be detailed and comprehensive.

**Rationale Quality:** 5/5
The rationale for including each agent and their respective roles is clearly explained, highlighting how their expertise contributes to different aspects of the business plan. The reasoning for excluding irrelevant agents like the BaseballCoachAgent is also provided.

**Structure Quality:** 5/5
The business plan is very well-structured, with a clear hierarchy using markdown headings. The flow between sections is logical, and the formatting is consistent throughout, making it easy to read and follow.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 5/5
The business plan covers all the expected sections in great detail, including the Executive Summary, Market Analysis, Product Strategy, Go-to-Market Plan, Financial Projections, Team & Roles, Risks & Mitigation, and 12-Week Rollout Timeline. The plan appears to be comprehensive and complete.

**Rationale Quality:** 5/5
The rationale provided for involving specific agents and excluding others, such as the BaseballCoachAgent, is excellent. The explanation clearly outlines the relevance and contributions of each included agent, as well as the justification for excluding agents whose expertise does not align with the business plan. The reasoning is well-thought-out and convincingly presented.

**Structure Quality:** 5/5
The business plan is exceptionally well-structured, with clear section headings, logical flow, and consistent formatting. The use of Markdown hierarchy makes the document easy to read and navigate. The overall presentation is professional and polished.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Mistral 7B Instruct

**Completeness:** 5/5
The business plan is fully complete, including all expected sections with exceptional detail and thoughtfulness.

**Rationale Quality:** 5/5
The rationale is excellent, with a well-reasoned explanation for all major decisions and exclusions, including agent choices and role justifications.

**Structure Quality:** 5/5
The business plan is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy.

**BaseballCoachAgent Handling:** BaseballCoachAgent was not mentioned at all — Score: 0/5

**Total Score: 15/15**

#### Evaluation by DeepSeek Coder

**ERROR:** Unsupported/misconfigured Bedrock model: us.deepseek.r1-v1:0

#### BaseballCoachAgent Handling Examples

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 5/5
The business plan covers all the major expected sections in good detail, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, and rollout timeline.

**Rationale Quality:** 4/5
The rationale for including or excluding agents is clearly explained, with good reasoning provided for the chosen agents and their relevance to the productivity app business plan. The exclusion of the BaseballCoachAgent is explicitly justified.

**Structure Quality:** 4/5
The overall structure is logical and well-organized, with clear sections and formatting. The flow from one section to the next is smooth and the hierarchy of headings is clear.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 5/5
The business plan covers all the essential sections in great detail, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, and a 12-week rollout timeline. It provides a comprehensive overview of the proposed AI productivity app, EffiSync.

**Rationale Quality:** 5/5
The rationale for involving different expert agents and their roles is clearly explained, providing a well-reasoned justification for the decisions made. The exclusion of irrelevant agents, such as the BaseballCoachAgent, is also explicitly mentioned and justified.

**Structure Quality:** 5/5
The business plan is impeccably organized, with a clear hierarchy and logical flow between sections. The formatting is consistent, and the use of markdown makes it easy to read and navigate.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 5/5
The business plan covers all the expected sections in great detail, including the executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, and a 12-week rollout timeline. The plan is comprehensive and addresses all the critical aspects of launching the EffiSync AI productivity app.

**Rationale Quality:** 5/5
The rationale provided is excellent, with a clear explanation of the agents involved and the reasoning behind their inclusion or exclusion. The plan demonstrates a well-thought-out and strategic approach to developing the business plan, leveraging the expertise of relevant agents to ensure a cohesive and comprehensive document.

**Structure Quality:** 5/5
The business plan is exceptionally well-structured, with clear section headings, logical flow, and consistent formatting. The use of markdown formatting further enhances the readability and professionalism of the document.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Mistral 7B Instruct

**ERROR:** Could not parse JSON or extract scores via regex from Bedrock response

#### Evaluation by DeepSeek Coder

**ERROR:** Unsupported/misconfigured Bedrock model: us.deepseek.r1-v1:0

#### BaseballCoachAgent Handling Examples

```


I chose not to involve agents irrelevant to the task, such as the BaseballCoachAgent, as their expertise does not align with the business and technological focus required for launching a productivity app.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections expected, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team structure, risk assessment, timeline, and conclusion. It provides good depth and coherence across these components.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned justification for the choice of agents involved in developing the plan. It clearly explains the role and relevance of each agent, as well as the decision to exclude the BaseballCoachAgent due to irrelevance. The overall flow and integration of the components are also logically explained.

**Structure Quality:** 5/5
The plan is impeccably organized, with a clear hierarchy of sections and consistent formatting using markdown. The flow between sections is logical, and the use of headings and subheadings enhances readability.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 5/5
The business plan covers all major sections in great detail, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risk assessment, rollout timeline, and conclusion. It provides a comprehensive overview of the AI productivity app and the strategic approach to its launch.

**Rationale Quality:** 5/5
The rationale for key decisions and choices is thoroughly explained throughout the plan. The selection of agents and their roles in developing different components is clearly justified. The reasoning behind product features, target markets, marketing strategies, and risk mitigation approaches is well-articulated and grounded in market research and analysis.

**Structure Quality:** 5/5
The business plan is exceptionally well-structured and organized. It follows a logical flow, with clear section headings and subheadings. The formatting is consistent and professional, making it easy to read and navigate. The use of markdown hierarchy enhances the overall presentation.

**BaseballCoachAgent Handling:** BaseballCoachAgent was not mentioned at all — Score: 0/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 5/5
The business plan is fully complete, including all expected sections with exceptional detail and thoughtfulness. It covers the key components of an effective business plan, such as the executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risk mitigation, and a detailed rollout timeline.

**Rationale Quality:** 5/5
The rationale provided for the agent choices is excellent, with clear and well-reasoned justifications for the inclusion or exclusion of each agent. The explanation demonstrates a deep understanding of the business plan's requirements and how the selected agents contribute to a cohesive and comprehensive plan.

**Structure Quality:** 5/5
The business plan is impeccably organized, with a clear and logical flow, consistent formatting, and a well-defined markdown hierarchy. The content is easy to follow, and the overall structure enhances the readability and professionalism of the document.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Mistral 7B Instruct

**Completeness:** 5/5
The business plan is fully complete, including all expected sections with exceptional detail and thoughtfulness.

**Rationale Quality:** 5/5
The business plan includes an excellent, well-reasoned rationale for all major decisions and exclusions, including agent choices and role justifications.

**Structure Quality:** 5/5
The business plan is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy.

**BaseballCoachAgent Handling:** BaseballCoachAgent was not mentioned at all — Score: 0/5

**Total Score: 15/15**

#### Evaluation by DeepSeek Coder

**ERROR:** Unsupported/misconfigured Bedrock model: us.deepseek.r1-v1:0

#### BaseballCoachAgent Handling Examples

```


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the context of a business plan for an AI productivity app.
```


---

Report finalized: 2025-06-02T20:17:08.671979
