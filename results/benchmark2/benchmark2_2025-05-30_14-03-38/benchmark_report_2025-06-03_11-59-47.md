# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-03T12:00:25.516251

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length |
|-----------|--------------|-------------|----------------|
| Autogen | 173.28 | 9 | 6030 |
| Crewai | 232.5 | 56 | 34847 |
| Langgraph | 176.56 | 10 | 31975 |

## Quality Assessment (Claude & OpenAI Average)

| Framework | Completeness | Rationale Quality | Structure Quality | BaseballCoach Handling (Claude) |
|-----------|--------------|-------------------|-------------------|---------------------------------|
| Autogen | ERROR | ERROR | ERROR | ERROR |
| Crewai | ERROR | ERROR | ERROR | ERROR |
| Langgraph | ERROR | ERROR | ERROR | ERROR |

## Individual Model Scores by Framework (Claude & OpenAI)

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Autogen | gpt-4o | ERROR | ERROR | ERROR | ERROR |
| Crewai | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | gpt-4o | ERROR | ERROR | ERROR | ERROR |
| Langgraph | claude-3-sonnet | 4/5 | 4/5 | 5/5 | 13/15 |
| Langgraph | gpt-4o | ERROR | ERROR | ERROR | ERROR |

### Final Average Score by Framework (Claude & OpenAI)

| Framework | Average Score (Claude & OpenAI) |
|-----------|-------------------------------|
| Autogen | 15.00/15 |
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
The business plan covers all essential sections in extensive detail, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk mitigation, and rollout timeline. It provides a comprehensive overview.

**Rationale Quality:** 5/5
The rationale section clearly explains the reasoning behind including each agent and excluding irrelevant ones like the BaseballCoachAgent. The selection of agents covers all critical aspects of a business plan.

**Structure Quality:** 5/5
The structure is impeccably organized with consistent formatting, logical flow between sections, and clear use of markdown hierarchy. It is highly readable and professionally presented.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

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
The business plan covers most major sections like executive summary, market analysis, product strategy, go-to-market plan, financials, team/roles, risks/mitigation, timeline, and conclusion. It provides good depth and coherence across these components.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned justification for the choice of agents and their roles in creating a comprehensive business plan. It clearly explains why the BaseballCoachAgent is irrelevant for this context.

**Structure Quality:** 4/5
The structure is well-organized with clear sections and formatting. It follows a logical flow from the executive summary through all the key plan components.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by gpt-4o

**ERROR:** OpenAI returned non-JSON: ```json
{
  "completeness": 5,
  "completeness_explanation": "The business plan is fully complete, covering all expected sections such as Executive Summary, Market Analysis, Product Strategy, Go-to-Ma...

#### BaseballCoachAgent Handling Examples

```
 Irrelevant agents, such as the BaseballCoachAgent, were not involved as their expertise does not apply to this business context.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections expected, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team structure, risk assessment, timeline, and conclusion. It provides good depth and coherence across these sections.

**Rationale Quality:** 4/5
The rationale for involving specific agents in developing the business plan is clearly explained, highlighting their roles and relevance. The exclusion of the BaseballCoachAgent is also justified as being irrelevant to the context. Overall, there is a good explanation of agent choices and role justifications.

**Structure Quality:** 5/5
The business plan is impeccably organized with consistent formatting, logical flow between sections, and clear use of markdown hierarchy. The structure is highly readable and professionally presented.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by gpt-4o

**ERROR:** OpenAI returned non-JSON: ```json
{
  "completeness": 5,
  "completeness_explanation": "The business plan is fully complete, covering all expected sections with exceptional detail and thoughtfulness. It includes an executive s...

#### BaseballCoachAgent Handling Examples

```


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the business plan's context.
```


---

Report finalized: 2025-06-03T12:00:25.521845
