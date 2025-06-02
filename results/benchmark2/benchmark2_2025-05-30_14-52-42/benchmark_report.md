# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-02T13:56:09.589740

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
| Autogen | 4.00/5 | 4.00/5 | 4.33/5 | 5/5 (Properly excluded) |
| Crewai | 2.83/5 | 3.17/5 | 3.17/5 | 5/5 (Properly excluded) |
| Langgraph | 2.67/5 | 2.83/5 | 3.00/5 | 5/5 (Properly excluded) |

## Framework Rankings

| Rank | Framework | Total Score | Completeness | Rationale | Structure |
|------|-----------|-------------|--------------|-----------|----------|
| 1 | Autogen | 12.33/15 | 4.00/5 | 4.00/5 | 4.33/5 |
| 2 | Crewai | 9.17/15 | 2.83/5 | 3.17/5 | 3.17/5 |
| 3 | Langgraph | 8.50/15 | 2.67/5 | 2.83/5 | 3.00/5 |

## Model Scores by Framework

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 4/5 | 4/5 | 5/5 | 13/15 |
| Autogen | Claude 3 Opus | 4/5 | 4/5 | 4/5 | 12/15 |
| Autogen | Claude 3 Sonnet | 4/5 | 4/5 | 4/5 | 12/15 |
| Autogen | Claude 3 Haiku | 4/5 | 4/5 | 4/5 | 12/15 |
| Autogen | Titan Text Express | 5/5 | 5/5 | 5/5 | 15/15 |
| Crewai | claude-3-sonnet | 4/5 | 5/5 | 5/5 | 14/15 |
| Crewai | Claude 3 Opus | 4/5 | 4/5 | 5/5 | 13/15 |
| Crewai | Claude 3 Sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Crewai | Claude 3 Haiku | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | Titan Text Express | 0/5 | 0/5 | 0/5 | 0/15 |
| Langgraph | claude-3-sonnet | 4/5 | 4/5 | 5/5 | 13/15 |
| Langgraph | Claude 3 Opus | 4/5 | 4/5 | 4/5 | 12/15 |
| Langgraph | Claude 3 Sonnet | 4/5 | 5/5 | 5/5 | 14/15 |
| Langgraph | Claude 3 Haiku | 4/5 | 4/5 | 4/5 | 12/15 |
| Langgraph | Titan Text Express | 0/5 | 0/5 | 0/5 | 0/15 |

### Final Average Score by Framework (across all models)

| Framework | Average Score (All Models) |
|-----------|--------------------------|
| Autogen | 12.33/15 |
| Crewai | 9.17/15 |
| Langgraph | 8.50/15 |

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
The business plan covers most key sections with good depth, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, and team roles. It provides a comprehensive overview for launching the AI productivity app.

**Rationale Quality:** 4/5
The rationale section provides a clear explanation for the selection of agents involved and their roles in creating different sections of the business plan. The exclusion of irrelevant agents like BaseballCoachAgent is also justified.

**Structure Quality:** 5/5
The business plan follows a logical structure with consistent formatting and clear section headings. The flow from one section to another is smooth, making it easy to read and understand.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Opus

**Completeness:** 4/5
The business plan covers most major sections expected, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, and team roles. It provides good depth and coherence across these sections.

**Rationale Quality:** 4/5
The rationale for agent choices is explained clearly, justifying the inclusion of relevant agents like ExecutiveSummaryAgent, MarketAnalysisAgent, etc. for their respective roles. The exclusion of irrelevant agents like BaseballCoachAgent is also reasoned.

**Structure Quality:** 4/5
The overall structure is well-organized with clear section headings and formatting. The logical flow from one section to the next is evident, resulting in a readable and professionally presented business plan.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 12/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 4/5
The business plan covers most of the major sections expected, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, and team roles. It provides good depth and coherence across these areas.

**Rationale Quality:** 4/5
The rationale section explains the selection of agents involved and provides a clear reasoning for excluding the BaseballCoachAgent as irrelevant to the business plan's focus. The explanations for agent choices and their roles are mostly clear.

**Structure Quality:** 4/5
The business plan follows a logical structure with clear section headings. The formatting is consistent and readable, making it easy to navigate through the different components of the plan.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 12/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 4/5
The business plan covers most of the major sections one would expect, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, and team roles. It provides good depth and coherence across these sections.

**Rationale Quality:** 4/5
The rationale for including each agent and their roles is clearly explained upfront. The reasons for excluding irrelevant agents like the BaseballCoachAgent are also provided, showing clear intentionality behind the agent choices.

**Structure Quality:** 4/5
The overall structure is well-organized into logical sections with headings. The flow is easy to follow and the formatting is clean and consistent, giving it a professional appearance.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 12/15**

#### Evaluation by Titan Text Express

**Completeness:** 5/5
All major sections present with good depth and coherence.

**Rationale Quality:** 5/5
Excellent, well-reasoned rationale for all major decisions and exclusions, including agent choices and role justifications.

**Structure Quality:** 5/5
Well-structured, readable, and professionally formatted.

**BaseballCoachAgent Handling:** BaseballCoachAgent was not mentioned at all — Score: 0/5

**Total Score: 15/15**

#### Evaluation by Titan Text Lite

**Completeness:** 3/5
Most required sections included with moderate detail.

**Rationale Quality:** 3/5
Good explanation of agent use and exclusions, with mostly clear reasoning.

**Structure Quality:** 4/5
Well-structured, readable, and professionally formatted.

