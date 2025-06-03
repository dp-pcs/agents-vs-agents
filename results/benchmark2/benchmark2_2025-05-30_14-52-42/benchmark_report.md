# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-03T11:25:53.899845

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length | Message Count |
|-----------|--------------|-------------|----------------|----------------|
| Autogen | 227.12 | 9 | 7437 | 0 |
| Crewai | 149.34 | 4 | 5640 | 0 |
| Langgraph | 212.57 | 10 | 32255 | 0 |

## Agent Selection Capabilities

| Framework | Filtered Irrelevant Agents | Analysis Method |
| Autogen | ? | ? |
| Crewai | ? | ? |
| Langgraph | ? | ? |

## Quality Assessment

| Framework | Completeness | Rationale Quality | Structure Quality | BaseballCoach Handling |
|-----------|--------------|-------------------|-------------------|------------------------|
| Autogen | 1.00/5 | 1.00/5 | 1.00/5 | 5/5 (Properly excluded) |
| Crewai | 1.00/5 | 1.25/5 | 1.25/5 | 5/5 (Properly excluded) |
| Langgraph | 1.33/5 | 1.67/5 | 1.67/5 | 5/5 (Properly excluded) |

## Framework Rankings

| Rank | Framework | Total Score | Completeness | Rationale | Structure |
|------|-----------|-------------|--------------|-----------|----------|
| 1 | Langgraph | 4.67/15 | 1.33/5 | 1.67/5 | 1.67/5 |
| 2 | Crewai | 3.50/15 | 1.00/5 | 1.25/5 | 1.25/5 |
| 3 | Autogen | 3.00/15 | 1.00/5 | 1.00/5 | 1.00/5 |

## Model Scores by Framework

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 4/5 | 4/5 | 4/5 | 12/15 |
| Autogen | Titan Text Express | 0/5 | 0/5 | 0/5 | 0/15 |
| Autogen | Titan Text Lite | 0/5 | 0/5 | 0/5 | 0/15 |
| Autogen | Titan Text Premier | 0/5 | 0/5 | 0/5 | 0/15 |
| Crewai | claude-3-sonnet | 4/5 | 5/5 | 5/5 | 14/15 |
| Crewai | Titan Text Express | 0/5 | 0/5 | 0/5 | 0/15 |
| Crewai | Titan Text Lite | 0/5 | 0/5 | 0/5 | 0/15 |
| Crewai | Titan Text Premier | 0/5 | 0/5 | 0/5 | 0/15 |
| Langgraph | claude-3-sonnet | 4/5 | 5/5 | 5/5 | 14/15 |
| Langgraph | Titan Text Express | 0/5 | 0/5 | 0/5 | 0/15 |
| Langgraph | Titan Text Premier | 0/5 | 0/5 | 0/5 | 0/15 |

### Final Average Score by Framework (across all models)

| Framework | Average Score (All Models) |
|-----------|--------------------------|
| Autogen | 3.00/15 |
| Crewai | 3.50/15 |
| Langgraph | 4.67/15 |

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
- Completed in 227.12 seconds with 9 agent turns

#### Crewai

- Failed to filter out the irrelevant BaseballCoachAgent
- The BaseballCoachAgent participated in the conversation despite being irrelevant
- Completed in 149.34 seconds with 4 agent turns

#### Langgraph

- Failed to filter out the irrelevant BaseballCoachAgent
- The BaseballCoachAgent participated in the conversation despite being irrelevant
- Completed in 212.57 seconds with 10 agent turns


---

## Detailed Evaluations

### Autogen

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most of the major sections expected, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, and team roles. It provides good depth and detail in each section.

**Rationale Quality:** 4/5
The rationale for including and excluding agents is clearly explained. The chosen agents align well with the needs of creating a comprehensive business plan for an AI productivity app launch. The reasoning for not using the BaseballCoachAgent is also provided.

**Structure Quality:** 4/5
The business plan is well-structured and organized into logical sections with clear headings. The formatting is consistent and readable, making it easy to follow the flow of information.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 12/15**

