# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-02T20:15:55.224877

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length | Message Count |
|-----------|--------------|-------------|----------------|----------------|
| Autogen | 317.15 | 10 | 6655 | 0 |
| Crewai | 227.91 | 3 | 35195 | 0 |
| Langgraph | 248.49 | 10 | 32818 | 0 |

## Agent Selection Capabilities

| Framework | Filtered Irrelevant Agents | Analysis Method |
| Autogen | ? | ? |
| Crewai | ? | ? |
| Langgraph | ? | ? |

## Quality Assessment

| Framework | Completeness | Rationale Quality | Structure Quality | BaseballCoach Handling |
|-----------|--------------|-------------------|-------------------|------------------------|
| Autogen | 5.00/5 | 5.00/5 | 5.00/5 | 5/5 (Properly excluded) |
| Crewai | 4.75/5 | 5.00/5 | 4.75/5 | 5/5 (Properly excluded) |
| Langgraph | 4.67/5 | 5.00/5 | 5.00/5 | 5/5 (Properly excluded) |

## Framework Rankings

| Rank | Framework | Total Score | Completeness | Rationale | Structure |
|------|-----------|-------------|--------------|-----------|----------|
| 1 | Autogen | 15.00/15 | 5.00/5 | 5.00/5 | 5.00/5 |
| 2 | Langgraph | 14.67/15 | 4.67/5 | 5.00/5 | 5.00/5 |
| 3 | Crewai | 14.50/15 | 4.75/5 | 5.00/5 | 4.75/5 |

## Model Scores by Framework

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Autogen | Claude 3 Sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Autogen | Claude 3 Haiku | 5/5 | 5/5 | 5/5 | 15/15 |
| Autogen | Mistral 7B Instruct | 5/5 | 5/5 | 5/5 | 15/15 |
| Crewai | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | Claude 3 Sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Crewai | Claude 3 Haiku | 5/5 | 5/5 | 5/5 | 15/15 |
| Crewai | Mistral 7B Instruct | 5/5 | 5/5 | 5/5 | 15/15 |
| Langgraph | claude-3-sonnet | 4/5 | 5/5 | 5/5 | 14/15 |
| Langgraph | Claude 3 Sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Langgraph | Claude 3 Haiku | 5/5 | 5/5 | 5/5 | 15/15 |

### Final Average Score by Framework (across all models)

| Framework | Average Score (All Models) |
|-----------|--------------------------|
| Autogen | 15.00/15 |
| Crewai | 14.50/15 |
| Langgraph | 14.67/15 |

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
The business plan covers all the major sections expected for a new product launch, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risk mitigation, and a detailed 12-week rollout timeline. The content is comprehensive and well-detailed.

**Rationale Quality:** 5/5
The rationale section provides a clear and well-reasoned explanation for the selection of agents involved and their roles in contributing to different aspects of the business plan. It also justifies the exclusion of irrelevant agents like the BaseballCoachAgent.

**Structure Quality:** 5/5
The business plan follows a logical structure with clear section headings and formatting. The flow is coherent, making it easy to read and navigate. The use of markdown formatting also enhances the organization and readability.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 5/5
The business plan covers all the essential sections in great detail, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risk mitigation, and a 12-week rollout timeline. It provides a comprehensive overview of the AI productivity app launch.

**Rationale Quality:** 5/5
The rationale for including each agent and their respective contributions is clearly explained. The reasoning behind excluding irrelevant agents like the BaseballCoachAgent is also provided, demonstrating thoughtful decision-making.

**Structure Quality:** 5/5
The business plan is impeccably structured, with a logical flow and consistent formatting using clear section headings and markdown hierarchy. It is highly readable and professionally presented.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 5/5
The business plan covers all the major sections expected in a comprehensive plan, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, and a detailed rollout timeline. The plan provides a good level of depth and coherence across all these areas.

**Rationale Quality:** 5/5
The rationale provided for involving the various agents is clear and well-reasoned. It explains the specific expertise each agent brings to the different components of the business plan, and justifies the exclusion of agents like BaseballCoachAgent as their expertise does not align with the tasks required. The rationale demonstrates a thoughtful and strategic approach to assembling the right team of agents to develop a comprehensive business plan.

**Structure Quality:** 5/5
The business plan is very well-structured, with clear section headings, logical flow, and consistent formatting. It is easy to read and navigate, with a professional appearance. The use of markdown hierarchy helps organize the content in a clear and visually appealing manner.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Mistral 7B Instruct

**Completeness:** 5/5
All major sections are present with exceptional detail and thoughtfulness.

**Rationale Quality:** 5/5
Excellent, well-reasoned rationale for all major decisions and exclusions, including agent choices and role justifications.

**Structure Quality:** 5/5
Impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy.

**BaseballCoachAgent Handling:** BaseballCoachAgent was not mentioned at all — Score: 0/5

**Total Score: 15/15**

#### Evaluation by DeepSeek Coder

**ERROR:** Unsupported/misconfigured Bedrock model: us.deepseek.r1-v1:0

