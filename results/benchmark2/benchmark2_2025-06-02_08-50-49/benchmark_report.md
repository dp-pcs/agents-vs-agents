# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-02T14:09:54.915825

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length | Message Count |
|-----------|--------------|-------------|----------------|----------------|
| Autogen | 206.26 | 9 | 6409 | 0 |
| Crewai | 334.63 | 5 | 33888 | 0 |
| Langgraph | 240.43 | 10 | 31996 | 0 |

## Agent Selection Capabilities

| Framework | Filtered Irrelevant Agents | Analysis Method |
| Autogen | ? | ? |
| Crewai | ? | ? |
| Langgraph | ? | ? |

## Quality Assessment

| Framework | Completeness | Rationale Quality | Structure Quality | BaseballCoach Handling |
|-----------|--------------|-------------------|-------------------|------------------------|
| Autogen | 4.67/5 | 4.67/5 | 4.50/5 | 5/5 (Properly excluded) |
| Crewai | 2.67/5 | 3.17/5 | 2.83/5 | 5/5 (Properly excluded) |
| Langgraph | 2.67/5 | 3.33/5 | 2.83/5 | 5/5 (Properly excluded) |

## Framework Rankings

| Rank | Framework | Total Score | Completeness | Rationale | Structure |
|------|-----------|-------------|--------------|-----------|----------|
| 1 | Autogen | 13.83/15 | 4.67/5 | 4.67/5 | 4.50/5 |
| 2 | Langgraph | 8.83/15 | 2.67/5 | 3.33/5 | 2.83/5 |
| 3 | Crewai | 8.67/15 | 2.67/5 | 3.17/5 | 2.83/5 |

## Model Scores by Framework

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 4/5 | 5/5 | 5/5 | 14/15 |
| Autogen | Claude 3 Opus | 5/5 | 5/5 | 4/5 | 14/15 |
| Autogen | Claude 3 Sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Autogen | Claude 3 Haiku | 5/5 | 5/5 | 5/5 | 15/15 |
| Autogen | Titan Text Express | 5/5 | 4/5 | 4/5 | 13/15 |
| Crewai | claude-3-sonnet | 4/5 | 4/5 | 4/5 | 12/15 |
| Crewai | Claude 3 Opus | 4/5 | 5/5 | 5/5 | 14/15 |
| Crewai | Claude 3 Sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | Claude 3 Haiku | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | Titan Text Express | 0/5 | 0/5 | 0/5 | 0/15 |
| Langgraph | claude-3-sonnet | 4/5 | 5/5 | 5/5 | 14/15 |
| Langgraph | Claude 3 Opus | 4/5 | 5/5 | 4/5 | 13/15 |
| Langgraph | Claude 3 Sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Langgraph | Claude 3 Haiku | 4/5 | 5/5 | 4/5 | 13/15 |
| Langgraph | Titan Text Express | 0/5 | 0/5 | 0/5 | 0/15 |

### Final Average Score by Framework (across all models)

| Framework | Average Score (All Models) |
|-----------|--------------------------|
| Autogen | 13.83/15 |
| Crewai | 8.67/15 |
| Langgraph | 8.83/15 |

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
- Completed in 206.26 seconds with 9 agent turns

#### Crewai

- Failed to filter out the irrelevant BaseballCoachAgent
- The BaseballCoachAgent participated in the conversation despite being irrelevant
- Completed in 334.63 seconds with 5 agent turns

#### Langgraph

- Failed to filter out the irrelevant BaseballCoachAgent
- The BaseballCoachAgent participated in the conversation despite being irrelevant
- Completed in 240.43 seconds with 10 agent turns


---

## Detailed Evaluations

### Autogen

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers all major sections expected, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk mitigation, and a 12-week timeline. The level of detail provided is good across most sections.

**Rationale Quality:** 5/5
The rationale for agent selection and their roles is excellently explained, providing clear justification for inclusion and exclusion of specific agents based on their relevance to the business plan components.

