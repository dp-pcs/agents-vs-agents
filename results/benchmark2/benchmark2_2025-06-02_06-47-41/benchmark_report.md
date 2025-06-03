# Multi-Agent Orchestration Benchmark Report

Generated: 2025-06-03T11:27:24.702284

## Performance Metrics

| Framework | Duration (s) | Agent Turns | Output Length | Message Count |
|-----------|--------------|-------------|----------------|----------------|
| Autogen | 317.15 | 10 | 6655 | 0 |
| Crewai | 227.91 | 3 | 35195 | 0 |
| Langgraph | 248.49 | 10 | 32818 | 0 |

## Agent Selection Capabilities

| Framework | Filtered Irrelevant Agents | Analysis Method |
| Autogen | ? | ? |
| Crewai | ? | ? |
| Langgraph | ? | ? |

## Quality Assessment

| Framework | Completeness | Rationale Quality | Structure Quality | BaseballCoach Handling |
|-----------|--------------|-------------------|-------------------|------------------------|
| Autogen | 1.25/5 | 1.25/5 | 1.25/5 | 5/5 (Properly excluded) |
| Crewai | 1.33/5 | 1.67/5 | 1.33/5 | 5/5 (Properly excluded) |
| Langgraph | 1.33/5 | 1.67/5 | 1.33/5 | 5/5 (Properly excluded) |

## Framework Rankings

| Rank | Framework | Total Score | Completeness | Rationale | Structure |
|------|-----------|-------------|--------------|-----------|----------|
| 1 | Crewai | 4.33/15 | 1.33/5 | 1.67/5 | 1.33/5 |
| 2 | Langgraph | 4.33/15 | 1.33/5 | 1.67/5 | 1.33/5 |
| 3 | Autogen | 3.75/15 | 1.25/5 | 1.25/5 | 1.25/5 |

## Model Scores by Framework

| Framework | Model | Completeness | Rationale Quality | Structure Quality | Total |
|-----------|-------|--------------|-------------------|-------------------|-------|
| Autogen | claude-3-sonnet | 5/5 | 5/5 | 5/5 | 15/15 |
| Autogen | Titan Text Express | 0/5 | 0/5 | 0/5 | 0/15 |
| Autogen | Titan Text Lite | 0/5 | 0/5 | 0/5 | 0/15 |
| Autogen | Titan Text Premier | 0/5 | 0/5 | 0/5 | 0/15 |
| Crewai | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Crewai | Titan Text Express | 0/5 | 0/5 | 0/5 | 0/15 |
| Crewai | Titan Text Premier | 0/5 | 0/5 | 0/5 | 0/15 |
| Langgraph | claude-3-sonnet | 4/5 | 5/5 | 4/5 | 13/15 |
| Langgraph | Titan Text Express | 0/5 | 0/5 | 0/5 | 0/15 |
| Langgraph | Titan Text Premier | 0/5 | 0/5 | 0/5 | 0/15 |

### Final Average Score by Framework (across all models)

| Framework | Average Score (All Models) |
|-----------|--------------------------|
| Autogen | 3.75/15 |
| Crewai | 4.33/15 |
| Langgraph | 4.33/15 |

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
The business plan covers all the major sections expected, including executive summary, market analysis, product strategy, go-to-market plan, financial projections, team and roles, risks and mitigation, and a detailed 12-week rollout timeline. The level of detail provided is exceptional.

**Rationale Quality:** 5/5
The rationale section provides an excellent, well-reasoned explanation for the choice of agents involved and their respective roles in contributing to the different components of the business plan. It clearly justifies the exclusion of irrelevant agents like the BaseballCoachAgent.

**Structure Quality:** 5/5
The business plan is impeccably organized with consistent formatting, clear section headings, and a logical flow from one component to the next. The use of markdown formatting enhances the readability and hierarchical structure.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 15/15**

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
The business plan covers most of the major sections expected, including market analysis, product overview, competitive advantage, business model, financial projections, and an executive summary. However, some sections like detailed marketing and operations plans are missing.

**Rationale Quality:** 5/5
The rationale section provides an excellent and well-reasoned justification for the choice of agents involved, as well as the exclusion of irrelevant agents like the BaseballCoachAgent. The roles and contributions of each agent are clearly explained.

**Structure Quality:** 4/5
The business plan is well-structured, with a logical flow and consistent formatting using markdown. The hierarchy of sections is clear, making it easy to navigate and read.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

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

**ERROR:** An error occurred (ValidationException) when calling the InvokeModel operation: 400 Bad Request: Too many input tokens. Max input tokens: 4096, request input token count: 7262 

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


I chose not to involve agents irrelevant to the task, such as the BaseballCoachAgent, as their expertise does not align with the business and technology focus required for this plan.
```

### Langgraph

#### Evaluation by claude-3-sonnet

**Completeness:** 4/5
The business plan covers most major sections one would expect, including an executive summary, market analysis, product strategy, go-to-market plan, financial projections, team structure, risk assessment, and timeline. It provides good depth on the rationale and thought process behind each component.

**Rationale Quality:** 5/5
The rationale section provides excellent justification for the choice of agents used and how they fit together into a cohesive plan. The exclusion of the BaseballCoachAgent is well-reasoned.

**Structure Quality:** 4/5
The overall structure is logical and well-formatted, with clear section headings. The flow from the rationale into the various plan components is smooth.

**BaseballCoachAgent Handling:** BaseballCoachAgent was properly excluded with explanation — Score: 5/5

**Total Score: 13/15**

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

**ERROR:** An error occurred (ValidationException) when calling the InvokeModel operation: 400 Bad Request: Too many input tokens. Max input tokens: 4096, request input token count: 7039 

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

Report finalized: 2025-06-03T11:27:24.703623
