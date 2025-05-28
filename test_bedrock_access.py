import boto3
import json

bedrock_models = [
    ("arn:aws:bedrock:us-east-1:082830052325:inference-profile/us.anthropic.claude-opus-4-20250514-v1:0", "Claude Opus 4", "anthropic"),
    ("arn:aws:bedrock:us-east-1:082830052325:inference-profile/us.anthropic.claude-sonnet-4-20250514-v1:0", "Claude Sonnet 4", "anthropic"),
    ("arn:aws:bedrock:us-east-1:082830052325:inference-profile/us.anthropic.claude-3-7-sonnet-20250219-v1:0", "Claude 3.7 Sonnet", "anthropic"),
    ("arn:aws:bedrock:us-east-1:082830052325:inference-profile/us.deepseek.r1-v1:0", "DeepSeek-R1", "deepseek"),
]

def get_body_for_model(family):
    if family == "anthropic":
        return {
            "messages": [
                {"role": "user", "content": "Say hello."}
            ],
            "max_tokens": 5,
            "temperature": 0.1,
            "anthropic_version": "bedrock-2023-05-31"
        }
    elif family == "deepseek":
        # Return a list of body variants to try
        return [
            # Variant A: messages + inferenceConfig
            {
                "inferenceConfig": {
                    "max_tokens": 5,
                    "temperature": 0.1,
                    "top_p": 0.9
                },
                "messages": [
                    {"role": "user", "content": "Say hello."}
                ]
            },
            # Variant B: messages + max_tokens
            {
                "messages": [
                    {"role": "user", "content": "Say hello."}
                ],
                "max_tokens": 5
            },
            # Variant C: input + max_tokens
            {
                "input": "Say hello.",
                "max_tokens": 5
            }
        ]

    else:
        return {
            "prompt": "Say hello.",
            "max_tokens": 5,
            "temperature": 0.1
        }


bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
prompt = "Say hello."

for model_id, label, family in bedrock_models:
    if family == "deepseek":
        bodies = get_body_for_model(family)
        for i, body in enumerate(bodies):
            try:
                print(f"Trying DeepSeek body variant {i+1} for {label}: {json.dumps(body)}")
                response = bedrock.invoke_model(
                    modelId=model_id,
                    body=json.dumps(body),
                    accept="application/json",
                    contentType="application/json"
                )
                print(f"{label} (variant {i+1}): ACCESS ")
                print(f"{label} (variant {i+1}): ACCESS ")
                break
            except Exception as e:
                print(f"{label} (variant {i+1}): ACCESS  ({e.__class__.__name__}: {e})")
    else:
        try:
            body = get_body_for_model(family)
            response = bedrock.invoke_model(
                modelId=model_id,
                body=json.dumps(body),
                accept="application/json",
                contentType="application/json"
            )
            print(f"{label}: ACCESS ")
            print(f"{label}: ACCESS ")
        except Exception as e:
            print(f"{label}: ACCESS  ({e.__class__.__name__}: {e})")
