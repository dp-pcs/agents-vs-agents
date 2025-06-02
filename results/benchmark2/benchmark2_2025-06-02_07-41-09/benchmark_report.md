# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-02T14:05:59.686888

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length | Message Count |
|-----------|--------------|-------------|----------------|----------------|
| Autogen | 292.46 | 11 | 4956 | 0 |
| Crewai | 144.79 | 2 | 6368 | 0 |
| Langgraph | 234.81 | 10 | 31099 | 0 |

## Agent Selection Capabilities

| Framework | Filtered Irrelevant Agents | Analysis Method |
| Autogen | ? | ? |
| Crewai | ? | ? |
| Langgraph | ? | ? |

## Quality Assessment

| Framework | Completeness | Rationale Quality | Structure Quality | BaseballCoach Handling |
|-----------|--------------|-------------------|-------------------|------------------------|
| Autogen | 4.80/5 | 5.00/5 | 5.00/5 | 5/5 (Properly excluded) |
| Crewai | 3.50/5 | 4.17/5 | 3.50/5 | 5/5 (Properly excluded) |
| Langgraph | 2.67/5 | 3.17/5 | 3.00/5 | 5/5 (Properly excluded) |

## Framework Rankings

| Rank | Framework | Total Score | Completeness | Rationale | Structure |
|------|-----------|-------------|--------------|-----------|----------|
| 1 | Autogen | 14.80/15 | 4.80/5 | 5.00/5 | 5.00/5 |
| 2 | Crewai | 11.17/15 | 3.50/5 | 4.17/5 | 3.50/5 |
| 3 | Langgraph | 8.83/15 | 2.67/5 | 3.17/5 | 3.00/5 |

## Model Scores by Framework

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Autogen | Claude 3 Opus | 4/5 | 5/5 | 5/5 | 14/15 |
| Autogen | Claude 3 Sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Autogen | Claude 3 Haiku | 5/5 | 5/5 | 5/5 | 15/15 |
| Autogen | Titan Text Express | 5/5 | 5/5 | 5/5 | 15/15 |
| Crewai | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | Claude 3 Opus | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | Claude 3 Sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | Claude 3 Haiku | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | Titan Text Express | 5/5 | 5/5 | 5/5 | 15/15 |
| Langgraph | claude-3-sonnet | 4/5 | 4/5 | 4/5 | 12/15 |
| Langgraph | Claude 3 Opus | 4/5 | 5/5 | 5/5 | 14/15 |
| Langgraph | Claude 3 Sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Langgraph | Claude 3 Haiku | 4/5 | 5/5 | 5/5 | 14/15 |
| Langgraph | Titan Text Express | 0/5 | 0/5 | 0/5 | 0/15 |

### Final Average Score by Framework (across all models)

| Framework | Average Score (All Models) |
|-----------|--------------------------|
| Autogen | 14.80/15 |
| Crewai | 11.17/15 |
| Langgraph | 8.83/15 |

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
- Completed in 292.46 seconds with 11 agent turns

#### Crewai

- Failed to filter out the irrelevant BaseballCoachAgent
- The BaseballCoachAgent participated in the conversation despite being irrelevant
- Completed in 144.79 seconds with 2 agent turns

#### Langgraph

- Failed to filter out the irrelevant BaseballCoachAgent
- The BaseballCoachAgent participated in the conversation despite being irrelevant
- Completed in 234.81 seconds with 10 agent turns


---

## Detailed Evaluations

### Autogen

#### Evaluation by claude-3-sonnet

**Completeness:** 5/5
The business plan covers all expected sections in detail, including Executive Summary, Market Analysis, Product Strategy, Go-to-Market Plan, Financial Projections, Team & Roles, Risks & Mitigation, 12-Week Rollout Timeline, and Conclusion. The depth and thoughtfulness of content across these sections indicate exceptional completeness.

**Rationale Quality:** 5/5
The rationale provided clearly explains the reasoning behind selecting specific agents based on their expertise and how they contribute to an integrated strategy covering different aspects of the business plan. The exclusion of irrelevant agents like the BaseballCoachAgent is also explicitly justified.

