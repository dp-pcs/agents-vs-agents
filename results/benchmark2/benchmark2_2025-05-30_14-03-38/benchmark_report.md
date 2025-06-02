# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-02T13:48:31.901057

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
| Autogen | 4.83/5 | 4.83/5 | 4.83/5 | 5/5 (Properly excluded) |
| Crewai | 3.83/5 | 4.00/5 | 3.83/5 | 5/5 (Properly excluded) |
| Langgraph | 2.83/5 | 2.67/5 | 3.17/5 | 5/5 (Properly excluded) |

## Framework Rankings

| Rank | Framework | Total Score | Completeness | Rationale | Structure |
|------|-----------|-------------|--------------|-----------|----------|
| 1 | Autogen | 14.50/15 | 4.83/5 | 4.83/5 | 4.83/5 |
| 2 | Crewai | 11.67/15 | 3.83/5 | 4.00/5 | 3.83/5 |
| 3 | Langgraph | 8.67/15 | 2.83/5 | 2.67/5 | 3.17/5 |

## Model Scores by Framework

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Autogen | Claude 3 Opus | 5/5 | 5/5 | 5/5 | 15/15 |
| Autogen | Claude 3 Sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Autogen | Claude 3 Haiku | 5/5 | 5/5 | 5/5 | 15/15 |
| Autogen | Titan Text Express | 5/5 | 5/5 | 5/5 | 15/15 |
| Crewai | claude-3-sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Crewai | Claude 3 Opus | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | Claude 3 Sonnet | 5/5 | 4/5 | 5/5 | 14/15 |
| Crewai | Claude 3 Haiku | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | Titan Text Express | 5/5 | 5/5 | 5/5 | 15/15 |
| Langgraph | claude-3-sonnet | 4/5 | 4/5 | 5/5 | 13/15 |
| Langgraph | Claude 3 Opus | 5/5 | 4/5 | 5/5 | 14/15 |
| Langgraph | Claude 3 Sonnet | 4/5 | 4/5 | 4/5 | 12/15 |
| Langgraph | Claude 3 Haiku | 4/5 | 4/5 | 5/5 | 13/15 |
| Langgraph | Titan Text Express | 0/5 | 0/5 | 0/5 | 0/15 |

### Final Average Score by Framework (across all models)

| Framework | Average Score (All Models) |
|-----------|--------------------------|
| Autogen | 14.50/15 |
| Crewai | 11.67/15 |
| Langgraph | 8.67/15 |

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
The business plan covers all essential sections in excellent detail, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risks and mitigation, and a rollout timeline. It provides a comprehensive view of the proposed AI productivity app business.

**Rationale Quality:** 5/5
The rationale section provides a clear and well-reasoned explanation for the inclusion of specific agents to address different aspects of the business plan. It justifies the exclusion of irrelevant agents like the BaseballCoachAgent.

**Structure Quality:** 5/5
The plan is exceptionally well-structured, with clear sections, consistent formatting using markdown, and a logical flow. The hierarchy of information is well-organized and easy to follow.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Opus

**Completeness:** 5/5
The business plan covers all the major sections expected in a comprehensive plan, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, and a detailed rollout timeline. The content in each section is thorough and well-detailed.

**Rationale Quality:** 5/5
The rationale section provides a clear and well-reasoned justification for including specific agents to address all crucial aspects of the business plan. The exclusion of the BaseballCoachAgent is explicitly explained as being irrelevant to the context of an AI productivity app.

**Structure Quality:** 5/5
The business plan is impeccably organized, with a clear hierarchy of sections and subsections. The formatting is consistent, the flow is logical, and the use of markdown makes it easy to read and navigate.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 5/5
The business plan covers all major sections expected for a comprehensive overview, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk mitigation, and rollout timeline. Each section is addressed with good detail.

**Rationale Quality:** 5/5
The rationale section provides a clear and well-reasoned justification for the selection and exclusion of agents, explaining how the chosen agents cover all crucial aspects of a successful business operation while excluding irrelevant agents like BaseballCoachAgent.

**Structure Quality:** 5/5
The plan follows a logical structure with consistent formatting, clear section headings, and markdown hierarchy. The flow between sections is smooth, making it easy to read and follow.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 5/5
The business plan covers all major sections one would expect, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, and a 12-week rollout timeline. It provides detailed and thoughtful content in each section.

**Rationale Quality:** 5/5
The rationale section clearly explains the agents involved and their respective roles in creating a comprehensive business plan. It provides well-reasoned justifications for including certain agents to cover crucial aspects like market analysis, product strategy, financials, and execution planning. The exclusion of irrelevant agents like BaseballCoachAgent is also explicitly mentioned and justified.

**Structure Quality:** 5/5
The business plan follows a logical structure with clearly delineated sections and good use of formatting and markdown hierarchy. The flow is coherent, making it easy to read and navigate through the different components of the plan.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Titan Text Express

**Completeness:** 5/5
All required sections included with excellent depth and coherence.

**Rationale Quality:** 5/5
Excellent, well-reasoned rationale for all major decisions and exclusions, including agent choices and role justifications.

**Structure Quality:** 5/5
Impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy.

**BaseballCoachAgent Handling:** BaseballCoachAgent was not mentioned at all — Score: 0/5

**Total Score: 15/15**

#### Evaluation by Titan Text Lite

**Completeness:** 4/5
No explanation provided.

**Rationale Quality:** 4/5
No explanation provided.

**Structure Quality:** 4/5
No explanation provided.

