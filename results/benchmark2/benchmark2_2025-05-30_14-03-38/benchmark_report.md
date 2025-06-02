# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-02T09:47:34.160612

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length | Message Count |
|-----------|--------------|-------------|----------------|----------------|
| Autogen | 173.28 | 9 | 6030 | ? |
| Crewai | 232.5 | 56 | 34847 | ? |
| Langgraph | 176.56 | 10 | 31975 | ? |

## Agent Selection Capabilities

| Framework | Filtered Irrelevant Agents | Analysis Method |
| Autogen | ? | ? |
| Crewai | ? | ? |
| Langgraph | ? | ? |

## Quality Assessment

| Framework | Completeness | Rationale Quality | Structure Quality | BaseballCoach Handling |
|-----------|--------------|-------------------|-------------------|------------------------|
| Autogen | 5.00/5 | 5.00/5 | 5.00/5 | 5/5 (Properly excluded) |
| Crewai | 4.00/5 | 5.00/5 | 4.00/5 | 5/5 (Properly excluded) |
| Langgraph | 4.00/5 | 5.00/5 | 5.00/5 | 5/5 (Properly excluded) |

## Framework Rankings

| Rank | Framework | Total Score | Completeness | Rationale | Structure |
|------|-----------|-------------|--------------|-----------|----------|
| 1 | Autogen | 15.00/15 | 5.00/5 | 5.00/5 | 5.00/5 |
| 2 | Langgraph | 14.00/15 | 4.00/5 | 5.00/5 | 5.00/5 |
| 3 | Crewai | 13.00/15 | 4.00/5 | 5.00/5 | 4.00/5 |

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
The business plan covers all the expected sections with exceptional detail, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk mitigation, and rollout timeline.

**Rationale Quality:** 5/5
The rationale section provides a clear and well-reasoned justification for the selection and exclusion of agents, explaining how the chosen agents cover all crucial aspects of a business plan while excluding irrelevant ones like the BaseballCoachAgent.

**Structure Quality:** 5/5
The plan is impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy. Each section is clearly labeled and well-structured, making it easy to navigate and read.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### BaseballCoachAgent Handling Examples

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections required, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, timeline, and conclusion. It provides good depth and coherence across these sections.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the agent choices and their roles in creating a comprehensive business plan. It justifies the exclusion of irrelevant agents like the BaseballCoachAgent, clearly explaining how the chosen agents align with the business context.

**Structure Quality:** 4/5
The business plan is well-structured, with a logical flow and consistent formatting using Markdown headings and sections. The hierarchy and organization make it easy to read and navigate.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### BaseballCoachAgent Handling Examples

```
 Irrelevant agents, such as the BaseballCoachAgent, were not involved as their expertise does not apply to this business context.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections expected, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team overview, risk assessment, timeline, and conclusion. It provides good depth and detail across these components.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the inclusion of each agent and how they contribute to creating a comprehensive and cohesive business plan. The exclusion of the BaseballCoachAgent is also clearly justified as irrelevant to the context.

**Structure Quality:** 5/5
The business plan is impeccably organized, with a clear structure and hierarchy. The formatting is consistent, with appropriate use of headings and subheadings, making it easy to navigate and follow the logical flow of information.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### BaseballCoachAgent Handling Examples

```


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the business plan's context.
```


---

Report finalized: 2025-06-02T09:47:34.164216
