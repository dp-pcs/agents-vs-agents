# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-02T14:13:28.444106

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length | Message Count |
|-----------|--------------|-------------|----------------|----------------|
| Autogen | 186.22 | 10 | 2265 | 0 |
| Crewai | 183.39 | 5 | 33515 | 0 |
| Langgraph | 250.97 | 10 | 33831 | 0 |

## Agent Selection Capabilities

| Framework | Filtered Irrelevant Agents | Analysis Method |
| Autogen | ? | ? |
| Crewai | ? | ? |
| Langgraph | ? | ? |

## Quality Assessment

| Framework | Completeness | Rationale Quality | Structure Quality | BaseballCoach Handling |
|-----------|--------------|-------------------|-------------------|------------------------|
| Autogen | 3.50/5 | 4.17/5 | 3.67/5 | 5/5 (Properly excluded) |
| Crewai | 2.67/5 | 3.33/5 | 2.83/5 | 5/5 (Properly excluded) |
| Langgraph | 2.83/5 | 3.17/5 | 3.17/5 | 5/5 (Properly excluded) |

## Framework Rankings

| Rank | Framework | Total Score | Completeness | Rationale | Structure |
|------|-----------|-------------|--------------|-----------|----------|
| 1 | Autogen | 11.33/15 | 3.50/5 | 4.17/5 | 3.67/5 |
| 2 | Langgraph | 9.17/15 | 2.83/5 | 3.17/5 | 3.17/5 |
| 3 | Crewai | 8.83/15 | 2.67/5 | 3.33/5 | 2.83/5 |

## Model Scores by Framework

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Autogen | Claude 3 Opus | 4/5 | 5/5 | 4/5 | 13/15 |
| Autogen | Claude 3 Sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Autogen | Claude 3 Haiku | 4/5 | 5/5 | 5/5 | 14/15 |
| Autogen | Titan Text Express | 5/5 | 5/5 | 5/5 | 15/15 |
| Crewai | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | Claude 3 Opus | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | Claude 3 Sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | Claude 3 Haiku | 4/5 | 5/5 | 5/5 | 14/15 |
| Crewai | Titan Text Express | 0/5 | 0/5 | 0/5 | 0/15 |
| Langgraph | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Langgraph | Claude 3 Opus | 4/5 | 4/5 | 5/5 | 13/15 |
| Langgraph | Claude 3 Sonnet | 4/5 | 5/5 | 5/5 | 14/15 |
| Langgraph | Claude 3 Haiku | 5/5 | 5/5 | 5/5 | 15/15 |
| Langgraph | Titan Text Express | 0/5 | 0/5 | 0/5 | 0/15 |

### Final Average Score by Framework (across all models)

| Framework | Average Score (All Models) |
|-----------|--------------------------|
| Autogen | 11.33/15 |
| Crewai | 8.83/15 |
| Langgraph | 9.17/15 |

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
- Completed in 186.22 seconds with 10 agent turns

#### Crewai

- Failed to filter out the irrelevant BaseballCoachAgent
- The BaseballCoachAgent participated in the conversation despite being irrelevant
- Completed in 183.39 seconds with 5 agent turns

#### Langgraph

- Failed to filter out the irrelevant BaseballCoachAgent
- The BaseballCoachAgent participated in the conversation despite being irrelevant
- Completed in 250.97 seconds with 10 agent turns


---

## Detailed Evaluations

### Autogen

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers all the major expected sections and provides placeholders for agents to fill in the details. It is quite complete, though the actual content for each section is still lacking.

**Rationale Quality:** 5/5
The rationale provided for selecting the relevant agents and excluding irrelevant ones like the BaseballCoachAgent is excellent and well-reasoned. It clearly justifies the choices made and how the different components interconnect to create a cohesive plan.

**Structure Quality:** 4/5
The structure and formatting are good, with clear section headings and logical flow. The use of markdown hierarchy could be improved slightly, but overall it is well-organized and readable.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Opus

**Completeness:** 4/5
The business plan covers all the major sections expected, including rationale, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, and rollout timeline. However, some sections lack content as they are marked 'To be completed'.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the choice of agents involved and their respective roles. It clearly justifies the exclusion of irrelevant agents like BaseballCoachAgent. The interconnections between the various components are also explained logically.

**Structure Quality:** 4/5
The structure is well-organized with clear sections and headings. The flow is logical, starting with rationale and then following the typical business plan structure. While the formatting and hierarchy are good, some sections lack content.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 4/5
The business plan includes all the major sections expected, with a clear rationale provided for the agents involved and their roles. The structure is well-formatted with section placeholders.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the choice of agents included and excluded, justifying their relevance or lack thereof for launching an AI productivity app. The interconnections between sections are clearly articulated.

**Structure Quality:** 4/5
The overall structure is logical and well-organized, with consistent formatting and clear section headings. The markdown hierarchy is properly used. While complete, it could benefit from some additional polish.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 4/5
The plan covers all the major sections expected in a business plan, with placeholders for each component. It demonstrates an understanding of the necessary components.

