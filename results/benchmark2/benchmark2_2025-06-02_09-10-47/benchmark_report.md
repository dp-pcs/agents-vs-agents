# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-02T09:49:55.305687

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length | Message Count |
|-----------|--------------|-------------|----------------|----------------|
| Autogen | 186.22 | 10 | 2265 | ? |
| Crewai | 183.39 | 5 | 33515 | ? |
| Langgraph | 250.97 | 10 | 33831 | ? |

## Agent Selection Capabilities

| Framework | Filtered Irrelevant Agents | Analysis Method |
| Autogen | ? | ? |
| Crewai | ? | ? |
| Langgraph | ? | ? |

## Quality Assessment

| Framework | Completeness | Rationale Quality | Structure Quality | BaseballCoach Handling |
|-----------|--------------|-------------------|-------------------|------------------------|
| Autogen | 4.00/5 | 5.00/5 | 5.00/5 | 5/5 (Properly excluded) |
| Crewai | 4.00/5 | 5.00/5 | 4.00/5 | 5/5 (Properly excluded) |
| Langgraph | 4.00/5 | 4.00/5 | 5.00/5 | 5/5 (Properly excluded) |

## Framework Rankings

| Rank | Framework | Total Score | Completeness | Rationale | Structure |
|------|-----------|-------------|--------------|-----------|----------|
| 1 | Autogen | 14.00/15 | 4.00/5 | 5.00/5 | 5.00/5 |
| 2 | Crewai | 13.00/15 | 4.00/5 | 5.00/5 | 4.00/5 |
| 3 | Langgraph | 13.00/15 | 4.00/5 | 4.00/5 | 5.00/5 |

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
The business plan covers all the major sections one would expect, including rationale for agent selection. The only potential gap is the lack of a conclusion section, though that could be compiled from the other sections.

**Rationale Quality:** 5/5
The rationale for agent selection is excellent - it clearly justifies the inclusion and exclusion of agents based on their relevance to a business plan for an AI productivity app. The connections between the components are also well-explained.

**Structure Quality:** 5/5
The structure is impeccably organized into logical sections with a clear hierarchy using markdown formatting. Each section has a descriptive heading indicating which agent will complete that part of the plan.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### BaseballCoachAgent Handling Examples

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections with good depth, including an executive summary, market analysis, product strategy, marketing plan, financial projections, team and roles, risks and mitigation, implementation timeline, and conclusion. However, it does not provide detailed information on the specific product features or technical implementation.

**Rationale Quality:** 5/5
The rationale for including or excluding each agent is clearly explained, providing justifications for their relevance or irrelevance to the business plan. The reasoning behind the choice of agents is well-articulated and aligns with the goals of the business plan.

**Structure Quality:** 4/5
The business plan is well-structured and formatted, with clear sections and a logical flow. The use of headings and subheadings enhances readability and organization. However, there could be some improvements in terms of consistent formatting and hierarchy across all sections.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### BaseballCoachAgent Handling Examples

```


- **Agents Not Used:**
  - **BaseballCoachAgent**: This agent was not relevant to the business plan as the focus is on launching a technology product, not sports coaching.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections expected, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team overview, risk assessment, and timeline. It provides good depth and coherence across these sections.

**Rationale Quality:** 4/5
A clear rationale is provided for the selection and roles of the different agents used to develop the business plan. The explanation covers how each agent contributes to a specific aspect of the plan, ensuring comprehensive coverage. The exclusion of the BaseballCoachAgent is also justified.

**Structure Quality:** 5/5
The business plan is impeccably organized, with a logical flow across sections. It uses consistent markdown formatting and a clear hierarchy, making it easy to read and navigate. The structure is professional and polished.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### BaseballCoachAgent Handling Examples

```


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the business plan and does not contribute to the objectives of launching an AI productivity app.
```


---

Report finalized: 2025-06-02T09:49:55.307022
