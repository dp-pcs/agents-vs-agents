# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-02T14:16:41.080048

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length | Message Count |
|-----------|--------------|-------------|----------------|----------------|
| Autogen | 437.81 | 10 | 32535 | 0 |
| Crewai | 261.0 | 5 | 35616 | 0 |
| Langgraph | 256.83 | 10 | 31696 | 0 |

## Agent Selection Capabilities

| Framework | Filtered Irrelevant Agents | Analysis Method |
| Autogen | ? | ? |
| Crewai | ? | ? |
| Langgraph | ? | ? |

## Quality Assessment

| Framework | Completeness | Rationale Quality | Structure Quality | BaseballCoach Handling |
|-----------|--------------|-------------------|-------------------|------------------------|
| Autogen | 2.67/5 | 3.17/5 | 2.83/5 | 5/5 (Properly excluded) |
| Crewai | 3.40/5 | 4.00/5 | 3.40/5 | 5/5 (Properly excluded) |
| Langgraph | 4.00/5 | 4.75/5 | 4.50/5 | 5/5 (Properly excluded) |

## Framework Rankings

| Rank | Framework | Total Score | Completeness | Rationale | Structure |
|------|-----------|-------------|--------------|-----------|----------|
| 1 | Langgraph | 13.25/15 | 4.00/5 | 4.75/5 | 4.50/5 |
| 2 | Crewai | 10.80/15 | 3.40/5 | 4.00/5 | 3.40/5 |
| 3 | Autogen | 8.67/15 | 2.67/5 | 3.17/5 | 2.83/5 |

## Model Scores by Framework

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Autogen | Claude 3 Opus | 4/5 | 5/5 | 4/5 | 13/15 |
| Autogen | Claude 3 Sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Autogen | Claude 3 Haiku | 4/5 | 4/5 | 5/5 | 13/15 |
| Crewai | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | Claude 3 Opus | 5/5 | 5/5 | 5/5 | 15/15 |
| Crewai | Claude 3 Sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | Claude 3 Haiku | 4/5 | 5/5 | 4/5 | 13/15 |
| Langgraph | claude-3-sonnet | 4/5 | 5/5 | 5/5 | 14/15 |
| Langgraph | Claude 3 Opus | 4/5 | 5/5 | 5/5 | 14/15 |
| Langgraph | Claude 3 Sonnet | 4/5 | 4/5 | 4/5 | 12/15 |
| Langgraph | Claude 3 Haiku | 4/5 | 5/5 | 4/5 | 13/15 |

### Final Average Score by Framework (across all models)

| Framework | Average Score (All Models) |
|-----------|--------------------------|
| Autogen | 8.67/15 |
| Crewai | 10.80/15 |
| Langgraph | 13.25/15 |

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
- Completed in 437.81 seconds with 10 agent turns

#### Crewai

- Failed to filter out the irrelevant BaseballCoachAgent
- The BaseballCoachAgent participated in the conversation despite being irrelevant
- Completed in 261.0 seconds with 5 agent turns

#### Langgraph

- Failed to filter out the irrelevant BaseballCoachAgent
- The BaseballCoachAgent participated in the conversation despite being irrelevant
- Completed in 256.83 seconds with 10 agent turns


---

## Detailed Evaluations

### Autogen

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most of the key sections expected, such as executive summary, market analysis, product strategy, go-to-market plan, financial projections, team structure, risks and mitigation, rollout timeline, and conclusion. It demonstrates good depth and coherence across these areas.

**Rationale Quality:** 5/5
The rationale section provides an excellent and well-reasoned justification for the selection of agents included in the business plan. It clearly explains the relevance of each agent's role and how they collectively contribute to a comprehensive strategy for launching the AI productivity app. The exclusion of the BaseballCoachAgent is also logically explained.

**Structure Quality:** 4/5
The business plan follows a logical structure with distinct sections that flow well. The content is formatted readably with clear headings and hierarchy. Overall, it exhibits a professional structure suitable for a business plan document.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Opus

**Completeness:** 4/5
The business plan covers most of the expected sections with good depth, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, rollout timeline, and conclusion. However, some sections like the financial projections and team/roles appear to be missing based on the truncated content provided.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned justification for including each of the key agent roles in the business plan, while also clearly explaining why the BaseballCoachAgent is excluded as irrelevant for an AI productivity app.

**Structure Quality:** 4/5
The business plan is well-structured, with clear sections and formatting using Markdown headings. The flow from section to section is logical and readable, giving it a professional presentation overall.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 4/5
The plan covers most of the major sections expected for a business plan, including an executive summary, market analysis, product strategy, go-to-market approach, financial projections, team and roles, risks and mitigation, timeline, and conclusion. However, some details on the product features and specifics of the financial model are still lacking.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned justification for the choice of agents involved and excluding the BaseballCoachAgent, which is clearly irrelevant for an AI productivity app. The explanations are clear and insightful.

**Structure Quality:** 4/5
The content follows a logical structure with distinct sections and good use of formatting like headings and bullet points. It flows well from the rationale to the executive summary and market analysis. Overall it is well-organized and readable.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 4/5
The business plan covers most major sections including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, rollout timeline, and conclusion. It provides good depth overall.

