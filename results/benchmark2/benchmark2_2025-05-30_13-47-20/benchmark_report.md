# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-02T13:45:28.862974

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
| Autogen | 2.67/5 | 3.17/5 | 2.67/5 | 5/5 (Properly excluded) |
| Crewai | 2.67/5 | 3.33/5 | 2.67/5 | 5/5 (Properly excluded) |
| Langgraph | 2.83/5 | 3.33/5 | 3.17/5 | 5/5 (Properly excluded) |

## Framework Rankings

| Rank | Framework | Total Score | Completeness | Rationale | Structure |
|------|-----------|-------------|--------------|-----------|----------|
| 1 | Langgraph | 9.33/15 | 2.83/5 | 3.33/5 | 3.17/5 |
| 2 | Crewai | 8.67/15 | 2.67/5 | 3.33/5 | 2.67/5 |
| 3 | Autogen | 8.50/15 | 2.67/5 | 3.17/5 | 2.67/5 |

## Model Scores by Framework

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Autogen | Claude 3 Opus | 4/5 | 4/5 | 4/5 | 12/15 |
| Autogen | Claude 3 Sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Autogen | Claude 3 Haiku | 4/5 | 5/5 | 4/5 | 13/15 |
| Autogen | Titan Text Express | 0/5 | 0/5 | 0/5 | 0/15 |
| Crewai | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | Claude 3 Opus | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | Claude 3 Sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | Claude 3 Haiku | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | Titan Text Express | 0/5 | 0/5 | 0/5 | 0/15 |
| Langgraph | claude-3-sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Langgraph | Claude 3 Opus | 4/5 | 5/5 | 4/5 | 13/15 |
| Langgraph | Claude 3 Sonnet | 4/5 | 5/5 | 5/5 | 14/15 |
| Langgraph | Claude 3 Haiku | 4/5 | 5/5 | 5/5 | 14/15 |
| Langgraph | Titan Text Express | 0/5 | 0/5 | 0/5 | 0/15 |

### Final Average Score by Framework (across all models)

| Framework | Average Score (All Models) |
|-----------|--------------------------|
| Autogen | 8.50/15 |
| Crewai | 8.67/15 |
| Langgraph | 9.33/15 |

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
Most major sections of a business plan are present with good depth, including executive summary, market analysis, product strategy, marketing/sales plan, financial projections, team roles, risks and mitigation strategies. However, it lacks some minor sections like competitive analysis.

**Rationale Quality:** 5/5
Excellent rationale is provided for the selection of agents/roles and how they align with developing a comprehensive business plan for an AI productivity app. The relevance and purpose of each agent is clearly justified.

**Structure Quality:** 4/5
The overall structure is well-organized into logical sections with clear formatting and hierarchy using markdown. The flow between sections is coherent.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Opus

**Completeness:** 4/5
The business plan covers most major sections expected, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, timeline, and conclusion. While not extremely detailed, it provides a good overview of the key elements.

**Rationale Quality:** 4/5
The rationale for agent selection is clearly explained, justifying the inclusion of relevant agents and exclusion of irrelevant ones like the BaseballCoachAgent. The reasoning for the agent choices aligns well with the goal of creating a comprehensive business plan for an AI productivity app.

**Structure Quality:** 4/5
The business plan follows a logical structure with section headings and a cohesive flow. The formatting is clean and readable, making good use of markdown for hierarchy and organization.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 12/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 4/5
The business plan covers most major sections expected, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risks and mitigation, rollout timeline, and conclusion. The content provided shows good depth and coherence across these areas.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned justification for the choice of agents involved in creating the business plan. It clearly explains the relevance and roles of each agent selected, as well as the rationale for excluding irrelevant agents like the BaseballCoachAgent.

**Structure Quality:** 4/5
The business plan is well-structured, with a logical flow and consistent formatting using clear section headings. The hierarchy of sections and subsections makes it easy to navigate and read.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 4/5
The business plan covers most major sections with good depth, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team/roles, risks & mitigation, launch timeline, and conclusion. However, it may be lacking some additional details on company overview, operations plan, etc.

**Rationale Quality:** 5/5
The rationale for agent choices and their roles is excellently explained, providing clear justification for inclusion/exclusion of specific agents based on their relevance to an AI productivity app. The reasoning is well-articulated.

**Structure Quality:** 4/5
The structure is logical and well-organized, with consistent formatting and a clear hierarchy of sections. However, there could be some additional polish in terms of transitions between sections.

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
The business plan covers most major sections expected, including market analysis, product overview, target market, competitive advantage, financial projections, and a conclusion. It provides good depth and detail across these components.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the choice of agents involved and their roles in developing a comprehensive business plan. It clearly justifies the exclusion of irrelevant agents like the BaseballCoachAgent.

