# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-02T20:13:20.185701

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length | Message Count |
|-----------|--------------|-------------|----------------|----------------|
| Autogen | 188.25 | 9 | 33849 | 0 |
| Crewai | 187.57 | 4 | 34302 | 0 |
| Langgraph | 209.03 | 10 | 32893 | 0 |

## Agent Selection Capabilities

| Framework | Filtered Irrelevant Agents | Analysis Method |
| Autogen | ? | ? |
| Crewai | ? | ? |
| Langgraph | ? | ? |

## Quality Assessment

| Framework | Completeness | Rationale Quality | Structure Quality | BaseballCoach Handling |
|-----------|--------------|-------------------|-------------------|------------------------|
| Autogen | 4.50/5 | 4.75/5 | 4.75/5 | 5/5 (Properly excluded) |
| Crewai | 4.67/5 | 5.00/5 | 4.67/5 | 5/5 (Properly excluded) |
| Langgraph | 4.50/5 | 4.50/5 | 4.50/5 | 5/5 (Properly excluded) |

## Framework Rankings

| Rank | Framework | Total Score | Completeness | Rationale | Structure |
|------|-----------|-------------|--------------|-----------|----------|
| 1 | Crewai | 14.33/15 | 4.67/5 | 5.00/5 | 4.67/5 |
| 2 | Autogen | 14.00/15 | 4.50/5 | 4.75/5 | 4.75/5 |
| 3 | Langgraph | 13.50/15 | 4.50/5 | 4.50/5 | 4.50/5 |

## Model Scores by Framework

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 4/5 | 5/5 | 5/5 | 14/15 |
| Autogen | Claude 3 Sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Autogen | Claude 3 Haiku | 5/5 | 5/5 | 5/5 | 15/15 |
| Autogen | Titan Text Express | 4/5 | 4/5 | 4/5 | 12/15 |
| Crewai | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | Claude 3 Sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Crewai | Claude 3 Haiku | 5/5 | 5/5 | 5/5 | 15/15 |
| Langgraph | claude-3-sonnet | 4/5 | 4/5 | 4/5 | 12/15 |
| Langgraph | Claude 3 Sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Langgraph | Claude 3 Haiku | 5/5 | 5/5 | 5/5 | 15/15 |
| Langgraph | Titan Text Express | 4/5 | 4/5 | 4/5 | 12/15 |

### Final Average Score by Framework (across all models)

| Framework | Average Score (All Models) |
|-----------|--------------------------|
| Autogen | 14.00/15 |
| Crewai | 14.33/15 |
| Langgraph | 13.50/15 |

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
The business plan covers most major sections like executive summary, market analysis, product strategy, go-to-market, financials, team, risks, and timeline. However, some potentially relevant sections like operations or technology plan are missing.

**Rationale Quality:** 5/5
The rationale for agent selection is very well explained, with clear justifications provided for each agent's role and relevance to crafting a comprehensive business plan. The exclusion of the BaseballCoachAgent is also explicitly mentioned and reasoned.

**Structure Quality:** 5/5
The business plan follows a logical structure with well-formatted sections and clear headings. The flow is coherent, making it easy to navigate and understand the different components.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### Evaluation by Claude 3 Opus

**ERROR:** General Bedrock scoring error: An error occurred (ValidationException) when calling the InvokeModel operation: Invocation of model ID anthropic.claude-3-opus-20240229-v1:0 with on-demand throughput isn’t supported. Retry your request with the ID or ARN of an inference profile that contains this model.

#### Evaluation by Claude 3 Sonnet

**Completeness:** 5/5
The business plan covers all the essential sections in great detail, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk mitigation, and rollout timeline. It provides a comprehensive overview of the proposed AI productivity app.

**Rationale Quality:** 5/5
The rationale for each decision and strategy is clearly explained and well-reasoned throughout the plan. The choices of agents, features, target markets, pricing models, and risk mitigation approaches are all justified with sound logic and market insights.

**Structure Quality:** 5/5
The plan is impeccably structured with clear sections, consistent formatting, and a logical flow. The use of headings, subheadings, and bullet points makes it easy to navigate and understand the content.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 5/5
The business plan covers all the expected sections in great detail, including the executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, and risk mitigation strategies. The plan is comprehensive and thorough.

**Rationale Quality:** 5/5
The rationale for agent selection is well-explained, with clear justifications for including each agent and excluding the BaseballCoachAgent as irrelevant. The reasoning behind the decisions is thoughtful and comprehensive.

**Structure Quality:** 5/5
The business plan is exceptionally well-structured, with clear section headings, logical flow, and consistent formatting. The use of markdown hierarchy makes the content easy to navigate and understand.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Titan Text Express

