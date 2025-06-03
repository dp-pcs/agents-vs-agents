# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-02T17:31:52.460343

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
| Autogen | 4.00/5 | 5.00/5 | 4.00/5 | 5/5 (Properly excluded) |
| Crewai | 4.00/5 | 5.00/5 | 5.00/5 | 5/5 (Properly excluded) |
| Langgraph | 4.00/5 | 5.00/5 | 5.00/5 | 5/5 (Properly excluded) |

## Framework Rankings

| Rank | Framework | Total Score | Completeness | Rationale | Structure |
|------|-----------|-------------|--------------|-----------|----------|
| 1 | Crewai | 14.00/15 | 4.00/5 | 5.00/5 | 5.00/5 |
| 2 | Langgraph | 14.00/15 | 4.00/5 | 5.00/5 | 5.00/5 |
| 3 | Autogen | 13.00/15 | 4.00/5 | 5.00/5 | 4.00/5 |

## Model Scores by Framework

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | claude-3-sonnet | 4/5 | 5/5 | 5/5 | 14/15 |
| Langgraph | claude-3-sonnet | 4/5 | 5/5 | 5/5 | 14/15 |

### Final Average Score by Framework (across all models)

| Framework | Average Score (All Models) |
|-----------|--------------------------|
| Autogen | 13.00/15 |
| Crewai | 14.00/15 |
| Langgraph | 14.00/15 |

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
The business plan includes all the major sections one would expect, from executive summary to rollout timeline. It shows good depth by involving relevant agents to tackle each section.

**Rationale Quality:** 5/5
The rationale provided is excellent - it clearly explains the reasoning behind including each agent and how their roles are interconnected to create a cohesive plan. The exclusion of irrelevant agents like BaseballCoachAgent is also justified.

**Structure Quality:** 4/5
The structure is well-organized with separate sections for each component. The flow is logical, starting with an executive summary and market analysis before diving into product, marketing, and operational details. The formatting with markdown headers is clean and readable.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### BaseballCoachAgent Handling Examples

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most of the essential sections in good detail, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team structure, risk mitigation, and a launch timeline. However, some sections like the competitive analysis and detailed financial models are not provided.

**Rationale Quality:** 5/5
The rationale for including specific agents and excluding others like the BaseballCoachAgent is clearly and thoughtfully explained, directly tying to the business context of launching an AI productivity app.

**Structure Quality:** 5/5
The plan is very well-structured, with clear sections and formatting using markdown. The content flows logically from the overview to supporting details like market analysis and financial projections.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### BaseballCoachAgent Handling Examples

```


- **Agents Not Used:**
  - **BaseballCoachAgent**: This agent was not relevant to the business plan as the focus is on launching a technology product, not sports coaching.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most of the key sections one would expect, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team overview, risk assessment, and timeline. It provides good depth and detail across these components.

**Rationale Quality:** 5/5
The rationale section provides an excellent and well-reasoned explanation for the choice of agents involved in crafting the business plan. It clearly justifies the relevance and role of each agent, and explicitly states why the BaseballCoachAgent was excluded as irrelevant.

**Structure Quality:** 5/5
The business plan is impeccably organized, with a clear logical flow from one section to the next. The use of headings and formatting enhances readability, and the content is presented in a professional manner.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### BaseballCoachAgent Handling Examples

```


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the business plan and does not contribute to the objectives of launching an AI productivity app.
```


---

Report finalized: 2025-06-02T17:31:52.463228