**Structure Quality:** 4/5
The business plan is well-structured, with a logical flow of sections and consistent formatting using markdown. The hierarchy of headings and subheadings is clear and readable.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Opus

**Completeness:** 4/5
The business plan covers most of the essential sections expected, including the executive summary, market analysis, product overview, target market, competitive advantage, financial projections, and conclusion. It provides good depth and coherence across these components.

**Rationale Quality:** 5/5
The rationale section excellently explains the reasoning behind including specific expert agents and excluding irrelevant ones like the BaseballCoachAgent. It clearly justifies the choices made and how the different components fit together to form a comprehensive business strategy.

**Structure Quality:** 4/5
The business plan is well-structured, with a logical flow and clear formatting using markdown headings and sections. It is highly readable and maintains a professional tone throughout.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 4/5
The business plan covers most of the expected sections, including market analysis, product overview, target market, competitive advantage, financial projections, and a conclusion. It provides good depth and coherence across these components.

**Rationale Quality:** 5/5
The rationale for using specific agents and their roles is clearly explained, providing excellent justification for the agent choices and how they collectively contribute to a comprehensive business plan. The exclusion of irrelevant agents like the BaseballCoachAgent is also explicitly mentioned and justified.

**Structure Quality:** 4/5
The business plan is well-structured, with a logical flow and clear section hierarchy. The formatting is professional and consistent, making it easy to read and follow.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 4/5
The business plan covers most essential sections like market analysis, product overview, target market, competitive advantage, financial projections, and a conclusion. It provides good depth and coherence across these components.

**Rationale Quality:** 5/5
The rationale section clearly explains the reasoning behind engaging different expert agents for each key aspect of the business plan. It provides a well-reasoned justification for the inclusion and exclusion of agents based on their relevance to launching a productivity app.

**Structure Quality:** 4/5
The business plan is well-structured, with clear sections and a logical flow. The formatting is professional, with consistent use of headings and subheadings, making it easy to read and navigate.

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


Agents not used include any irrelevant ones, such as a BaseballCoachAgent, as their expertise does not align with the business objectives of launching a productivity app.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 5/5
The business plan appears to be fully complete, covering all the expected sections such as executive summary, market analysis, product strategy, go-to-market plan, financial projections, team structure, risk assessment, timeline, and conclusion. The level of detail provided in each section is also exceptional.

**Rationale Quality:** 5/5
The rationale for agent selection is well-explained, clearly outlining the role and purpose of each agent involved in developing the comprehensive business plan. The exclusion of the BaseballCoachAgent is justified as irrelevant to the context of an AI productivity app launch.

**Structure Quality:** 5/5
The structure of the business plan is impeccably organized, with clear section headings, consistent formatting, and a logical flow from one component to the next. The use of markdown formatting enhances readability and hierarchy.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Opus

**Completeness:** 4/5
The business plan covers most major sections like executive summary, market analysis, product strategy, go-to-market strategy, financials, team, risks, and timeline. However, some sections like detailed competitive analysis and implementation plan are missing.

**Rationale Quality:** 5/5
The rationale for including/excluding different agents is clearly explained and well-reasoned, tying each agent's role to a specific aspect of the business plan.

**Structure Quality:** 4/5
The overall structure is logical and well-organized into sections. The formatting is mostly consistent with headings and subheadings. Some parts could use additional polish.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 4/5
The business plan covers most major sections with good depth, including executive summary, market analysis, product strategy, go-to-market plan, financials, team structure, risk assessment, and timeline. However, it lacks some additional context like a company overview.

**Rationale Quality:** 5/5
The rationale for agent choices and exclusions is thoroughly explained, providing clear justifications for each agent's role and how they collectively contribute to a comprehensive business plan.

**Structure Quality:** 5/5
The structure is impeccably organized with consistent formatting, logical flow between sections, and clear hierarchy using markdown.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 4/5
The business plan covers most major sections with good depth, including executive summary, market analysis, product strategy, go-to-market plan, financials, team, risks, and timeline. However, some potentially relevant sections like operations and technical implementation details are missing.

**Rationale Quality:** 5/5
The rationale for including/excluding each agent is clearly explained, with good justification for their roles in developing a comprehensive business plan for an AI productivity app. The BaseballCoachAgent is explicitly mentioned as irrelevant.

**Structure Quality:** 5/5
The plan is very well structured, with clear sections, formatting, and logical flow. Markdown is used effectively to delineate sections and subsections.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

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

Report finalized: 2025-06-02T13:45:28.867684
