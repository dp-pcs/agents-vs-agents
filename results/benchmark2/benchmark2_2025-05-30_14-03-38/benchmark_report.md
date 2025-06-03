# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-03T11:53:11.597192

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length | Message Count |
|-----------|--------------|-------------|----------------|----------------|
| Autogen | 173.28 | 9 | 6030 | 0 |
| Crewai | 232.5 | 56 | 34847 | 0 |
| Langgraph | 176.56 | 10 | 31975 | 0 |

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

## Model Scores by Framework

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Crewai | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Langgraph | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |

### Final Average Score by Framework (across all models)

| Framework | Average Score (All Models) |
|-----------|--------------------------|
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
The business plan covers all the essential sections with exceptional detail and thoughtfulness, including the executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risks and mitigation strategies, and a 12-week rollout timeline.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned justification for the selection of agents and their roles in creating a comprehensive business plan. It clearly explains the relevance of each agent and how their contributions address different aspects of the business plan.

**Structure Quality:** 5/5
The business plan is impeccably organized, with a clear hierarchy and logical flow of sections. The formatting is consistent, and the use of headings and subheadings makes it easy to navigate.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by gpt-4o

**ERROR:** OpenAI returned non-JSON: ```json
{
  "completeness": 5,
  "completeness_explanation": "The business plan is fully complete, covering all expected sections such as Executive Summary, Market Analysis, Product Strategy, Go-to-Ma...

#### BaseballCoachAgent Handling Examples

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections expected, including Executive Summary, Market Analysis, Financial Projections, and Conclusion. It provides good depth and coherence across these sections.

**Rationale Quality:** 5/5
The rationale section clearly explains the selection of relevant agents and their roles, as well as the exclusion of irrelevant agents like the BaseballCoachAgent. The reasoning for agent choices is well-justified and aligned with the business context.

**Structure Quality:** 4/5
The overall structure is well-organized, with a logical flow between sections and consistent formatting using Markdown. The hierarchy of sections is clear and readable.

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
The provided content covers most major sections expected in a business plan, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team, risk assessment, timeline, and conclusion. The level of detail is good overall.

**Rationale Quality:** 5/5
The rationale for selecting and excluding agents is clearly explained, with well-reasoned justifications provided for each choice based on relevance to the business plan context. The roles of the chosen agents are logically mapped to the different components of the plan.

**Structure Quality:** 4/5
The content is well-structured, with a logical flow between sections and clear formatting using markdown headings and bullet points. The overall organization and readability are good.

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

Report finalized: 2025-06-03T11:53:11.598604
