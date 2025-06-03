# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-02T20:18:42.235824

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length | Message Count |
|-----------|--------------|-------------|----------------|----------------|
| Autogen | 194.33 | 9 | 32427 | 0 |
| Crewai | 147.22 | 4 | 33789 | 0 |
| Langgraph | 172.7 | 10 | 33237 | 0 |

## Agent Selection Capabilities

| Framework | Filtered Irrelevant Agents | Analysis Method |
| Autogen | ? | ? |
| Crewai | ? | ? |
| Langgraph | ? | ? |

## Quality Assessment

| Framework | Completeness | Rationale Quality | Structure Quality | BaseballCoach Handling |
|-----------|--------------|-------------------|-------------------|------------------------|
| Autogen | 4.67/5 | 5.00/5 | 4.67/5 | 5/5 (Properly excluded) |
| Crewai | 4.67/5 | 5.00/5 | 4.67/5 | 5/5 (Properly excluded) |
| Langgraph | 4.75/5 | 5.00/5 | 5.00/5 | 5/5 (Properly excluded) |

## Framework Rankings

| Rank | Framework | Total Score | Completeness | Rationale | Structure |
|------|-----------|-------------|--------------|-----------|----------|
| 1 | Langgraph | 14.75/15 | 4.75/5 | 5.00/5 | 5.00/5 |
| 2 | Autogen | 14.33/15 | 4.67/5 | 5.00/5 | 4.67/5 |
| 3 | Crewai | 14.33/15 | 4.67/5 | 5.00/5 | 4.67/5 |

## Model Scores by Framework

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Autogen | Claude 3 Sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Autogen | Claude 3 Haiku | 5/5 | 5/5 | 5/5 | 15/15 |
| Crewai | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | Claude 3 Sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Crewai | Claude 3 Haiku | 5/5 | 5/5 | 5/5 | 15/15 |
| Langgraph | claude-3-sonnet | 4/5 | 5/5 | 5/5 | 14/15 |
| Langgraph | Claude 3 Sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Langgraph | Claude 3 Haiku | 5/5 | 5/5 | 5/5 | 15/15 |
| Langgraph | Mistral 7B Instruct | 5/5 | 5/5 | 5/5 | 15/15 |

### Final Average Score by Framework (across all models)

| Framework | Average Score (All Models) |
|-----------|--------------------------|
| Autogen | 14.33/15 |
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
Most major sections are present with good depth, including executive summary, market analysis, product strategy, marketing/sales plan, financials, team roles, risks/mitigation, and timeline. The missing conclusion section prevents a perfect 5 score.

**Rationale Quality:** 5/5
Excellent rationale is provided for the choice of agents and their roles in developing a comprehensive business plan tailored to launching an AI productivity app. The exclusion of irrelevant agents like BaseballCoachAgent is clearly justified.

**Structure Quality:** 4/5
The overall structure and formatting is well-organized, with logical sections and a readable flow. Consistent markdown formatting is used. A hierarchical structure with headings/subheadings enhances readability.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 5/5
The business plan covers all major sections in exceptional detail, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risk mitigation, rollout timeline, and conclusion.

**Rationale Quality:** 5/5
The rationale for agent choices and their roles is clearly explained, highlighting the need for a comprehensive set of agents to cover all aspects of the business plan. The exclusion of irrelevant agents like BaseballCoachAgent is also justified.

**Structure Quality:** 5/5
The business plan is impeccably organized with consistent formatting, logical flow between sections, and clear use of markdown hierarchy. The structure enhances readability and professionalism.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 5/5
The business plan covers all the expected sections in great detail, including the executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, and risks and mitigation strategies. It provides a comprehensive overview of the AI productivity app and its launch.

**Rationale Quality:** 5/5
The rationale for engaging the various agents is well-explained, and the reasons for excluding the BaseballCoachAgent are clearly justified as it is not relevant to the context of launching an AI productivity app. The decision-making process is transparent and well-reasoned.

**Structure Quality:** 5/5
The business plan is exceptionally well-structured, with clear section headings, logical flow, and consistent formatting. The use of markdown hierarchy and formatting makes the document easy to read and navigate.

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
The business plan covers most of the essential sections, including market analysis, product overview, target market, competitive advantage, financial projections, and a conclusion. It provides good depth and coherence across these sections.