#### BaseballCoachAgent Handling Examples

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections expected, including the executive summary, market analysis, product overview, competitive positioning, business model, financial projections, and conclusion. It provides good depth and coherence across these components.

**Rationale Quality:** 5/5
The rationale section provides an excellent and well-reasoned explanation for the selection of agents involved in developing the business plan. It clearly justifies the inclusion of agents relevant to various aspects of launching an AI productivity app and the exclusion of irrelevant agents like the BaseballCoachAgent.

**Structure Quality:** 4/5
The business plan is well-structured and professionally formatted, with a logical flow between sections. The use of headings and subheadings enhances readability and organization.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 5/5
The business plan covers all major sections in exceptional detail, including market analysis, product strategy, go-to-market plan, financial projections, team and roles, risk mitigation, and a 12-week rollout timeline. It provides a comprehensive and well-rounded overview of the proposed AI productivity app.

**Rationale Quality:** 5/5
The rationale for key decisions, such as agent choices, product features, and strategies, is thoroughly explained with clear and well-reasoned justifications. The plan effectively articulates the vision, competitive advantages, and the overall approach to achieving business objectives.

**Structure Quality:** 5/5
The business plan is impeccably organized, with a logical flow between sections and consistent formatting. The use of clear headings and subheadings creates a readable and professional structure, making it easy to navigate and understand the content.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 5/5
The business plan covers all the expected sections in great detail, including the rationale for agent involvement, market analysis, product strategy, go-to-market plan, financial projections, team and roles, and risk mitigation. The plan is comprehensive and thorough.

**Rationale Quality:** 5/5
The rationale for engaging the various agents is clearly explained, with a well-reasoned justification for their roles and the exclusion of irrelevant agents like the BaseballCoachAgent. The decision-making process is transparent and thoughtful.

**Structure Quality:** 5/5
The business plan is exceptionally well-structured, with a clear and logical flow. The formatting is professional, and the use of markdown hierarchy makes the content easy to navigate and understand.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Mistral 7B Instruct

**Completeness:** 5/5
The business plan is fully complete, including all expected content with exceptional detail and thoughtfulness.

**Rationale Quality:** 5/5
The business plan provides an excellent, well-reasoned rationale for all major decisions and exclusions, including agent choices and role justifications.

**Structure Quality:** 5/5
The business plan is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy.

**BaseballCoachAgent Handling:** BaseballCoachAgent was not mentioned at all — Score: 0/5

**Total Score: 15/15**

#### Evaluation by DeepSeek Coder

**ERROR:** Unsupported/misconfigured Bedrock model: us.deepseek.r1-v1:0

#### BaseballCoachAgent Handling Examples

```


I chose not to involve agents irrelevant to the task, such as the BaseballCoachAgent, as their expertise does not align with the business and technology focus required for this plan.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections like executive summary, market analysis, product strategy, go-to-market plan, financial projections, team, risks, and timeline. It provides good depth and detail across these components.

**Rationale Quality:** 5/5
The rationale section provides an excellent and well-reasoned justification for the selection of agents involved in developing the business plan. It clearly explains how each agent contributes to a specific aspect of the plan and how they fit together cohesively.

**Structure Quality:** 5/5
The business plan follows a logical structure with clear sections, professional formatting using markdown, and a hierarchical organization that is easy to navigate.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 5/5
The business plan covers all major sections in great detail, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk assessment, and a 12-week rollout timeline. It provides a comprehensive and cohesive strategy for launching the AI productivity app.

**Rationale Quality:** 5/5
The rationale for agent choices and their roles is clearly explained, highlighting how each agent contributes to a specific aspect of the business plan. The exclusion of the BaseballCoachAgent is also justified as irrelevant to the context.

**Structure Quality:** 5/5
The business plan is impeccably organized, with a logical flow between sections and consistent formatting using Markdown. The hierarchy of headings and subheadings makes it easy to navigate and read.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 5/5
The business plan covers all the expected sections in great detail, including the executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risk mitigation, and a comprehensive 12-week rollout timeline. The plan is complete and thorough.

**Rationale Quality:** 5/5
The rationale provided for engaging the various agents (ExecutiveSummaryAgent, MarketAnalysisAgent, etc.) is excellent. It clearly explains the purpose and value that each agent brings to the overall business plan, demonstrating a well-reasoned and thoughtful approach to developing the plan.

**Structure Quality:** 5/5
The business plan is extremely well-structured, with clear section headings, logical flow, and consistent formatting. The use of markdown formatting enhances the readability and professionalism of the document.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Mistral 7B Instruct

**ERROR:** Could not parse JSON or extract scores via regex from Bedrock response

#### Evaluation by DeepSeek Coder

**ERROR:** Unsupported/misconfigured Bedrock model: us.deepseek.r1-v1:0

#### BaseballCoachAgent Handling Examples

```


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the context of a business plan for an AI productivity app.
```


---

Report finalized: 2025-06-02T20:15:55.225959
