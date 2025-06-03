# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-03T11:52:21.974135

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
| Autogen | 4.00/5 | 5.00/5 | 4.00/5 | 5/5 (Properly excluded) |
| Crewai | 4.00/5 | 5.00/5 | 4.00/5 | 5/5 (Properly excluded) |
| Langgraph | 4.00/5 | 5.00/5 | 4.00/5 | 5/5 (Properly excluded) |

## Framework Rankings

| Rank | Framework | Total Score | Completeness | Rationale | Structure |
|------|-----------|-------------|--------------|-----------|----------|
| 1 | Autogen | 13.00/15 | 4.00/5 | 5.00/5 | 4.00/5 |
| 2 | Crewai | 13.00/15 | 4.00/5 | 5.00/5 | 4.00/5 |
| 3 | Langgraph | 13.00/15 | 4.00/5 | 5.00/5 | 4.00/5 |

## Model Scores by Framework

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Langgraph | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |

### Final Average Score by Framework (across all models)

| Framework | Average Score (All Models) |
|-----------|--------------------------|
| Autogen | 13.00/15 |
| Crewai | 13.00/15 |
| Langgraph | 13.00/15 |

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
The business plan covers all major sections required, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risks and mitigation strategies, and a rollout timeline. The content provided has good depth and coherence.

**Rationale Quality:** 5/5
The rationale for the choice of agents is clearly and thoroughly explained, highlighting their relevance to the business plan sections. The exclusion of irrelevant agents like BaseballCoachAgent is also justified.

**Structure Quality:** 4/5
The structure is well-organized, with sections clearly delineated and content flowing logically. The use of markdown formatting aids readability.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by gpt-4o

**ERROR:** OpenAI returned non-JSON: ```json
{
  "completeness": 5,
  "completeness_explanation": "The business plan is fully complete, covering all expected sections with exceptional detail and thoughtfulness. It includes an executive s...

#### BaseballCoachAgent Handling Examples

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers all major sections with good depth, including market analysis, product overview, target market, competitive advantage, financial projections, and conclusion. It provides a comprehensive view of the proposed AI productivity app business.

**Rationale Quality:** 5/5
The rationale section clearly explains the choice of expert agents involved and their respective roles in developing the different components of the business plan. It provides excellent reasoning for including each agent and excluding irrelevant ones like the BaseballCoachAgent.

**Structure Quality:** 4/5
The plan is well-structured with clear sections and formatting. It follows a logical flow starting with the rationale, executive summary, market analysis, and other key components. The markdown formatting is clean and readable.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by gpt-4o

**ERROR:** OpenAI returned non-JSON: ```json
{
  "completeness": 5,
  "completeness_explanation": "The business plan for EffiPro is fully complete, including all expected sections such as Executive Summary, Market Analysis, Product Strat...

#### BaseballCoachAgent Handling Examples

```


Agents not used include any irrelevant ones, such as a BaseballCoachAgent, as their expertise does not align with the business objectives of launching a productivity app.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most of the essential sections, including an executive summary, market analysis, product strategy, go-to-market strategy, financial projections, team structure, risk assessment, and timeline. It provides good depth and coherence across these sections.

**Rationale Quality:** 5/5
The rationale for selecting and excluding agents is clearly explained, providing well-reasoned justifications for the choices made. The role and relevance of each agent in contributing to the overall business plan objectives are articulated convincingly.

**Structure Quality:** 4/5
The business plan is well-structured, readable, and professionally formatted. It follows a logical flow, with clear section divisions and hierarchy. The use of markdown formatting enhances readability.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by gpt-4o

**ERROR:** OpenAI returned non-JSON: ```json
{
  "completeness": 5,
  "completeness_explanation": "The business plan is fully complete, covering all expected sections such as Executive Summary, Market Analysis, Product Strategy, Go-to-Ma...

#### BaseballCoachAgent Handling Examples

```


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the business plan and does not contribute to the objectives of launching an AI productivity app.
```


---

Report finalized: 2025-06-03T11:52:21.978572