**Structure Quality:** 5/5
The business plan follows a logical structure with consistent formatting and a clear hierarchy using markdown sections. The flow between sections is coherent, making it easy to follow.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### Evaluation by Claude 3 Opus

**Completeness:** 5/5
The business plan covers all the essential sections in great detail, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk mitigation, and a 12-week rollout timeline.

**Rationale Quality:** 5/5
The rationale for including or excluding each agent is thoroughly explained, clearly justifying the choices made to cover all necessary components of an operational plan while excluding irrelevant agents like the BaseballCoachAgent.

**Structure Quality:** 4/5
The plan follows a logical structure with clear sections and good formatting. While not impeccable, it is well-organized and readable.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 5/5
The business plan covers all major sections expected, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk mitigation, and a 12-week rollout timeline. The content is comprehensive and well-detailed across each section.

**Rationale Quality:** 5/5
The rationale provided for including specific agents is well-reasoned and justified, clearly explaining the role and purpose of each agent chosen. The exclusion of irrelevant agents like BaseballCoachAgent is also explicitly mentioned and explained.

**Structure Quality:** 5/5
The overall structure is impeccably organized, with consistent formatting and a logical hierarchy of sections. The use of markdown formatting enhances readability, and the flow of information is clear and professionally presented.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 5/5
The business plan covers all essential sections expected, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risks and mitigation, timeline, and conclusion. The depth and detail provided for each section is exceptional.

**Rationale Quality:** 5/5
The rationale for including or excluding specific agents is clearly explained, with sound reasoning provided for the choices made to ensure a comprehensive and coherent plan. The roles and relevance of each agent are well-justified.

**Structure Quality:** 5/5
The business plan follows a logical structure, with clear sections and subsections. The formatting is consistent and professional, with effective use of headings and markdown hierarchy, making it easy to navigate and read.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Titan Text Express

**Completeness:** 5/5
All required sections included with good depth and coherence.

**Rationale Quality:** 4/5
Good explanation of agent use and exclusions, with mostly clear reasoning.

**Structure Quality:** 4/5
Well-structured, readable, and professionally formatted.

**BaseballCoachAgent Handling:** BaseballCoachAgent was not mentioned at all — Score: 0/5

**Total Score: 13/15**

#### Evaluation by Titan Text Lite

**Completeness:** 4/5
The business plan is well-structured, covering all necessary components of an operational plan. It involves the use of agents to cover all necessary components of an operational plan, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risks mitigation, and a 12-week timeline. The plan is comprehensive and well-organized, providing a clear understanding of the business objectives, unique value proposition, and primary goals.

**Rationale Quality:** 4/5
The rationale provided is comprehensive and well-reasoned, covering all major sections of the business plan. The agents used are relevant to the operational setting and contribute to the overall strategy. The plan is well-structured, covering all necessary components of an operational plan, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risks mitigation, and a 12-week timeline. The plan is comprehensive and well-organized, providing a clear understanding of the business objectives, unique value proposition, and primary goals.

**Structure Quality:** 4/5
The structure of the business plan is well-organized, with clear headings and subheadings. The agents used are relevant to the operational setting and contribute to the overall strategy. The plan is well-structured, covering all necessary components of an operational plan, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risks mitigation, and a 12-week timeline. The plan is comprehensive and well-organized, providing a clear understanding of the business objectives, unique value proposition, and primary goals.

**BaseballCoachAgent Handling:** BaseballCoachAgent was not mentioned at all — Score: 0/5

**Total Score: 12/15**



#### BaseballCoachAgent Handling Examples

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most of the key sections expected, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team structure, risk assessment, launch timeline, and conclusion. It provides good depth and detail across these components.

**Rationale Quality:** 4/5
The rationale for agent selection and their roles is well-explained, clearly outlining how each agent contributes to building a comprehensive business plan. The reasoning for excluding irrelevant agents like the BaseballCoachAgent is also provided.

**Structure Quality:** 4/5
The plan follows a logical structure, with sections organized in a coherent manner. The use of markdown formatting enhances readability, and the flow between sections is smooth and professionally presented.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 12/15**