#### Evaluation by Claude 3 Sonnet

**ERROR:** An error occurred (ValidationException) when calling the InvokeModel operation: Malformed input request: #: subject must not be valid against schema {"required":["messages"]}#: required key [max_tokens] not found, please reformat your input and try again.

#### Evaluation by Claude 3 Haiku

**ERROR:** An error occurred (ValidationException) when calling the InvokeModel operation: Malformed input request: #: subject must not be valid against schema {"required":["messages"]}#: required key [max_tokens] not found, please reformat your input and try again.

#### Evaluation by Titan Text Express

**Completeness:** ?/5
No explanation provided.

**Rationale Quality:** ?/5
No explanation provided.

**Structure Quality:** ?/5
No explanation provided.

**BaseballCoachAgent Handling:** Unknown BaseballCoachAgent handling — Score: ?/5

#### Evaluation by Titan Text Lite

**Completeness:** ?/5
No explanation provided.

**Rationale Quality:** ?/5
No explanation provided.

**Structure Quality:** ?/5
No explanation provided.

**BaseballCoachAgent Handling:** Unknown BaseballCoachAgent handling — Score: ?/5

#### Evaluation by Titan Text Premier

**Completeness:** ?/5
No explanation provided.

**Rationale Quality:** ?/5
No explanation provided.

**Structure Quality:** ?/5
No explanation provided.

**BaseballCoachAgent Handling:** Unknown BaseballCoachAgent handling — Score: ?/5

#### Evaluation by Command R+

**ERROR:** An error occurred (ValidationException) when calling the InvokeModel operation: The provided Content Type is invalid or not supported for this model

#### Evaluation by Mistral 7B Instruct

**ERROR:** An error occurred (ValidationException) when calling the InvokeModel operation: The provided Content Type is invalid or not supported for this model

#### Evaluation by Mixtral 8x7B Instruct

**ERROR:** An error occurred (ValidationException) when calling the InvokeModel operation: The provided Content Type is invalid or not supported for this model

#### Evaluation by Mistral Large

**ERROR:** An error occurred (ValidationException) when calling the InvokeModel operation: The provided Content Type is invalid or not supported for this model

#### BaseballCoachAgent Handling Examples

BaseballCoachAgent was not used in the conversation.

### Crewai

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers all major sections expected for a comprehensive plan, including market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, rollout timeline, and a conclusion. It provides good depth and coherence across these sections.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the choice of agents and their roles in developing the business plan. It clearly justifies the exclusion of the BaseballCoachAgent as irrelevant to the business context.

**Structure Quality:** 5/5
The business plan is impeccably organized with clear section headings, consistent formatting using Markdown, and a logical flow from one section to the next. The hierarchy of information is evident, making it easy to read and follow.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### Evaluation by Claude 3 Sonnet

**ERROR:** An error occurred (ValidationException) when calling the InvokeModel operation: Malformed input request: #: subject must not be valid against schema {"required":["messages"]}#: required key [max_tokens] not found, please reformat your input and try again.

#### Evaluation by Claude 3 Haiku

**ERROR:** An error occurred (ValidationException) when calling the InvokeModel operation: Malformed input request: #: subject must not be valid against schema {"required":["messages"]}#: required key [max_tokens] not found, please reformat your input and try again.

#### Evaluation by Titan Text Express

**Completeness:** ?/5
No explanation provided.

**Rationale Quality:** ?/5
No explanation provided.

**Structure Quality:** ?/5
No explanation provided.

**BaseballCoachAgent Handling:** Unknown BaseballCoachAgent handling — Score: ?/5

#### Evaluation by Titan Text Lite

**Completeness:** ?/5
No explanation provided.

**Rationale Quality:** ?/5
No explanation provided.

**Structure Quality:** ?/5
No explanation provided.

**BaseballCoachAgent Handling:** Unknown BaseballCoachAgent handling — Score: ?/5

