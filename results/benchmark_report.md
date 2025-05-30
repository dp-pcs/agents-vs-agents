# Multi-Agent Orchestration Benchmark Report

Generated: 2025-05-29T15:17:24.497859

## Performance Metrics

| Framework | Duration (seconds) | Agent Turns | Output Length (chars) |
|-----------|-------------------|-------------|----------------------|
| Autogen | 193.74 | 9 | 6770 |
| Crewai | 195.55 | 5 | 33822 |
| Langgraph | 161.28 | 10 | 31043 |

## Agent Selection Capabilities

| Framework | Filtered Irrelevant Agents | Detection Details |
|-----------|----------------------------|-------------------|
| Autogen | No | Detection method: Text analysis.
BaseballCoachAgent appears to have been used despite being irrelevant. |
| Crewai | Yes | Detection method: Text analysis.
BaseballCoachAgent was not mentioned, suggesting it was filtered out. |
| Langgraph | Yes | Detection method: Text analysis.
BaseballCoachAgent was mentioned but in context of being excluded. |

## Quality Assessment

| Framework | Completeness | Rationale Quality | Structure Quality | BaseballCoach Handling |
|-----------|--------------|-------------------|-------------------|------------------------|
| Crewai | 3.00/3 | 3.00/3 | 3.00/3 | 2 (Properly excluded) |
| Autogen | 3.00/3 | 2.33/3 | 3.00/3 | 0 (Not mentioned) |
| Langgraph | 2.67/3 | 2.00/3 | 2.67/3 | 0 (Not mentioned) |

## Framework Rankings

| Rank | Framework | Total Score | Completeness | Rationale | Structure |
|------|-----------|-------------|--------------|-----------|----------|
| 1 | Crewai | 9.00/9 | 3.00/3 | 3.00/3 | 3.00/3 |
| 2 | Autogen | 8.33/9 | 3.00/3 | 2.33/3 | 3.00/3 |
| 3 | Langgraph | 7.33/9 | 2.67/3 | 2.00/3 | 2.67/3 |

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
- Completed in 193.74 seconds with 9 agent turns

#### Crewai

- Successfully filtered out the irrelevant BaseballCoachAgent
- The output did not use the BaseballCoachAgent
- Completed in 195.55 seconds with 5 agent turns

#### Langgraph

- Successfully filtered out the irrelevant BaseballCoachAgent
- The output did not use the BaseballCoachAgent
- Completed in 161.28 seconds with 10 agent turns


---

## Detailed Evaluations

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 3/3
The business plan covers all the key sections expected in a professional business plan, including Executive Summary, Market Analysis, Product Strategy, Go-to-Market Plan, Financial Projections, Team & Roles, Risks & Mitigation, 12-Week Rollout Timeline, and Conclusion. Additionally, it provides a rationale section at the top, mentioning the agents used and their roles.

**Rationale Quality:** 3/3
The rationale section clearly explains why each agent was used and the role they played in developing the business plan. It also mentions the BaseballCoachAgent and explains why it was excluded due to being irrelevant for a tech product business plan.

**Structure Quality:** 3/3
The business plan follows a clear structure with well-organized sections and professional formatting. The sections flow logically, with appropriate headings and consistent formatting throughout.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation

**Total Score: 9.00/9**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 3/3
The business plan covers all the required sections in appropriate detail, including the Executive Summary, Market Analysis, Product Strategy, Go-to-Market Plan, Financial Projections, Team & Roles, Risks & Mitigation, 12-Week Rollout Timeline, and Conclusion. It also provides a clear rationale at the top, mentioning the agents used and their roles.

**Rationale Quality:** 3/3
The rationale section clearly explains why each agent was used and their specific contributions to the business plan. It also mentions the BaseballCoachAgent and justifies its exclusion as irrelevant to the task. The reasoning behind strategic decisions is well-explained throughout the plan.

**Structure Quality:** 3/3
The business plan follows a professional structure with clear sections and headings. The flow between sections is logical, and the formatting is consistent, making it easy to read and navigate.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation

**Total Score: 9.00/9**

#### Evaluation by Claude 3 Haiku

**Completeness:** 3/3
The business plan covers all the required sections, including Executive Summary, Market Analysis, Product Strategy, Go-to-Market, Financial Projections, Team & Roles, Risks & Mitigation, 12-Week Rollout Timeline, Conclusion, and a detailed rationale at the top explaining the agents used and the reasoning behind strategic decisions.

**Rationale Quality:** 3/3
The rationale section provides a clear and comprehensive explanation of the agents used in developing the business plan, including why certain agents (such as BaseballCoachAgent) were not used. The reasoning behind the strategic decisions is also well-explained.

**Structure Quality:** 3/3
The business plan is well-organized, with clear markdown sections in the required order. The flow between sections is logical, and the formatting is professional and easy to follow.

**BaseballCoachAgent Handling:** BaseballCoachAgent was not mentioned at all

**Total Score: 9.00/9**

### Autogen

#### Evaluation by claude-3-sonnet

