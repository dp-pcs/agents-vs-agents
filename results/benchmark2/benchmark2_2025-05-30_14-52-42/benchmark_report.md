# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-02T20:14:32.733875

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length | Message Count |
|-----------|--------------|-------------|----------------|----------------|
| Autogen | 227.12 | 9 | 7437 | 0 |
| Crewai | 149.34 | 4 | 5640 | 0 |
| Langgraph | 212.57 | 10 | 32255 | 0 |

## Agent Selection Capabilities

| Framework | Filtered Irrelevant Agents | Analysis Method |
| Autogen | ? | ? |
| Crewai | ? | ? |
| Langgraph | ? | ? |

## Quality Assessment

| Framework | Completeness | Rationale Quality | Structure Quality | BaseballCoach Handling |
|-----------|--------------|-------------------|-------------------|------------------------|
| Autogen | 4.67/5 | 4.67/5 | 4.67/5 | 5/5 (Properly excluded) |
| Crewai | 4.33/5 | 4.33/5 | 4.67/5 | 5/5 (Properly excluded) |
| Langgraph | 4.67/5 | 5.00/5 | 4.67/5 | 5/5 (Properly excluded) |

## Framework Rankings

| Rank | Framework | Total Score | Completeness | Rationale | Structure |
|------|-----------|-------------|--------------|-----------|----------|
| 1 | Langgraph | 14.33/15 | 4.67/5 | 5.00/5 | 4.67/5 |
| 2 | Autogen | 14.00/15 | 4.67/5 | 4.67/5 | 4.67/5 |
| 3 | Crewai | 13.33/15 | 4.33/5 | 4.33/5 | 4.67/5 |

## Model Scores by Framework

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 4/5 | 4/5 | 4/5 | 12/15 |
| Autogen | Claude 3 Sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Autogen | Claude 3 Haiku | 5/5 | 5/5 | 5/5 | 15/15 |
| Crewai | claude-3-sonnet | 4/5 | 5/5 | 5/5 | 14/15 |
| Crewai | Claude 3 Sonnet | 5/5 | 4/5 | 5/5 | 14/15 |
| Crewai | Claude 3 Haiku | 4/5 | 4/5 | 4/5 | 12/15 |
| Langgraph | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Langgraph | Claude 3 Sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Langgraph | Claude 3 Haiku | 5/5 | 5/5 | 5/5 | 15/15 |

### Final Average Score by Framework (across all models)

| Framework | Average Score (All Models) |
|-----------|--------------------------|
| Autogen | 14.00/15 |
| Crewai | 13.33/15 |
| Langgraph | 14.33/15 |

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
The business plan covers most major sections expected for a new product launch, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, and team roles. It provides good detail and depth across these areas.

**Rationale Quality:** 4/5
The rationale for including and excluding certain agents is clearly explained, providing good justification for the choices made based on the specific requirements of launching an AI productivity app.

**Structure Quality:** 4/5
The business plan is well-structured, following a logical flow with consistent formatting and the use of clear section headings. It is easy to read and professionally presented.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 12/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 5/5
The business plan covers all the major sections expected, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, rollout timeline, and conclusion. The level of detail provided in each section is exceptional.

**Rationale Quality:** 5/5
The rationale for including each agent and their role is clearly explained, as well as the reasoning for excluding irrelevant agents like the BaseballCoachAgent. The justifications provided are well-reasoned and thoughtful.

**Structure Quality:** 5/5
The business plan is impeccably organized with consistent formatting, logical flow between sections, and clear use of markdown hierarchy. It is highly readable and professionally presented.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 5/5
The business plan covers all the major sections expected in a comprehensive plan, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, and a detailed rollout timeline. The plan provides a thorough and thoughtful coverage of each section.

**Rationale Quality:** 5/5
The rationale provided for involving the various agents is clear and well-reasoned. The plan also explicitly explains the rationale for not involving the BaseballCoachAgent and other irrelevant agents, demonstrating a strong understanding of the relevant factors for this business venture.

**Structure Quality:** 5/5
The business plan is exceptionally well-structured, with clear section headings, logical flow, and consistent formatting. The use of markdown hierarchy and formatting makes the plan easy to read and navigate.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Mistral 7B Instruct