#### Evaluation by Titan Text Premier

**Completeness:** ?/5
No explanation provided.

**Rationale Quality:** ?/5
No explanation provided.

**Structure Quality:** ?/5
No explanation provided.

**BaseballCoachAgent Handling:** Unknown BaseballCoachAgent handling — Score: ?/5

#### Evaluation by Command R+

**ERROR:** An error occurred (ValidationException) when calling the InvokeModel operation: The provided Content Type is invalid or not supported for this model

#### Evaluation by Mistral 7B Instruct

**ERROR:** An error occurred (ValidationException) when calling the InvokeModel operation: The provided Content Type is invalid or not supported for this model

#### Evaluation by Mixtral 8x7B Instruct

**ERROR:** An error occurred (ValidationException) when calling the InvokeModel operation: The provided Content Type is invalid or not supported for this model

#### Evaluation by Mistral Large

**ERROR:** An error occurred (ValidationException) when calling the InvokeModel operation: The provided Content Type is invalid or not supported for this model

#### BaseballCoachAgent Handling Examples

```


Agents not used:
- **BaseballCoachAgent**: This agent was not relevant to the business plan as it focuses on sports coaching rather than business strategy.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections like executive summary, market analysis, product strategy, go-to-market plan, financials, team, risks, and timeline. It provides good depth and detail across these components.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned justification for including each agent and their roles in developing the business plan. It clearly explains how the agents work together cohesively to address all critical aspects.

**Structure Quality:** 5/5
The plan follows a logical structure with clear sections and formatting. The flow between sections is smooth, with each component building upon the previous one. The markdown formatting is consistent and polished.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 14/15**

#### Evaluation by Claude 3 Sonnet

**ERROR:** An error occurred (ValidationException) when calling the InvokeModel operation: Malformed input request: #: subject must not be valid against schema {"required":["messages"]}#: required key [max_tokens] not found, please reformat your input and try again.

#### Evaluation by Claude 3 Haiku

**ERROR:** An error occurred (ValidationException) when calling the InvokeModel operation: Malformed input request: #: subject must not be valid against schema {"required":["messages"]}#: required key [max_tokens] not found, please reformat your input and try again.

#### Evaluation by Titan Text Express

**Completeness:** ?/5
No explanation provided.

**Rationale Quality:** ?/5
No explanation provided.

**Structure Quality:** ?/5
No explanation provided.

**BaseballCoachAgent Handling:** Unknown BaseballCoachAgent handling — Score: ?/5

#### Evaluation by Titan Text Lite

**ERROR:** An error occurred (ValidationException) when calling the InvokeModel operation: 400 Bad Request: Too many input tokens. Max input tokens: 4096, request input token count: 6966 

#### Evaluation by Titan Text Premier

**Completeness:** ?/5
No explanation provided.

**Rationale Quality:** ?/5
No explanation provided.

**Structure Quality:** ?/5
No explanation provided.

**BaseballCoachAgent Handling:** Unknown BaseballCoachAgent handling — Score: ?/5

#### Evaluation by Command R+

**ERROR:** An error occurred (ValidationException) when calling the InvokeModel operation: The provided Content Type is invalid or not supported for this model

#### Evaluation by Mistral 7B Instruct

**ERROR:** An error occurred (ValidationException) when calling the InvokeModel operation: The provided Content Type is invalid or not supported for this model

#### Evaluation by Mixtral 8x7B Instruct

**ERROR:** An error occurred (ValidationException) when calling the InvokeModel operation: The provided Content Type is invalid or not supported for this model

#### Evaluation by Mistral Large

**ERROR:** An error occurred (ValidationException) when calling the InvokeModel operation: The provided Content Type is invalid or not supported for this model

#### BaseballCoachAgent Handling Examples

```


I chose not to involve the **BaseballCoachAgent** as it is irrelevant to the context of a business plan for an AI productivity app.
```


---

Report finalized: 2025-06-03T11:25:53.904269