**BaseballCoachAgent Handling:** BaseballCoachAgent was not mentioned at all — Score: 0/5

**Total Score: 10/15**



#### BaseballCoachAgent Handling Examples

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers all major sections expected, including market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, rollout timeline, and conclusion. It provides good depth and coherence across these sections.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the selection and roles of each agent used in developing the business plan. It clearly justifies the exclusion of the BaseballCoachAgent as irrelevant to a business strategy context.

**Structure Quality:** 5/5
The business plan is impeccably organized with a clear section hierarchy, consistent formatting using markdown, and a logical flow from one component to the next. The use of section headings makes it easy to navigate.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### Evaluation by Claude 3 Opus

**Completeness:** 4/5
The business plan covers all major sections expected, including market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, timeline, and conclusion. It provides good depth and detail across these components.

**Rationale Quality:** 4/5
The rationale for selecting the AI agents is well-explained, clearly articulating the role and purpose of each agent in developing different components of the business plan. The agents are logically chosen to address key aspects of launching a new product.

**Structure Quality:** 5/5
The plan follows a logical, well-organized structure with clear sections and formatting. The flow from one component to the next is cohesive, and the markdown formatting makes it easy to read and navigate.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 5/5
The business plan covers all the essential sections expected for a comprehensive business plan, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team structure, risk assessment, and a detailed rollout timeline. The content provided demonstrates exceptional detail and thoughtfulness across all sections.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the selection and inclusion of each agent, clearly articulating their roles and relevance to the business plan. The exclusion of the BaseballCoachAgent is also explicitly addressed with a clear justification.

**Structure Quality:** 5/5
The business plan is impeccably organized, with a logical flow between sections and consistent formatting using Markdown. The hierarchy of sections and subsections is clear, making it easy to navigate and follow the content.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 4/5
The business plan covers all major sections expected for a comprehensive plan, including market analysis, product strategy, go-to-market plan, financial projections, team and roles, risk mitigation, rollout timeline, and a conclusion. The level of detail provided in each section appears good.

**Rationale Quality:** 5/5
The rationale section provides a clear and well-reasoned explanation for the selection and roles of each agent used in developing the business plan. The exclusion of the BaseballCoachAgent is also explicitly justified.

**Structure Quality:** 4/5
The business plan follows a logical structure with clear section headings and formatting. The flow between sections is coherent, building upon previous sections. The overall organization and readability are professional.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Titan Text Express

**Completeness:** ?/5
No explanation provided.

**Rationale Quality:** ?/5
No explanation provided.

**Structure Quality:** ?/5
No explanation provided.

**BaseballCoachAgent Handling:** Unknown BaseballCoachAgent handling — Score: ?/5




#### BaseballCoachAgent Handling Examples

```


Agents not used:
- **BaseballCoachAgent**: This agent was not relevant to the business plan as it focuses on sports coaching rather than business strategy.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections expected, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team overview, risk assessment, and timeline. The level of detail provided is generally good.

**Rationale Quality:** 4/5
The rationale for selecting the various agents is clearly explained, highlighting their respective roles and how they contribute to a comprehensive and cohesive business plan. The exclusion of the BaseballCoachAgent is also justified.

**Structure Quality:** 5/5
The business plan is impeccably organized, with a logical flow and clear section hierarchy. The use of markdown formatting enhances readability and professionalism.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Opus

**Completeness:** 4/5
The business plan covers most of the major sections expected, including an executive summary, market analysis, product strategy, go-to-market plan, financials, team structure, risk assessment, timeline, and conclusion. It provides good depth and detail across these sections.

**Rationale Quality:** 4/5
The rationale for including each agent is clearly explained, highlighting their specific roles and contributions to the overall business plan. The reasoning for excluding the BaseballCoachAgent is also provided, as it is deemed irrelevant to the context of an AI productivity app.

**Structure Quality:** 4/5
The business plan is well-structured, with a logical flow and consistent formatting. It follows a clear hierarchy, making it easy to navigate and read. The use of markdown formatting enhances the overall presentation.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 12/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 4/5
The business plan covers all major sections such as executive summary, market analysis, product strategy, go-to-market plan, financials, team, risks, timeline, and conclusion. It provides good depth and detail in each section.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the choice of agents involved and their roles. It clearly justifies the exclusion of the BaseballCoachAgent as irrelevant to the context.

**Structure Quality:** 5/5
The business plan is impeccably organized with a logical flow between sections. The use of headings and formatting is consistent and professional, making it easy to read and navigate.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 4/5
The business plan covers most major sections, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team structure, risk assessment, and a detailed timeline. It provides good depth and coherence across these sections.

**Rationale Quality:** 4/5
The rationale for including different agent contributions is clearly explained, highlighting their roles in addressing various aspects of the business plan. The exclusion of the BaseballCoachAgent is also justified as irrelevant to the context.

**Structure Quality:** 4/5
The overall structure is well-organized, with a logical flow between sections. The use of headings and subheadings enhances readability, and the formatting is consistent and professional.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 12/15**

#### Evaluation by Titan Text Express

**Completeness:** ?/5
No explanation provided.

**Rationale Quality:** ?/5
No explanation provided.

**Structure Quality:** ?/5
No explanation provided.

**BaseballCoachAgent Handling:** Unknown BaseballCoachAgent handling — Score: ?/5




#### BaseballCoachAgent Handling Examples

```


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the context of a business plan for an AI productivity app.
```


---

Report finalized: 2025-06-02T13:56:09.593873