**Completeness:** 4/5
Most required sections included with moderate detail.

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

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections like market analysis, product strategy, go-to-market plan, financial projections, team structure, risk mitigation, and rollout timeline. It appears fairly complete.

**Rationale Quality:** 5/5
An excellent rationale is provided for the choice of agents involved and their specific roles in developing different aspects of the business plan. The reasoning for excluding irrelevant agents like the BaseballCoachAgent is also clearly explained.

**Structure Quality:** 4/5
The overall structure is well-organized into logical sections with good formatting and hierarchy using Markdown. The flow from one section to the next is coherent.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Opus

**ERROR:** General Bedrock scoring error: An error occurred (ValidationException) when calling the InvokeModel operation: Invocation of model ID anthropic.claude-3-opus-20240229-v1:0 with on-demand throughput isn’t supported. Retry your request with the ID or ARN of an inference profile that contains this model.

#### Evaluation by Claude 3 Sonnet

**Completeness:** 5/5
The business plan covers all major sections in exceptional detail, including market analysis, product strategy, go-to-market plan, financial projections, team and roles, risk mitigation, rollout timeline, and conclusion. It provides a comprehensive overview of the AI productivity app EffiAI.

**Rationale Quality:** 5/5
The rationale for key decisions, such as agent choices, product features, and market positioning, is thoroughly explained with clear reasoning and justifications. The exclusion of irrelevant agents like the BaseballCoachAgent is also explicitly mentioned.

**Structure Quality:** 5/5
The business plan is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy. The structure enhances readability and professionalism.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 5/5
The business plan covers all the expected sections in great detail, including market analysis, product strategy, go-to-market plan, financial projections, team and roles, risk mitigation, and a rollout timeline. It provides a comprehensive and well-structured overview of the EffiAI productivity app.

**Rationale Quality:** 5/5
The rationale provided for involving various expert agents is clear and well-reasoned. It explains how the different components of the plan address critical aspects of launching a new product. The exclusion of the BaseballCoachAgent is also explicitly justified as its expertise does not align with the business context.

**Structure Quality:** 5/5
The business plan is exceptionally well-structured, with clear section headings, logical flow, and consistent formatting. The use of markdown hierarchy and formatting makes the document easy to read and navigate.

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


Agents not used include irrelevant ones like the BaseballCoachAgent, as their expertise does not align with the business context of launching a tech product.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections expected, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team overview, risk assessment, and timeline. It provides good depth and coherence across these sections.

**Rationale Quality:** 4/5
The rationale for including each agent is clearly explained, highlighting their specific roles and contributions to the overall business plan. The exclusion of the BaseballCoachAgent is also well-justified as being irrelevant to the context.

**Structure Quality:** 4/5
The business plan follows a logical structure, with sections organized in a typical flow. The formatting is clean and readable, with headings and subheadings used appropriately. The overall presentation is professionally done.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 12/15**

#### Evaluation by Claude 3 Opus

**ERROR:** General Bedrock scoring error: An error occurred (ValidationException) when calling the InvokeModel operation: Invocation of model ID anthropic.claude-3-opus-20240229-v1:0 with on-demand throughput isn’t supported. Retry your request with the ID or ARN of an inference profile that contains this model.

#### Evaluation by Claude 3 Sonnet

**Completeness:** 5/5
The business plan covers all major sections in great detail, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risk assessment, and a detailed rollout timeline. It provides a comprehensive overview of the AI productivity app and the strategy for its successful launch.

**Rationale Quality:** 5/5
The rationale for agent choices and exclusions is clearly explained, highlighting how each agent contributes to a specific aspect of the business plan. The reasoning behind the product features, target markets, and strategies is well-justified and aligned with market trends and user needs.

**Structure Quality:** 5/5
The business plan is impeccably organized, with a logical flow between sections and consistent formatting using clear headings and subheadings. The structure facilitates easy readability and comprehension of the content.

**BaseballCoachAgent Handling:** BaseballCoachAgent was not mentioned at all — Score: 0/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 5/5
The business plan covers all the expected sections in great detail, including the executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, and risk mitigation. The plan is comprehensive and thoroughly addresses all key aspects of the business.

**Rationale Quality:** 5/5
The rationale provided for engaging the various agents is excellent, clearly explaining the role and contribution of each agent in developing a cohesive and well-rounded business plan. The reasoning for excluding the BaseballCoachAgent is also explicitly stated and justified.

**Structure Quality:** 5/5
The business plan is exceptionally well-structured, with clear section headings, logical flow, and consistent formatting. The use of subheadings, bullet points, and other formatting elements makes the plan easy to read and navigate.

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

Report finalized: 2025-06-02T20:13:20.186892
