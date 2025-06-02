# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-02T09:48:46.065236

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length | Message Count |
|-----------|--------------|-------------|----------------|----------------|
| Autogen | 317.15 | 10 | 6655 | ? |
| Crewai | 227.91 | 3 | 35195 | ? |
| Langgraph | 248.49 | 10 | 32818 | ? |

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
| Langgraph | 4.00/5 | 5.00/5 | 4.00/5 | 5/5 (Properly excluded) |

## Framework Rankings

| Rank | Framework | Total Score | Completeness | Rationale | Structure |
|------|-----------|-------------|--------------|-----------|----------|
| 1 | Autogen | 15.00/15 | 5.00/5 | 5.00/5 | 5.00/5 |
| 2 | Crewai | 13.00/15 | 4.00/5 | 5.00/5 | 4.00/5 |
| 3 | Langgraph | 13.00/15 | 4.00/5 | 5.00/5 | 4.00/5 |

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
The business plan covers all major sections in exceptional detail, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, and rollout timeline.

**Rationale Quality:** 5/5
Excellent rationale is provided for the inclusion of each agent and their respective roles in contributing to the various sections of the business plan. The reasoning for excluding the BaseballCoachAgent is also clearly justified.

**Structure Quality:** 5/5
The business plan is impeccably organized with consistent formatting, logical section flow, and clear hierarchy using markdown headings. It is highly readable and professionally presented.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### BaseballCoachAgent Handling Examples

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The plan covers most major sections in good depth, including market analysis, product overview, competitive advantage, business model, and financial projections. However, some sections like the team, risks, and detailed product strategy seem to be missing or lacking detail.

**Rationale Quality:** 5/5
The rationale for selecting and involving various expert agents is clearly explained, highlighting how their expertise aligns with different components of the business plan. The exclusion of irrelevant agents like the BaseballCoachAgent is also justified.

**Structure Quality:** 4/5
The structure and formatting are logical and professional, with clear sections and hierarchical markdown formatting. The flow between sections is smooth and easy to follow.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### BaseballCoachAgent Handling Examples

```


I chose not to involve agents irrelevant to the task, such as the BaseballCoachAgent, as their expertise does not align with the business and technology focus required for this plan.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections expected, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team, risk assessment, and timeline. It demonstrates good depth and coherence.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned justification for the selection and roles of each agent involved in developing the business plan. It clearly explains how the agents fit together to address all critical aspects of launching a new product.

**Structure Quality:** 4/5
The business plan is well-structured, with a logical flow of sections and clear formatting using markdown. The hierarchy of sections is evident, making it readable and professionally presented.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### BaseballCoachAgent Handling Examples

```


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the context of a business plan for an AI productivity app.
```


---

Report finalized: 2025-06-02T09:48:46.069414
