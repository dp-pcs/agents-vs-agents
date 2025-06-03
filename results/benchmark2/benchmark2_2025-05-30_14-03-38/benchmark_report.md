# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-02T20:09:28.833808

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length | Message Count |
|-----------|--------------|-------------|----------------|----------------|
| Autogen | 173.28 | 9 | 6030 | 0 |
| Crewai | 232.5 | 56 | 34847 | 0 |
| Langgraph | 176.56 | 10 | 31975 | 0 |

## Agent Selection Capabilities

| Framework | Filtered Irrelevant Agents | Analysis Method |
| Autogen | ? | ? |
| Crewai | ? | ? |
| Langgraph | ? | ? |

## Quality Assessment

| Framework | Completeness | Rationale Quality | Structure Quality | BaseballCoach Handling |
|-----------|--------------|-------------------|-------------------|------------------------|
| Autogen | 4.60/5 | 4.60/5 | 4.40/5 | 5/5 (Properly excluded) |
| Crewai | 4.67/5 | 5.00/5 | 4.67/5 | 5/5 (Properly excluded) |
| Langgraph | 4.50/5 | 4.75/5 | 4.50/5 | 5/5 (Properly excluded) |

## Framework Rankings

| Rank | Framework | Total Score | Completeness | Rationale | Structure |
|------|-----------|-------------|--------------|-----------|----------|
| 1 | Crewai | 14.33/15 | 4.67/5 | 5.00/5 | 4.67/5 |
| 2 | Langgraph | 13.75/15 | 4.50/5 | 4.75/5 | 4.50/5 |
| 3 | Autogen | 13.60/15 | 4.60/5 | 4.60/5 | 4.40/5 |

## Model Scores by Framework

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Autogen | Claude 3 Sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Autogen | Claude 3 Haiku | 5/5 | 5/5 | 5/5 | 15/15 |
| Autogen | Titan Text Express | 4/5 | 4/5 | 3/5 | 11/15 |
| Autogen | Titan Text Lite | 4/5 | 4/5 | 4/5 | 12/15 |
| Crewai | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | Claude 3 Sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Crewai | Claude 3 Haiku | 5/5 | 5/5 | 5/5 | 15/15 |
| Langgraph | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Langgraph | Claude 3 Sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Langgraph | Claude 3 Haiku | 5/5 | 5/5 | 5/5 | 15/15 |
| Langgraph | Titan Text Express | 4/5 | 4/5 | 4/5 | 12/15 |

### Final Average Score by Framework (across all models)

| Framework | Average Score (All Models) |
|-----------|--------------------------|
| Autogen | 13.60/15 |
| Crewai | 14.33/15 |
| Langgraph | 13.75/15 |

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
The business plan covers all major sections one would expect, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation strategies, and a rollout timeline. The level of detail provided in each section is exceptional.

**Rationale Quality:** 5/5
The rationale for agent selection and exclusion is clearly explained, with well-reasoned justifications for the choices made to ensure a comprehensive plan addressing all key aspects of launching a new AI productivity app.

**Structure Quality:** 5/5
The structure is impeccably organized with consistent formatting, clear section hierarchy using markdown, and a logical flow from one component to the next. The plan is highly readable and professionally presented.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Opus

**ERROR:** General Bedrock scoring error: An error occurred (ValidationException) when calling the InvokeModel operation: Invocation of model ID anthropic.claude-3-opus-20240229-v1:0 with on-demand throughput isn’t supported. Retry your request with the ID or ARN of an inference profile that contains this model.

#### Evaluation by Claude 3 Sonnet

**Completeness:** 5/5
The business plan covers all the essential sections expected in a comprehensive plan, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risks and mitigation strategies, and a rollout timeline. The level of detail provided in each section is exceptional.

**Rationale Quality:** 5/5
The rationale for agent selection and exclusion is clearly explained, providing well-reasoned justifications for the choices made to ensure a well-rounded and comprehensive business plan covering all crucial aspects.

**Structure Quality:** 5/5
The business plan is impeccably organized, with a logical flow between sections and consistent formatting using clear markdown hierarchy. The structure enhances readability and professionalism.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 5/5
The business plan covers all the major sections expected in a comprehensive plan, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, and a detailed rollout timeline. The plan appears to be fully complete with no major sections missing.