**Completeness:** 3/3
The business plan covers all the required sections in appropriate detail, including the Executive Summary, Market Analysis, Product Strategy, Go-to-Market Plan, Financial Projections, Team & Roles, Risks & Mitigation, 12-Week Rollout Timeline, and Conclusion. A rationale is provided at the top.

**Rationale Quality:** 2/3
The business plan provides an adequate rationale for the overall strategy and approach, explaining the reasoning behind key decisions such as the product features, marketing tactics, and financial projections. However, it does not explicitly mention the BaseballCoachAgent or explain why it was excluded.

**Structure Quality:** 3/3
The business plan is well-structured and follows a logical flow with clear section headings and formatting. The organization and structure align with standard business plan formats, making it easy to read and navigate.

**BaseballCoachAgent Handling:** BaseballCoachAgent was not mentioned at all

**Total Score: 8.00/9**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 3/3
The business plan covers all the required sections in appropriate detail, including the Executive Summary, Market Analysis, Product Strategy, Go-to-Market Plan, Financial Projections, Team & Roles, Risks & Mitigation, 12-Week Rollout Timeline, and Conclusion. It also provides a rationale at the top mentioning the use of AI agents.

**Rationale Quality:** 2/3
The plan provides an adequate rationale for the use of AI agents in the product strategy section, mentioning the integration of AI technology for task automation, prioritization, and resource management. However, it does not explicitly mention the BaseballCoachAgent or explain why it was excluded.

**Structure Quality:** 3/3
The business plan is well-structured, with clear sections following a standard format. The markdown headers are consistent, and the flow between sections is logical and easy to follow. The formatting is professional and readable.

**BaseballCoachAgent Handling:** BaseballCoachAgent was not mentioned at all

**Total Score: 8.00/9**

#### Evaluation by Claude 3 Haiku

**Completeness:** 3/3
The business plan covers all the required sections, including Executive Summary, Market Analysis, Product Strategy, Go-to-Market, Financial Projections, Team & Roles, Risks & Mitigation, and a 12-Week Rollout Timeline. The plan also includes a rationale at the top, which explains the overall vision and approach for the AI Productivity App launch.

**Rationale Quality:** 3/3
The rationale provided in the Executive Summary and throughout the plan clearly explains the key strategic decisions, such as the focus on AI integration, market alignment, and differentiation. It also mentions the exclusion of the BaseballCoachAgent and provides a reasonable explanation for not including it.

**Structure Quality:** 3/3
The business plan is well-organized, with clear section headers and a logical flow. The formatting is professional, and the content is easy to read and follow.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation

**Total Score: 9.00/9**

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 2/3
The business plan covers most of the key sections, including Executive Summary, Market Analysis, Product Strategy, and provides some details in each section. However, it lacks sections on Go-to-Market strategy, Financial Projections, Team & Roles, Risks & Mitigation, 12-Week Rollout Timeline, and a Conclusion.

**Rationale Quality:** 1/3
The business plan does not provide a clear rationale for the use or exclusion of specific agents, including the BaseballCoachAgent. It does not explain the reasoning behind strategic decisions.

**Structure Quality:** 2/3
The business plan follows a good structure with clear sections and headings. The flow between sections is logical, and the formatting is consistent.

**BaseballCoachAgent Handling:** BaseballCoachAgent was not mentioned at all

**Total Score: 5.00/9**

#### Evaluation by Claude 3 Sonnet

**Completeness:** 3/3
The business plan covers all the required sections, including Executive Summary, Market Analysis, Product Strategy, Go-to-Market Plan, Financial Projections, Team & Roles, Risks & Mitigation, 12-Week Rollout Timeline, and a Conclusion. It also provides a rationale at the top.

**Rationale Quality:** 2/3
The business plan provides an adequate rationale for the product strategy and target market. However, it does not explicitly mention the BaseballCoachAgent or explain why it was excluded.

**Structure Quality:** 3/3
The business plan is well-structured, with clear sections and headings. It follows a logical flow and is easy to read and navigate.

**BaseballCoachAgent Handling:** BaseballCoachAgent was not mentioned at all

**Total Score: 8.00/9**

#### Evaluation by Claude 3 Haiku

**Completeness:** 3/3
The business plan covers all the required sections, including Executive Summary, Market Analysis, Product Strategy, Go-to-Market Plan, Financial Projections, Team & Roles, Risks & Mitigation, and a 12-Week Rollout Timeline. It also includes a rationale section at the top that explains the key agents used and the reasoning behind strategic decisions.

**Rationale Quality:** 3/3
The rationale section provides a clear and comprehensive explanation for the key decisions made in the business plan. It explains the reasoning behind the choice of agents, the target market, the unique value proposition, and the go-to-market strategy. The plan also mentions the BaseballCoachAgent and explains why it was excluded from the solution.

**Structure Quality:** 3/3
The business plan is well-organized, with clear and consistent headers for each section. The flow between sections is logical, and the formatting is professional, making it easy to read and understand.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation

**Total Score: 9.00/9**