**Rationale Quality:** 5/5
The rationale section provides an excellent and well-reasoned explanation for the choice of agents involved, directly tying them to the relevant aspects of a business plan. The exclusion of irrelevant agents like BaseballCoachAgent is also clearly justified.

**Structure Quality:** 5/5
The overall structure is logically organized into sections, with a clear hierarchy and flow. The use of markdown formatting enhances readability.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

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

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections expected, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, organizational structure, risk analysis, and implementation timeline. It provides good depth and coherence across these components.

**Rationale Quality:** 5/5
The rationale section excellently explains the reasoning behind including each agent and their respective roles in contributing to the business plan. It clearly justifies the relevance of the agents involved and explicitly addresses why the BaseballCoachAgent was excluded.

**Structure Quality:** 4/5
The business plan is well-structured, with a logical flow and formatting that makes it readable and professionally presented. The use of markdown with section headings aids in navigating the content.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Opus

**Completeness:** 4/5
The provided content covers most of the major sections expected in a business plan, such as executive summary, market analysis, product strategy, marketing plan, financial projections, and team/roles. It provides good depth and coherence across these sections.

**Rationale Quality:** 5/5
The rationale section provides an excellent and well-reasoned explanation for the agents involved in creating the business plan and the decision to exclude the BaseballCoachAgent, which is clearly irrelevant for a productivity app business.

**Structure Quality:** 4/5
The content is well-structured, with a logical flow of sections and clear formatting using markdown headers. The hierarchy and organization make it easy to read and follow.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 4/5
The business plan covers most of the expected sections with good depth, including executive summary, market analysis, product strategy, marketing plan, financial projections, team structure, risk mitigation, rollout timeline, and conclusion. However, there are no dedicated sections for operations or manufacturing/fulfillment.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned justification for the choice of agents involved and the exclusion of irrelevant agents like the BaseballCoachAgent. The explanations are clear and demonstrate thoughtful planning.

**Structure Quality:** 4/5
The business plan is well-structured with clear sections, formatting, and logical flow. The use of markdown formatting aids readability. While not perfect, it maintains a professional and organized presentation.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 4/5
The business plan covers most of the major sections expected, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, launch timeline, and conclusion. It provides good depth and coherence across these sections.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the inclusion and exclusion of various agents in assembling the business plan. It clearly justifies the choices made and the roles of each agent, ensuring a comprehensive and cohesive plan.

**Structure Quality:** 5/5
The business plan is impeccably organized, with a consistent formatting, logical section flow, and clear use of markdown hierarchy. The structure is easy to follow and professionally presented.

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


- **Agents Not Used:**
  - **BaseballCoachAgent**: This agent was not relevant to the business plan as the focus is on launching a technology product, not sports coaching.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most of the key sections required, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team structure, risk assessment, timeline, and conclusion. The level of detail provided is good, demonstrating a comprehensive understanding of the various aspects of launching a new product.

**Rationale Quality:** 5/5
The rationale for selecting and excluding agents is clearly explained. The choice of agents is well-reasoned and aligns with the objectives of launching an AI productivity app. The exclusion of the BaseballCoachAgent is justified, as it is irrelevant to the business plan. The agents work together cohesively to address all critical aspects of the product launch.

**Structure Quality:** 4/5
The structure of the business plan is logical and well-organized. It follows a typical flow, starting with an executive summary and progressing through key sections like market analysis, product strategy, financials, and implementation plans. The use of headings and subheadings enhances readability and makes it easy to navigate the document.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Opus

**Completeness:** 4/5
The business plan covers most major sections with good depth, including an executive summary, market analysis, product strategy, go-to-market plan, financials, team, risks, timeline, and conclusion. The level of detail provided is quite thorough.

**Rationale Quality:** 4/5
A clear rationale is provided for selecting the different agents involved in creating the business plan, explaining their roles and contributions. The reasoning for excluding the BaseballCoachAgent is also explicitly stated.

**Structure Quality:** 5/5
The plan is extremely well-structured, with clear sections and logical flow. The formatting is consistent and professionally presented, with markdown hierarchy enhancing readability.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 4/5
The business plan covers most of the key sections one would expect, including an executive summary, market analysis, product strategy, go-to-market plan, financials, team, risks, timeline, and conclusion. It provides good depth and details in each section.

**Rationale Quality:** 5/5
The rationale for choosing the specific agents and their roles is clearly explained. The reasoning behind excluding the BaseballCoachAgent is also provided, demonstrating thoughtfulness in the agent selection process.

**Structure Quality:** 5/5
The business plan is well-structured, with clear sections and a logical flow. The use of headings and subheadings enhances readability, and the overall formatting is professional and consistent.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 5/5
The business plan covers all the expected sections in exceptional detail, including an executive summary, market analysis, product strategy, go-to-market plan, financials, team, risks, timeline, and conclusion.

**Rationale Quality:** 5/5
The rationale section provides excellent reasoning and justification for including each agent and their roles, as well as explicitly explaining why the BaseballCoachAgent was excluded as irrelevant.

**Structure Quality:** 5/5
The business plan is impeccably organized with clear section headings, consistent formatting using markdown, and a logical flow from one section to the next.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

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

Report finalized: 2025-06-02T14:13:28.448526