**Structure Quality:** 5/5
The business plan follows a logical structure with consistent formatting and clear section hierarchy using markdown. The flow between sections is coherent, and the overall organization is impeccable, making it easy to navigate and read.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Opus

**Completeness:** 4/5
The business plan covers all major sections with good depth and coherence, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, rollout timeline, and conclusion.

**Rationale Quality:** 5/5
The rationale provided is excellent, well-reasoned, and clearly explains the selection of relevant agents for each aspect of the business plan, while explicitly excluding the BaseballCoachAgent as irrelevant.

**Structure Quality:** 5/5
The business plan is impeccably organized, with consistent formatting, clear markdown hierarchy, and a logical flow across sections.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 5/5
The business plan covers all the major sections expected, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, rollout timeline, and conclusion. The sections are comprehensive and provide exceptional detail.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the agent choices and their roles in the business planning process. It clearly justifies why certain agents were included and why others like the BaseballCoachAgent were excluded as irrelevant.

**Structure Quality:** 5/5
The business plan is impeccably organized with a clear hierarchy, consistent formatting using markdown, and logical flow between sections. The structure makes it easy to read and navigate.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 5/5
The business plan covers all major sections expected, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, rollout timeline, and conclusion. The sections are fleshed out with good detail.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the agent choices and their roles in contributing to an integrated business strategy. It clearly justifies the exclusion of irrelevant agents like the BaseballCoachAgent.

**Structure Quality:** 5/5
The business plan is impeccably organized with consistent formatting, logical flow between sections, and a clear markdown hierarchy. The structure aids readability and professional presentation.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

#### Evaluation by Titan Text Express

**Completeness:** 5/5
All required sections included with good depth and coherence.

**Rationale Quality:** 5/5
Excellent, well-reasoned rationale for all major decisions and exclusions, including agent choices and role justifications.

**Structure Quality:** 5/5
Well-structured, readable, and professionally formatted.

**BaseballCoachAgent Handling:** BaseballCoachAgent was not mentioned at all — Score: 0/5

**Total Score: 15/15**

#### Evaluation by Titan Text Lite

**ERROR:** Could not parse Bedrock response: Extra data: line 17 column 1 (char 297)

**Raw Output:**
```
```
```tabular-data-json
{
    "rows": [
        {
            "Category": "Rationale Quality",
            "Score": "4"
        },
        {
            "Category": "Structure Quality",
            "Score": "4"
        },
        {
            "Category": "BaseballCoachAgent",
            "Score": "0"
        }
    ]
}
```

```tabular-data-json
{
    "rows": [
        {
            "Category": "Rationale Quality",
            "Score": "4"
        },
        {
            "Category": "Structure ...
```



#### BaseballCoachAgent Handling Examples

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections expected, such as market analysis, product strategy, go-to-market plan, financial projections, team structure, risk analysis, and rollout timeline. It provides good depth and coherence across these sections.

**Rationale Quality:** 5/5
The rationale for the selection of agents is well-explained, highlighting their relevance to different aspects of the business plan. The exclusion of the BaseballCoachAgent is also clearly justified as being irrelevant to the task at hand. The overall reasoning behind the agent choices and their roles is excellent.

**Structure Quality:** 4/5
The business plan follows a logical structure with clear sections and formatting. The flow between sections is smooth, and the use of markdown formatting enhances readability. Overall, the structure is well-organized and professionally presented.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Opus

**Completeness:** 4/5
The business plan covers most essential sections such as market analysis, product strategy, go-to-market plan, financial projections, team structure, risk mitigation, and launch timeline. It provides good depth and coherence across these components.

**Rationale Quality:** 5/5
The rationale for involving different expert agents and their roles is clearly explained. The reasoning for excluding irrelevant agents like the BaseballCoachAgent is also provided, demonstrating thoughtful consideration.

**Structure Quality:** 4/5
The business plan is well-structured with logical sections and clear formatting using markdown. The flow between sections is coherent, making it easy to read and navigate.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 4/5
The business plan covers all major sections expected, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, and a 12-week rollout timeline. The sections are generally covered with good depth and coherence.