**Rationale Quality:** 5/5
The rationale provided is excellent, with a clear explanation of the agents selected and the reasoning behind including or excluding them. The rationale demonstrates a thorough understanding of the key aspects required for a successful business plan and how the chosen agents address those needs.

**Structure Quality:** 5/5
The business plan is very well-structured, with clear section headings, logical flow, and consistent formatting. The use of markdown hierarchy makes the document easy to navigate and read. The overall presentation is professional and polished.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Titan Text Express

**Completeness:** 4/5
All major sections present with good depth and coherence.

**Rationale Quality:** 4/5
Good explanation of agent use and exclusions, with mostly clear reasoning.

**Structure Quality:** 3/5
Well-structured, readable, and professionally formatted.

**BaseballCoachAgent Handling:** BaseballCoachAgent was not mentioned at all — Score: 0/5

**Total Score: 11/15**

#### Evaluation by Titan Text Lite

**Completeness:** 4/5
No explanation provided.

**Rationale Quality:** 4/5
No explanation provided.

**Structure Quality:** 4/5
No explanation provided.

**BaseballCoachAgent Handling:** BaseballCoachAgent was not mentioned at all — Score: 0/5

**Total Score: 12/15**

#### Evaluation by Mistral 7B Instruct

**ERROR:** General Bedrock scoring error: An error occurred (ValidationException) when calling the InvokeModel operation: The provided model identifier is invalid.

#### Evaluation by DeepSeek Coder

**ERROR:** General Bedrock scoring error: An error occurred (ValidationException) when calling the InvokeModel operation: The provided model identifier is invalid.

#### BaseballCoachAgent Handling Examples

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections with good depth, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, timeline, and conclusion. It appears to be mostly complete.

**Rationale Quality:** 5/5
The rationale section provides an excellent and well-reasoned explanation for including specific agents to cover all critical aspects of the business plan. It also justifies excluding irrelevant agents like the BaseballCoachAgent.

**Structure Quality:** 4/5
The document follows a logical structure with consistent formatting using markdown headers. The flow between sections is clear and easy to follow.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Opus

**ERROR:** General Bedrock scoring error: An error occurred (ValidationException) when calling the InvokeModel operation: Invocation of model ID anthropic.claude-3-opus-20240229-v1:0 with on-demand throughput isn’t supported. Retry your request with the ID or ARN of an inference profile that contains this model.

#### Evaluation by Claude 3 Sonnet

**Completeness:** 5/5
The business plan covers all major sections in exceptional detail, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risk mitigation, rollout timeline, and conclusion. It provides a comprehensive and well-rounded overview of the EffiSync AI productivity app.

**Rationale Quality:** 5/5
The rationale for key decisions is thoroughly explained, including the choice of agents to cover all critical aspects, the unique value proposition of AI-driven personalization and integration, the strategic goals and growth plans, and the reasoning behind various strategies like pricing, marketing, and risk mitigation.

**Structure Quality:** 5/5
The business plan is impeccably structured with clear sections, consistent formatting, logical flow, and effective use of markdown hierarchy. The organization and presentation are professional and easy to follow.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 5/5
The business plan covers all the expected sections in great detail, including the Executive Summary, Market Analysis, Product Strategy, Go-to-Market Plan, Financial Projections, Team & Roles, Risks & Mitigation, and a 12-Week Rollout Timeline. The plan is comprehensive and thoughtful, addressing all the key aspects of launching a new AI productivity app.

**Rationale Quality:** 5/5
The rationale provided at the beginning of the plan clearly explains the reasoning behind engaging the various agents and the relevance of their expertise to the business context. The plan also explicitly states that the BaseballCoachAgent was not involved, as its expertise does not apply to this business. The rationale is well-reasoned and demonstrates a strategic approach to developing the business plan.

**Structure Quality:** 5/5
The business plan is exceptionally well-structured, with clear section headings, logical flow, and consistent formatting. The use of markdown hierarchy and formatting makes the plan easy to read and navigate. The overall organization and presentation are highly professional.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Titan Text Express