#### Evaluation by Claude 3 Opus

**Completeness:** 4/5
The business plan covers most major sections with good depth, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risk mitigation, rollout timeline, and conclusion. It provides a comprehensive overview of the business.

**Rationale Quality:** 5/5
The rationale section provides an excellent and well-reasoned explanation for the selection of agents and how their components fit together into a cohesive plan. The justification for including or excluding agents is clear.

**Structure Quality:** 5/5
The business plan is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy. It is easy to read and follow.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 4/5
The plan covers most major sections expected in a comprehensive business plan, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team/roles, risks and mitigation, rollout timeline, and conclusion. It provides good depth and coherence across these components.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned justification for the selection and role of each agent in creating the various plan components. It clearly explains how the agents' expertise aligns with the business objectives and how their contributions fit together into a cohesive strategy.

**Structure Quality:** 4/5
The plan follows a logical structure with distinct sections and clear formatting using markdown. The flow from one component to the next is well-organized and readable, giving it a professional presentation.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 4/5
The business plan covers most major sections expected, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team structure, risk mitigation, launch timeline, and conclusion. It provides good depth and coherence across these components.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the selection and role of each agent used in developing the business plan. It clearly justifies why certain agents were included or excluded based on their relevance to launching a tech product.

**Structure Quality:** 4/5
The structure is well-organized, with clear section headings and a logical flow from the executive summary through the various plan components. The formatting is consistent and readable, giving an overall professional presentation.

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


Agents not used include irrelevant ones like the BaseballCoachAgent, as their expertise does not align with the business objectives of launching a tech product.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections one would expect, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team overview, risk assessment, and a rollout timeline. It provides good depth and coherence across these sections.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the inclusion of each agent and how they contribute to the overall business plan. It clearly justifies the exclusion of the BaseballCoachAgent as irrelevant to the objectives of an AI productivity app.

**Structure Quality:** 5/5
The business plan is impeccably organized, with a clear hierarchy of sections and consistent formatting using markdown. The flow between sections is logical, with each component building upon the previous one.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### Evaluation by Claude 3 Opus

**Completeness:** 4/5
The business plan covers most major sections one would expect, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team overview, risk assessment, and implementation timeline. While certain details may be lacking, the overall plan provides good depth and coherence.

**Rationale Quality:** 5/5
The plan provides an excellent, well-reasoned rationale for the selection and roles of the various agents involved in developing the business plan. The exclusion of the BaseballCoachAgent is explicitly justified as being irrelevant to an AI productivity app. The roles of the agents are clearly outlined and aligned with the objectives of launching the new product.

**Structure Quality:** 4/5
The business plan follows a logical structure, with sections organized in a sensible flow. The formatting is consistent and professional, with clear use of headings and subheadings. The plan is easy to read and navigate.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 4/5
The business plan covers most major sections such as executive summary, market analysis, product strategy, go-to-market plan, financials, team, risks, and timeline. It provides good depth across these areas.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned justification for including each agent and their roles. It clearly explains how the agents work together to create a cohesive business plan for launching the AI productivity app.

**Structure Quality:** 4/5
The structure is logical and well-formatted, with clear sections and headings. The flow from executive summary to conclusion is coherent.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 4/5
The business plan covers most of the essential sections such as executive summary, market analysis, product strategy, go-to-market plan, financials, team, risks, timeline, and conclusion. While the content is somewhat truncated, it appears to provide good depth and coherence across these major sections.

**Rationale Quality:** 5/5
The rationale for including each agent and their roles is clearly and thoroughly explained. The reasoning for excluding the BaseballCoachAgent is also explicitly provided, citing its irrelevance to the AI productivity app business plan.

**Structure Quality:** 4/5
The structure of the business plan is well-organized and follows a logical flow, with clear section headings and formatting. The hierarchy of sections is easy to follow.

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


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the business plan and does not contribute to the objectives of launching an AI productivity app.
```


---

Report finalized: 2025-06-02T14:09:54.920889