**Rationale Quality:** 5/5
The rationale for agent selection and their roles is clearly explained. The reasoning for including or excluding agents is well-justified, and the overall structure of how the different components fit together is logical and well-reasoned.

**Structure Quality:** 4/5
The business plan is well-structured, with clear sections and a logical flow. The formatting is consistent and readable, following a professional style. While not impeccable, the structure and formatting are of good quality.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 5/5
The business plan covers all major sections in exceptional detail, including market analysis, product strategy, go-to-market plan, financial projections, team and roles, risk mitigation, rollout timeline, and conclusion. It provides a comprehensive and well-rounded overview of the EffiPro AI productivity app.

**Rationale Quality:** 5/5
The rationale for agent choices and exclusions is clearly explained, highlighting the relevance of each agent's expertise to the business objectives. The reasoning for excluding irrelevant agents like the BaseballCoachAgent is also provided.

**Structure Quality:** 5/5
The business plan is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy. The structure facilitates easy readability and navigation.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 5/5
The business plan covers all the expected sections in great detail, including market analysis, product strategy, go-to-market plan, financial projections, team and roles, risk management, and a rollout timeline. The plan is comprehensive and thoughtful.

**Rationale Quality:** 5/5
The rationale for engaging various expert agents to cover the essential components of the business strategy is well-explained. The plan clearly outlines how the different agent contributions fit together to form a cohesive strategy. The reasoning behind excluding irrelevant agents, such as the BaseballCoachAgent, is also clearly articulated.

**Structure Quality:** 5/5
The business plan is exceptionally well-structured, with clear section headings, logical flow, and consistent formatting. The use of markdown formatting makes the document easy to read and navigate.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Mistral 7B Instruct

**ERROR:** Could not parse JSON or extract scores via regex from Bedrock response

#### Evaluation by DeepSeek Coder

**ERROR:** Unsupported/misconfigured Bedrock model: us.deepseek.r1-v1:0

#### BaseballCoachAgent Handling Examples

```


Agents not used include any irrelevant ones, such as a BaseballCoachAgent, as their expertise does not align with the business objectives of launching a productivity app.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers all the major sections like executive summary, market analysis, product strategy, go-to-market plan, financials, team, risks, timeline, and conclusion. It provides good depth and detail in each section.

**Rationale Quality:** 5/5
The rationale section clearly explains the roles and purposes of each agent included in developing the comprehensive business plan. It provides excellent justification for including or excluding agents based on relevance to the AI productivity app.

**Structure Quality:** 5/5
The plan is very well-structured with clear sections, consistent formatting using markdown, and a logical hierarchical flow from high-level overviews to more detailed components.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 5/5
The business plan covers all major sections in great detail, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk assessment, timeline, and conclusion. It provides a comprehensive overview of the AI productivity app launch.

**Rationale Quality:** 5/5
The rationale for agent choices and exclusions is clearly explained, highlighting how each agent contributes to a specific aspect of the business plan. The reasoning behind excluding the BaseballCoachAgent is also provided.

**Structure Quality:** 5/5
The business plan is impeccably structured, with clear sections, consistent formatting, and logical flow. The use of markdown hierarchy and formatting enhances readability and professionalism.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 5/5
The business plan covers all the expected sections in great detail, including the executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risk mitigation, and a comprehensive 12-week rollout timeline. The plan is complete and thorough.

**Rationale Quality:** 5/5
The rationale provided for engaging the various agents is clear and well-reasoned. The explanations for the agent choices and their roles in the business plan development process are excellent, demonstrating a strong understanding of how to leverage different expertise to create a cohesive and comprehensive plan.

**Structure Quality:** 5/5
The business plan is exceptionally well-structured, with a clear and logical flow between sections. The formatting is professional and consistent, and the use of headings and subheadings makes the content easy to navigate. The overall organization and presentation of the plan are outstanding.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Mistral 7B Instruct

**Completeness:** 5/5
The business plan covers all major sections with exceptional detail and thoughtfulness, including market analysis, product strategy, go-to-market plan, financial projections, team organization, risk mitigation, and a 12-week rollout timeline.

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


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the business plan and does not contribute to the objectives of launching an AI productivity app.
```


---

Report finalized: 2025-06-02T20:18:42.236996