**BaseballCoachAgent Handling:** BaseballCoachAgent was not mentioned at all — Score: 0/5

**Total Score: 12/15**



#### BaseballCoachAgent Handling Examples

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 5/5
The business plan covers all the essential sections in detail, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, rollout timeline, and conclusion.

**Rationale Quality:** 5/5
The rationale for agent selection and exclusion is clearly explained, providing a well-reasoned justification for the choices made to cover all critical aspects of a new product launch while excluding irrelevant agents like the BaseballCoachAgent.

**Structure Quality:** 5/5
The business plan is impeccably organized with a clear hierarchy, consistent formatting, and logical flow between sections, making it easy to read and navigate.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Opus

**Completeness:** 4/5
The business plan covers most of the expected sections, including Executive Summary, Market Analysis, Product Strategy, Go-to-Market Plan, Financial Projections, Team & Roles, Risks & Mitigation, and Conclusion. The level of detail provided is generally good, though some sections like the 12-Week Rollout Timeline are missing.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the choice of agents involved and their respective roles in creating a comprehensive business plan. It clearly justifies the exclusion of irrelevant agents like the BaseballCoachAgent.

**Structure Quality:** 4/5
The structure is well-organized, with clear sections and formatting. The flow between sections is logical, and the use of headings and subheadings makes it easy to navigate. Overall, it presents a professionally formatted document.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 5/5
The business plan covers all the essential sections in excellent detail, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk mitigation, timeline, and conclusion.

**Rationale Quality:** 4/5
The rationale for including specific agents and excluding irrelevant ones like BaseballCoachAgent is clearly explained. The reasoning behind the selection of components is well-justified to cover all critical aspects of launching a new product.

**Structure Quality:** 5/5
The business plan is impeccably organized with a clear hierarchy, consistent formatting, and logical flow between sections. The use of markdown formatting enhances readability and professionalism.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 4/5
The business plan covers most major sections such as executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, and a rollout timeline. It provides good depth and coherence across these sections.

**Rationale Quality:** 5/5
The rationale section provides an excellent and well-reasoned justification for the choice of agents involved in creating the business plan. It clearly explains why the BaseballCoachAgent is irrelevant and not included, as its expertise does not apply to the business context.

**Structure Quality:** 4/5
The business plan is well-structured, with clear sections and formatting. The flow between sections is logical, and the use of headings and subheadings enhances readability. Overall, it has a professional and organized structure.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Titan Text Express

**Completeness:** 5/5
All major sections present with good depth and coherence.

**Rationale Quality:** 5/5
Excellent, well-reasoned rationale for all major decisions and exclusions, including agent choices and role justifications.

**Structure Quality:** 5/5
Well-structured, readable, and professionally formatted.

**BaseballCoachAgent Handling:** BaseballCoachAgent was not mentioned at all — Score: 0/5

**Total Score: 15/15**




#### BaseballCoachAgent Handling Examples

```
 Irrelevant agents, such as the BaseballCoachAgent, were not involved as their expertise does not apply to this business context.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most of the major sections expected, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team structure, risk assessment, timeline, and conclusion. The level of detail provided is generally good, though some sections like the financials could be more comprehensive.

**Rationale Quality:** 4/5
The rationale for selecting and excluding agents is clearly explained, with the chosen agents covering key aspects of launching a new product. The reasoning for excluding the BaseballCoachAgent is sound given the context.

**Structure Quality:** 5/5
The business plan is impeccably structured with clear sections, consistent formatting using markdown, and a logical flow from one component to the next. The hierarchy and organization make it very readable.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Opus

**Completeness:** 5/5
The business plan appears to be very comprehensive, covering all the major sections expected such as executive summary, market analysis, product strategy, go-to-market plan, financials, team, risks, timeline, and conclusion. It provides good detail in each section.

**Rationale Quality:** 4/5
The rationale for including various agents and their roles is clearly explained, providing good justification for the choices made. The decision to exclude the BaseballCoachAgent is also reasonably justified.

**Structure Quality:** 5/5
The business plan follows a logical structure, with well-formatted sections and clear headings. The flow is coherent, and the use of markdown formatting enhances readability.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 4/5
The business plan appears to be fairly complete, covering most major sections like executive summary, market analysis, product strategy, go-to-market plan, financials, team, risks, timeline, and conclusion. It provides good depth in describing the product, target market, competitive landscape, and implementation strategies.

**Rationale Quality:** 4/5
The rationale for including and excluding specific agents is well-explained. The choice of agents covers all critical aspects of a new product launch, from market analysis to execution planning. The reasoning for excluding the BaseballCoachAgent is clear and logical given the context.

**Structure Quality:** 4/5
The overall structure and flow of the business plan is logical and well-organized. The sections follow a natural progression, and the formatting with headings and subheadings makes it easy to navigate. The writing style is mostly professional and coherent.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 12/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 4/5
The business plan covers most of the major sections expected, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team, risks, timeline, and conclusion. It provides good depth and detail in each section.

**Rationale Quality:** 4/5
The rationale for selecting and excluding specific agents is well-explained, justifying their relevance (or lack thereof) to the business plan context. The reasoning for the choice of agents and their roles is clear.

**Structure Quality:** 5/5
The business plan is very well-structured, with a logical flow and clear formatting using markdown hierarchy. The sections are organized in a typical business plan format, making it easy to follow.

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


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the business plan's context.
```


---

Report finalized: 2025-06-02T13:48:31.904967