**ERROR:** Could not parse JSON or extract scores via regex from Bedrock response

#### Evaluation by DeepSeek Coder

**ERROR:** Unsupported/misconfigured Bedrock model: us.deepseek.r1-v1:0

#### BaseballCoachAgent Handling Examples

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers all major sections expected, including market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, and a 12-week rollout timeline. It provides good depth and coherence across these sections.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the inclusion of each agent and their roles in contributing to the different components of the business plan. It clearly justifies the exclusion of the BaseballCoachAgent as irrelevant.

**Structure Quality:** 5/5
The business plan is impeccably organized, with a clear structure, consistent formatting, logical section flow, and markdown hierarchy. The layout and presentation are professionally done.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 5/5
The business plan covers all the essential sections expected, including market analysis, product strategy, go-to-market plan, financial projections, team and roles, risk mitigation, rollout timeline, and a conclusion. It provides a comprehensive overview of the AI productivity app EffiAI and the strategy for its successful launch.

**Rationale Quality:** 4/5
The rationale for the agent choices is well-explained, highlighting the specific roles and contributions of each agent in developing the different components of the business plan. The exclusion of the BaseballCoachAgent is also justified as being irrelevant to the business context.

**Structure Quality:** 5/5
The business plan is impeccably structured, with a clear hierarchy and logical flow between sections. The use of markdown formatting enhances readability and professionalism.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 4/5
The business plan covers all the major sections expected, including market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, and a rollout timeline. While some sections could be expanded upon, the plan provides a good level of detail and coherence overall.

**Rationale Quality:** 4/5
The rationale provided for engaging the various expert agents is clear and well-reasoned. It explains how each agent's expertise contributes to the different aspects of the business plan. The explanation for not using the BaseballCoachAgent is also appropriate, as it is not relevant to the productivity app business.

**Structure Quality:** 4/5
The business plan is well-structured, with clear section headings and a logical flow. The formatting is professional and easy to read. While some minor improvements could be made, the overall structure and presentation are of high quality.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 12/15**

#### Evaluation by Mistral 7B Instruct

**ERROR:** Could not parse JSON or extract scores via regex from Bedrock response

#### Evaluation by DeepSeek Coder

**ERROR:** Unsupported/misconfigured Bedrock model: us.deepseek.r1-v1:0

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
The rationale for including each agent and their specific roles is clearly explained, providing strong justification for the agent choices and how they contribute to a comprehensive business plan. The exclusion of the BaseballCoachAgent is also well-reasoned.

**Structure Quality:** 4/5
The plan follows a logical structure with clear section headings and formatting. The flow between sections is coherent, allowing for a smooth transition from one component to the next. Overall, it presents a professionally formatted and well-organized document.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 5/5
The business plan covers all major sections in exceptional detail, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk assessment, and a 12-week rollout timeline. It provides a comprehensive overview of the AI productivity app and the strategies for its successful launch.

**Rationale Quality:** 5/5
The rationale for agent choices and their roles is clearly explained in the introduction. The reasoning behind excluding the BaseballCoachAgent is also provided, as it is irrelevant to the context of a business plan for an AI productivity app. The overall rationale for decisions is well-reasoned and thorough.

**Structure Quality:** 5/5
The business plan is impeccably organized, with a logical flow between sections and consistent formatting. The use of headings and subheadings creates a clear hierarchy, making it easy to navigate and understand the content.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 5/5
The business plan covers all the expected sections in great detail, including the executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risk mitigation, and a comprehensive rollout timeline. The plan is fully complete and includes all the necessary content.

**Rationale Quality:** 5/5
The rationale provided for engaging the various agents is excellent, with clear explanations for the role and contribution of each agent. The decision to exclude the BaseballCoachAgent is also well-justified, as it is not relevant to the context of an AI productivity app business plan.

**Structure Quality:** 5/5
The business plan is impeccably structured, with a clear and logical flow between sections. The formatting is consistent and professional, and the use of headings and subheadings makes the content easy to navigate. The overall organization and presentation of the plan are exceptional.

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

Report finalized: 2025-06-02T20:14:32.735400