**Rationale Quality:** 5/5
The rationale for including or excluding specific agents is well-explained, providing clear justifications for the choices made based on the relevance and alignment of the agents' expertise with the task of developing a business plan for an AI productivity app.

**Structure Quality:** 4/5
The business plan is well-structured, with logical section flow and consistent formatting using markdown hierarchy. The overall presentation is readable and professionally formatted.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 4/5
The business plan covers most major sections one would expect, including market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, and a rollout timeline. It provides good depth and coherence across these sections.

**Rationale Quality:** 5/5
The rationale section provides an excellent explanation for the choice of agents involved in developing the business plan, clearly justifying their relevance and roles. It also explicitly addresses the exclusion of the BaseballCoachAgent as irrelevant to the productivity app context.

**Structure Quality:** 4/5
The business plan is well-structured, with clear sections and logical flow. The formatting is consistent and readable, adhering to professional standards.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Titan Text Express

**Completeness:** 5/5
All required sections included with exceptional detail and thoughtfulness.

**Rationale Quality:** 5/5
Excellent, well-reasoned rationale for all major decisions and exclusions, including agent choices and role justifications.

**Structure Quality:** 5/5
Impeccably organized with consistent formatting, logical section flow, and clear markdown hierarchy.

**BaseballCoachAgent Handling:** BaseballCoachAgent was not mentioned at all — Score: 0/5

**Total Score: 15/15**




#### BaseballCoachAgent Handling Examples

```


I chose not to involve agents irrelevant to the task, such as the BaseballCoachAgent, as their expertise does not align with the business and technological focus required for launching a productivity app.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most of the key sections expected, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risk analysis, timeline, and conclusion. It provides good depth and detail across these sections.

**Rationale Quality:** 4/5
The rationale for including each agent and their respective roles is well-explained, highlighting how they contribute to a comprehensive business plan. The reasoning for excluding the BaseballCoachAgent is also clearly stated.

**Structure Quality:** 4/5
The business plan follows a logical structure with well-formatted sections. The flow between sections is coherent, and the use of headings and subheadings enhances readability.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 12/15**

#### Evaluation by Claude 3 Opus

**Completeness:** 4/5
The business plan covers all major sections one would expect, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risk analysis, timeline, and conclusion. The depth and detail provided in each section is good.

**Rationale Quality:** 5/5
The rationale for including each agent is clearly explained, highlighting their specific roles and contributions to the overall business plan. The reasoning for excluding the BaseballCoachAgent is also provided and makes sense given the context.

**Structure Quality:** 5/5
The structure and organization of the business plan is excellent. The sections flow logically, the formatting is consistent and professional, and the use of headings/subheadings makes it easy to navigate.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 4/5
The business plan covers most of the key sections expected, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risk mitigation, timeline, and conclusion. It provides good depth and detail across these sections.

**Rationale Quality:** 5/5
The rationale for including each agent and how they contribute to the overall plan is clearly explained. The reasoning for excluding the BaseballCoachAgent is also provided and makes sense given the context of an AI productivity app.

**Structure Quality:** 4/5
The plan follows a logical structure with sections flowing coherently. Formatting is generally good, though could potentially be improved with better use of headings and spacing.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

#### Evaluation by Claude 3 Haiku

**Completeness:** 4/5
The business plan covers most major sections like executive summary, market analysis, product strategy, go-to-market plan, financial projections, team roles, risk assessment, timeline, and conclusion. It provides good depth and coherence across these components.

**Rationale Quality:** 5/5
The rationale for including each agent and how they contribute to the overall plan is clearly and thoroughly explained. The reasoning for excluding the BaseballCoachAgent is also justified.

**Structure Quality:** 5/5
The plan follows a logical structure with clear sections and formatting. The markdown hierarchy and flow between sections is excellent.

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


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the context of a business plan for an AI productivity app.
```


---

Report finalized: 2025-06-02T14:05:59.691190
