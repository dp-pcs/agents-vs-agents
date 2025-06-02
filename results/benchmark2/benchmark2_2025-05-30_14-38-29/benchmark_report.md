# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-02T13:53:14.475814

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
| Autogen | 2.67/5 | 3.17/5 | 2.83/5 | 5/5 (Properly excluded) |
| Crewai | 2.67/5 | 3.33/5 | 2.67/5 | 5/5 (Properly excluded) |
| Langgraph | 2.67/5 | 3.17/5 | 3.00/5 | 5/5 (Properly excluded) |

## Framework Rankings

| Rank | Framework | Total Score | Completeness | Rationale | Structure |
|------|-----------|-------------|--------------|-----------|----------|
| 1 | Langgraph | 8.83/15 | 2.67/5 | 3.17/5 | 3.00/5 |
| 2 | Autogen | 8.67/15 | 2.67/5 | 3.17/5 | 2.83/5 |
| 3 | Crewai | 8.67/15 | 2.67/5 | 3.33/5 | 2.67/5 |

## Model Scores by Framework

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 4/5 | 4/5 | 4/5 | 12/15 |
| Autogen | Claude 3 Opus | 4/5 | 5/5 | 4/5 | 13/15 |
| Autogen | Claude 3 Sonnet | 4/5 | 5/5 | 5/5 | 14/15 |
| Autogen | Claude 3 Haiku | 4/5 | 5/5 | 4/5 | 13/15 |
| Autogen | Titan Text Express | 0/5 | 0/5 | 0/5 | 0/15 |
| Crewai | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | Claude 3 Opus | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | Claude 3 Sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | Claude 3 Haiku | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | Titan Text Express | 0/5 | 0/5 | 0/5 | 0/15 |
| Langgraph | claude-3-sonnet | 4/5 | 4/5 | 4/5 | 12/15 |
| Langgraph | Claude 3 Opus | 4/5 | 5/5 | 5/5 | 14/15 |
| Langgraph | Claude 3 Sonnet | 4/5 | 5/5 | 5/5 | 14/15 |
| Langgraph | Claude 3 Haiku | 4/5 | 5/5 | 4/5 | 13/15 |
| Langgraph | Titan Text Express | 0/5 | 0/5 | 0/5 | 0/15 |

### Final Average Score by Framework (across all models)

| Framework | Average Score (All Models) |
|-----------|--------------------------|
| Autogen | 8.67/15 |
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
The business plan covers most of the major sections one would expect like executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risks and mitigation, and timeline. It provides good depth in these areas.

**Rationale Quality:** 4/5
The rationale for selecting each agent is clearly explained, highlighting how they will contribute to different components of the business plan. The exclusion of the BaseballCoachAgent is also justified as irrelevant.

**Structure Quality:** 4/5
The plan follows a logical structure with clear section headings. The formatting is good with markdown hierarchy and readability.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 12/15**

#### Evaluation by Claude 3 Opus

**Completeness:** 4/5
The business plan covers most of the key sections like executive summary, market analysis, product strategy, go-to-market plan, financials, team, risks, and timeline. It provides good depth in each area.

**Rationale Quality:** 5/5
The rationale for including each agent is clearly explained and well-justified based on the requirements of a comprehensive business plan for an AI productivity app. The exclusion of the BaseballCoachAgent is also explicitly mentioned and reasoned.

**Structure Quality:** 4/5
The structure flows logically from the rationale to the different sections of the business plan. The formatting with headings and sub-sections makes it easy to read and follow.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 4/5
The business plan covers most major sections like executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risks and mitigation, and timeline. It provides good depth in each section.

**Rationale Quality:** 5/5
The rationale for agent selection is clearly explained, providing justification for including each agent and how they contribute to creating a comprehensive business plan. The reasoning for excluding the BaseballCoachAgent is also explicitly stated.

**Structure Quality:** 5/5
The business plan follows a logical structure with clear sections and formatting. The use of markdown headings makes it easy to navigate. The flow from one section to the next is smooth and coherent.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 4/5
The business plan covers most of the key sections including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risks and mitigation, and rollout timeline. It provides good depth and coherence across these areas.

**Rationale Quality:** 5/5
The rationale section provides an excellent and well-reasoned justification for the selection of each agent, clearly explaining their roles and how they contribute to a comprehensive business plan. The exclusion of the BaseballCoachAgent is also explicitly mentioned and explained.

**Structure Quality:** 4/5
The structure is well-organized with logical sections and consistent formatting using markdown. The flow between sections is coherent, making it readable and professionally presented.

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
The plan covers most essential sections like market analysis, product strategy, go-to-market plan, financial projections, team structure, risk assessment, and launch timeline. It provides good depth and details across these components.