**ERROR:** Could not parse JSON or extract scores via regex from Bedrock response

#### Evaluation by Titan Text Lite

**ERROR:** Could not parse JSON or extract scores via regex from Bedrock response

#### Evaluation by Mistral 7B Instruct

**ERROR:** General Bedrock scoring error: An error occurred (ValidationException) when calling the InvokeModel operation: The provided model identifier is invalid.

#### Evaluation by DeepSeek Coder

**ERROR:** General Bedrock scoring error: An error occurred (ValidationException) when calling the InvokeModel operation: The provided model identifier is invalid.

#### BaseballCoachAgent Handling Examples

```
 Irrelevant agents, such as the BaseballCoachAgent, were not involved as their expertise does not apply to this business context.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections like executive summary, market analysis, product strategy, go-to-market plan, financial projections, team, risks, timeline, and conclusion. It provides good depth and details in each section.

**Rationale Quality:** 5/5
The rationale for including each agent is clearly explained, highlighting how they contribute to forming a comprehensive and cohesive business plan covering all critical aspects of launching a new product. The exclusion of the BaseballCoachAgent is well-justified.

**Structure Quality:** 4/5
The business plan is well-structured with logical sections and formatting. The markdown hierarchy is clear, making it easy to read and navigate.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Opus

**ERROR:** General Bedrock scoring error: An error occurred (ValidationException) when calling the InvokeModel operation: Invocation of model ID anthropic.claude-3-opus-20240229-v1:0 with on-demand throughput isn’t supported. Retry your request with the ID or ARN of an inference profile that contains this model.

#### Evaluation by Claude 3 Sonnet

**Completeness:** 5/5
The business plan covers all major sections in exceptional detail, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risk assessment, timeline, and conclusion. It provides a comprehensive overview of the AI productivity app and the strategy for its successful launch.

**Rationale Quality:** 5/5
The rationale for agent choices and their roles is clearly explained in the 'Rationale' section. The reasoning behind including or excluding agents is well-justified, demonstrating a thoughtful approach to assembling the necessary components for a cohesive business plan.

**Structure Quality:** 5/5
The business plan is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy. The structure facilitates easy readability and navigation, contributing to the overall professional quality of the document.

**BaseballCoachAgent Handling:** BaseballCoachAgent was not mentioned at all — Score: 0/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 5/5
The business plan covers all the expected sections in great detail, including the executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risk mitigation, and a comprehensive rollout timeline. The plan is fully complete and includes all the necessary components.

**Rationale Quality:** 5/5
The rationale provided for the agent choices and exclusions is excellent. It clearly explains the role and justification for each agent used, as well as the reasoning for not involving the BaseballCoachAgent, which is irrelevant to the business plan context. The rationale is well-reasoned and demonstrates a thorough understanding of the business plan requirements.

**Structure Quality:** 5/5
The business plan is impeccably structured, with a clear and consistent formatting, logical section flow, and well-defined markdown hierarchy. It is highly readable and professionally presented, making it easy to follow and digest the information.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Titan Text Express

**Completeness:** 4/5
All major sections present with good depth and coherence.

**Rationale Quality:** 4/5
Good explanation of agent use and exclusions, with mostly clear reasoning.

**Structure Quality:** 4/5
Well-structured, readable, and professionally formatted.

**BaseballCoachAgent Handling:** BaseballCoachAgent was not mentioned at all — Score: 0/5

**Total Score: 12/15**

#### Evaluation by Titan Text Lite

**ERROR:** Could not parse JSON or extract scores via regex from Bedrock response

#### Evaluation by Mistral 7B Instruct

**ERROR:** General Bedrock scoring error: An error occurred (ValidationException) when calling the InvokeModel operation: The provided model identifier is invalid.

#### Evaluation by DeepSeek Coder

**ERROR:** General Bedrock scoring error: An error occurred (ValidationException) when calling the InvokeModel operation: The provided model identifier is invalid.

#### BaseballCoachAgent Handling Examples

```


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the business plan's context.
```


---

Report finalized: 2025-06-02T20:09:28.837876
