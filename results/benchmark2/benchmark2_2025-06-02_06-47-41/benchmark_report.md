# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-02T14:02:23.184282

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
| Crewai | 2.67/5 | 3.33/5 | 2.67/5 | 5/5 (Properly excluded) |
| Langgraph | 2.67/5 | 3.33/5 | 3.00/5 | 5/5 (Properly excluded) |

## Framework Rankings

| Rank | Framework | Total Score | Completeness | Rationale | Structure |
|------|-----------|-------------|--------------|-----------|----------|
| 1 | Autogen | 15.00/15 | 5.00/5 | 5.00/5 | 5.00/5 |
| 2 | Langgraph | 9.00/15 | 2.67/5 | 3.33/5 | 3.00/5 |
| 3 | Crewai | 8.67/15 | 2.67/5 | 3.33/5 | 2.67/5 |

## Model Scores by Framework

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Autogen | Claude 3 Opus | 5/5 | 5/5 | 5/5 | 15/15 |
| Autogen | Claude 3 Sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Autogen | Claude 3 Haiku | 5/5 | 5/5 | 5/5 | 15/15 |
| Autogen | Titan Text Express | 5/5 | 5/5 | 5/5 | 15/15 |
| Crewai | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | Claude 3 Opus | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | Claude 3 Sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | Claude 3 Haiku | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | Titan Text Express | 0/5 | 0/5 | 0/5 | 0/15 |
| Langgraph | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Langgraph | Claude 3 Opus | 4/5 | 5/5 | 4/5 | 13/15 |
| Langgraph | Claude 3 Sonnet | 4/5 | 5/5 | 5/5 | 14/15 |
| Langgraph | Claude 3 Haiku | 4/5 | 5/5 | 5/5 | 14/15 |
| Langgraph | Titan Text Express | 0/5 | 0/5 | 0/5 | 0/15 |

### Final Average Score by Framework (across all models)

| Framework | Average Score (All Models) |
|-----------|--------------------------|
| Autogen | 15.00/15 |
| Crewai | 8.67/15 |
| Langgraph | 9.00/15 |

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
The business plan covers all the essential sections in great detail, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, and a 12-week rollout timeline.

**Rationale Quality:** 5/5
The rationale for involving different agents and their roles is clearly explained, providing a well-reasoned justification for the decisions made in constructing the business plan. The exclusion of irrelevant agents like BaseballCoachAgent is also explicitly mentioned.

**Structure Quality:** 5/5
The business plan is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy, making it easy to read and follow.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Opus

**Completeness:** 5/5
The business plan covers all the expected sections in detail, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, and a 12-week rollout timeline.

**Rationale Quality:** 5/5
The rationale for including each agent and their respective roles is clearly articulated, with a well-reasoned justification for the exclusion of irrelevant agents like the BaseballCoachAgent.

**Structure Quality:** 5/5
The business plan is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy, making it easy to follow and understand.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 5/5
The business plan covers all the essential sections, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, and a 12-week rollout timeline. It provides comprehensive details and demonstrates thoughtfulness in addressing the various aspects required for a successful product launch.

**Rationale Quality:** 5/5
The rationale section clearly explains the selection of agents involved in drafting the business plan, highlighting their specific roles and relevance to the task at hand. It provides a well-reasoned justification for including certain agents while excluding others, such as the BaseballCoachAgent, due to their lack of alignment with the product launch requirements.

**Structure Quality:** 5/5
The business plan follows a logical structure, with sections organized in a coherent and readable manner. The use of headings and subheadings enhances the overall organization, making it easy to navigate through the different components. The formatting is consistent and professionally presented, adhering to best practices for business plan documentation.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 5/5
The business plan covers all major sections in great detail, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team structure, risk assessment, and a rollout timeline.

**Rationale Quality:** 5/5
The rationale provided for including each agent and excluding the BaseballCoachAgent is clear and well-reasoned, explaining how each component contributes to the overall business plan for launching an AI productivity app.

**Structure Quality:** 5/5
The business plan is impeccably structured with clear sections, consistent formatting using markdown, and a logical flow from one component to the next.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

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

**Completeness:** 5/5
No explanation provided.

**Rationale Quality:** 5/5
No explanation provided.

**Structure Quality:** 5/5
No explanation provided.

**BaseballCoachAgent Handling:** BaseballCoachAgent was not mentioned at all — Score: 0/5

**Total Score: 15/15**