**Rationale Quality:** 5/5
The rationale for agent selection and their roles is excellently explained, clearly justifying the choices made to comprehensively address all aspects of launching a new product. The exclusion of irrelevant agents like BaseballCoachAgent is also logically reasoned.

**Structure Quality:** 4/5
The structure is well-organized with clear sections, headings, and logical flow. The formatting is professional and readable, though some minor inconsistencies in markdown styling could be improved.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Opus

**Completeness:** 4/5
The business plan covers most major sections like market analysis, product strategy, go-to-market plan, financial projections, team, risks, timeline, and conclusion. It seems reasonably complete.

**Rationale Quality:** 5/5
The rationale section provides a clear and well-reasoned explanation for the inclusion of various agents based on their expertise mapping to different components of the business plan. The relevance and role of each agent is justified.

**Structure Quality:** 4/5
The structure flows logically from the rationale to the different sections of the business plan. Formatting with headings and markdown makes it easy to read and navigate.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 4/5
The business plan covers most of the key sections expected, including market analysis, product strategy, go-to-market plan, financial projections, team structure, risk mitigation, and rollout timeline. However, some additional details could be provided in certain areas for a more comprehensive plan.

**Rationale Quality:** 5/5
The rationale section provides an excellent and well-reasoned justification for the selection of expert agents used in the plan, explaining their relevance and how their contributions fit together to address various aspects of launching a new product. The exclusion of irrelevant agents like the BaseballCoachAgent is also clearly explained.

**Structure Quality:** 4/5
The overall structure of the business plan is well-organized, with sections flowing logically from the executive summary to the conclusion. The use of headings and formatting helps with readability, giving it a professional appearance. However, some minor formatting inconsistencies could be addressed for a more polished presentation.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 4/5
The business plan covers most major sections with good depth, including market analysis, product strategy, go-to-market plan, financial projections, team structure, risk assessment, and a rollout timeline. However, some additional details or sections could further enhance its completeness.

**Rationale Quality:** 5/5
The rationale section provides an excellent and well-reasoned explanation for the selection of relevant agents and their roles in creating a comprehensive business plan. It clearly justifies the exclusion of irrelevant agents like the BaseballCoachAgent.

**Structure Quality:** 4/5
The business plan follows a logical structure with distinct sections and formatting. The use of headings and subheadings makes it easy to navigate, though some minor formatting inconsistencies exist. Overall, it presents a professionally structured and readable document.

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


Agents not used include irrelevant ones like the BaseballCoachAgent, as their expertise does not align with the business context of launching a tech product.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most of the major sections expected, including an executive summary, market analysis, product strategy, go-to-market strategy, financial projections, team details, risk assessment, and timeline. However, some sections like the competitive analysis and detailed marketing plan are missing.

**Rationale Quality:** 4/5
The rationale for the choice of agents and their roles is well-explained, providing a clear understanding of how each component contributes to the overall business plan. The decision to exclude the BaseballCoachAgent is also justified as being irrelevant to the context.

**Structure Quality:** 4/5
The structure of the business plan is well-organized and follows a logical flow, starting with an executive summary and progressing through the various sections. The use of headings and subheadings makes it easy to navigate the document.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 12/15**

#### Evaluation by Claude 3 Opus

**Completeness:** 4/5
The business plan covers most of the major sections expected, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team overview, risk assessment, and timeline. It provides good depth and detail across these components.

**Rationale Quality:** 5/5
The rationale section provides an excellent and well-reasoned justification for the choice of agents involved in developing the business plan. It clearly explains the role and relevance of each agent, as well as the decision to exclude the BaseballCoachAgent as irrelevant to the context. The rationale is coherent and thoughtful.

**Structure Quality:** 5/5
The business plan follows a logical structure, with clear sections and formatting. The use of headings and subheadings facilitates readability, and the overall organization is impeccable, allowing for a smooth flow between the different components.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 4/5
The business plan covers all the major sections expected, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team structure, risk assessment, timeline, and conclusion. The content provided has good depth and coherence across these sections.

**Rationale Quality:** 5/5
The rationale for including each agent and their respective roles is clearly explained, providing a well-reasoned justification for the decisions made. The exclusion of the BaseballCoachAgent is also explicitly addressed and logically justified.

**Structure Quality:** 5/5
The business plan is impeccably organized, with a consistent formatting style, logical section flow, and clear use of markdown hierarchy. The structure makes it easy to navigate and follow the content.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 4/5
The business plan covers most of the major sections expected, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team composition, risk assessment, and timeline. It provides good depth and coherence across these sections.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the choice of agents involved and their respective roles. It clearly justifies the exclusion of the BaseballCoachAgent as irrelevant to the business plan context.

**Structure Quality:** 4/5
The business plan is well-structured, with a logical flow between sections and consistent formatting using markdown. The hierarchy of sections is clear, making it readable and professionally presented.

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

Report finalized: 2025-06-02T13:53:14.479641