**Rationale Quality:** 4/5
Clear rationale is provided for including each of the agents/sections and why the BaseballCoachAgent is excluded as irrelevant. The reasoning for the agent choices is well-explained.

**Structure Quality:** 5/5
The structure is impeccably organized into logical sections with clear headings and formatting. The flow between sections is coherent.

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

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections like executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, timeline, and conclusion. It provides good depth and coherence across these components.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the choice of agents involved and the exclusion of irrelevant agents like the BaseballCoachAgent. The justifications for each agent's role are clear and align with the business objectives.

**Structure Quality:** 4/5
The business plan is well-structured, with a logical flow and consistent formatting using markdown. Sections are organized hierarchically, making it readable and professionally presented.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Opus

**Completeness:** 5/5
The business plan covers all major sections in significant detail, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team structure, risk assessment, timeline, and conclusion. It appears to be a comprehensive plan addressing key aspects needed to launch the ProdAI app.

**Rationale Quality:** 5/5
The rationale section provides a clear and well-reasoned explanation for the choice of agents involved, highlighting their relevance to different components of the business plan. It also justifies the exclusion of irrelevant agents like the BaseballCoachAgent.

**Structure Quality:** 5/5
The business plan follows a logical structure with clear sections and formatting. The use of markdown headers and formatting aids readability and hierarchical organization of content.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 4/5
The document includes most major sections of a business plan, covering topics like executive summary, market analysis, product strategy, go-to-market, financials, team, risks, and timeline. While the content provided is not fully comprehensive, it demonstrates good depth and coherence across the covered sections.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the choice of agents and their roles in developing the business plan. It clearly justifies the inclusion and exclusion of agents based on their relevance to the business objectives.

**Structure Quality:** 4/5
The document is well-structured, with clear sections and subsections using markdown formatting. The flow between sections is logical, making it easy to read and follow. While not impeccable, the overall structure and formatting is professionally presented.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 4/5
The provided content covers most major sections expected in a business plan, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team structure, risk assessment, timeline, and conclusion. While some sections are only briefly outlined, the overall completeness is good.

**Rationale Quality:** 5/5
The rationale for engaging specific expert agents and excluding irrelevant ones like the BaseballCoachAgent is clearly and thoroughly explained. The reasoning behind each agent's role and their collective contribution to a cohesive business plan is well-justified.

**Structure Quality:** 4/5
The document follows a logical structure with distinct sections for each business plan component. The use of headings and formatting enhances readability, though some parts could benefit from additional polish or hierarchy.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### BaseballCoachAgent Handling Examples

```


I chose not to involve irrelevant agents like the BaseballCoachAgent, as their expertise does not align with the business objectives of launching a tech product.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most of the major sections one would expect, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team structure, risk assessment, and timeline. It provides good depth and coherence across these sections.

**Rationale Quality:** 5/5
The rationale for including each agent and their specific roles is clearly explained, justifying their relevance to the business plan development process. The exclusion of the BaseballCoachAgent is also explicitly justified as being irrelevant to the context.

**Structure Quality:** 5/5
The business plan follows a logical structure with consistent formatting and clear section hierarchy using markdown. The flow between sections is smooth, making it easy to read and navigate.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### Evaluation by Claude 3 Opus

**Completeness:** 4/5
The business plan covers most of the key sections one would expect, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team overview, risk assessment, and timeline. It provides good depth and coherence across these sections.

**Rationale Quality:** 5/5
The rationale section provides an excellent explanation for the choice of agents involved and their roles in contributing to a comprehensive business plan. The reasoning for excluding the BaseballCoachAgent is also clearly justified.

**Structure Quality:** 5/5
The business plan is very well structured, with clear section headings, consistent formatting using markdown, and a logical flow from one section to the next. The hierarchy and organization are impeccable.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 4/5
The business plan covers most of the key sections one would expect, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team structure, risk assessment, and timeline. It provides good depth and detail in these areas.

**Rationale Quality:** 4/5
The rationale section clearly explains the reasoning behind involving each key agent and their roles in developing the comprehensive business plan. The exclusion of the BaseballCoachAgent is well-justified as being irrelevant to the business context.

**Structure Quality:** 4/5
The plan follows a logical structure with clear sections and formatting. The flow from one component to the next is well-organized and readable. The hierarchy of sections with headings/subheadings is professional.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 12/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 4/5
The business plan covers most major sections, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team structure, risk assessment, and timeline. It provides good depth and coherence across these sections.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the choice of agents involved in developing the business plan. It clearly justifies the relevance of each agent and their respective roles, while explicitly excluding the BaseballCoachAgent as irrelevant to the context.

**Structure Quality:** 4/5
The business plan is well-structured, with a logical flow and clear section divisions. The use of headings and formatting enhances readability and presents a professional appearance.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### BaseballCoachAgent Handling Examples

```


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the business plan context.
```


---

Report finalized: 2025-06-02T14:16:41.084009