#### BaseballCoachAgent Handling Examples

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The provided content covers most major sections expected in a business plan, including market analysis, product overview, competitive advantage, business model, and financial projections. Some areas like detailed marketing and operations plans are missing, but overall it provides good depth.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the choice of agents involved and their roles. It clearly justifies the exclusion of irrelevant agents like the BaseballCoachAgent, aligning the plan components with the business objectives.

**Structure Quality:** 4/5
The content is well-structured with clear sections and a logical flow. The formatting with headings and markdown hierarchy aids readability, giving it a professional appearance overall.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Opus

**Completeness:** 4/5
The content covers most major sections expected in a business plan, including executive summary, market analysis, product overview, competitive advantage, business model, and financial projections. While some details may be missing, the key components are present.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the choice of agents involved and their roles. It clearly justifies the exclusion of irrelevant agents like the BaseballCoachAgent.

**Structure Quality:** 4/5
The content is well-structured, with clear sections and headings. The formatting is consistent and professional, making it easy to read and follow the logical flow of information.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 4/5
The business plan covers most major sections with good depth, including executive summary, market analysis, product overview, competitive advantage, business model, and financial projections. However, some details like specific go-to-market strategies or organizational structure are missing.

**Rationale Quality:** 5/5
The rationale for including various agents and their roles is clearly explained, with a well-reasoned justification for excluding irrelevant agents like the BaseballCoachAgent. The overall approach of covering all critical aspects through a comprehensive set of agents is well-justified.

**Structure Quality:** 4/5
The content is well-structured, with clear sections and subheadings. The formatting is professional, and the flow is logical, making it easy to read and follow.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 4/5
The business plan appears to cover most of the major sections like market analysis, product strategy, go-to-market plan, financials, team, risks, and timeline. However, some key details are missing like specific numbers/data for market sizing, financial projections, competitive analysis, etc.

**Rationale Quality:** 5/5
The rationale for agent selection and roles is thoroughly explained, clearly justifying the choices made and how they fit together cohesively to address all aspects of launching the app.

**Structure Quality:** 4/5
The structure flows logically with clear sections and formatting. The hierarchy with headers makes it easy to follow.

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


I chose not to involve agents irrelevant to the task, such as the BaseballCoachAgent, as their expertise does not align with the business and technology focus required for this plan.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most of the expected sections with good depth, including an executive summary, market analysis, product strategy, go-to-market approach, financial projections, team structure, risk assessment, and a timeline. However, some additional details could be provided in certain sections.

**Rationale Quality:** 5/5
The rationale for the choice of agents is well-explained, highlighting their specific roles and how they contribute to a comprehensive and cohesive business plan. The exclusion of the BaseballCoachAgent is also justified as being irrelevant to the context.

**Structure Quality:** 4/5
The structure is logical and well-formatted, with clear section headings and a professional presentation. The flow between sections is coherent, making it easy to follow the overall plan.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Opus

**Completeness:** 4/5
The business plan covers most of the expected sections, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team structure, risk assessment, and timeline. It provides good depth and coherence across these components.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the selection and roles of the various agents involved in developing the business plan. It clearly justifies the exclusion of the BaseballCoachAgent as irrelevant to the context of an AI productivity app.

**Structure Quality:** 4/5
The business plan is well-structured, with a logical flow between sections and clear formatting using markdown. The rationale section at the beginning helps set the context, followed by the main business plan sections presented in a readable and professionally formatted manner.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 4/5
The business plan covers most major sections expected, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team composition, risk analysis, and implementation timeline. It demonstrates good depth and coherence across these components.

**Rationale Quality:** 5/5
The plan provides excellent rationale for the choice and roles of the various agents used to develop the comprehensive strategy. The reasoning behind including or excluding specific agents like the BaseballCoachAgent is clearly explained.

**Structure Quality:** 5/5
The structure and formatting of the plan is impeccable, with a clear logical flow between sections and consistent use of markdown hierarchy. The content is well-organized and easy to follow.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 4/5
The business plan covers most major sections expected, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team structure, risk assessment, timeline, and conclusion. It provides good depth and coherence across these components.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the choice of agents involved and their roles in developing a comprehensive business plan. It clearly justifies the exclusion of the BaseballCoachAgent as irrelevant to the context.

**Structure Quality:** 5/5
The plan is impeccably organized, with a logical flow of sections and consistent formatting using markdown. The use of headings and subheadings creates a clear hierarchy, making it easy to navigate.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### Evaluation by Titan Text Express

**Completeness:** ?/5
The business plan is complete, covering all essential sections with good depth and coherence.

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

Report finalized: 2025-06-02T14:02:23.186566
