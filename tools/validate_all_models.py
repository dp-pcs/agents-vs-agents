import boto3
import json
import os
from botocore.exceptions import BotoCoreError, ClientError
from bedrock_models_supported import LLM_MODELS

REGION = "us-east-1"
OUTPUT_VALID = "bedrock_models_validated.py"
OUTPUT_SKIPPED = "models_skipped_due_to_access.json"
PROMPT = "Summarize the benefits of artificial intelligence in simple terms."

def get_bedrock_client():
    return boto3.client("bedrock-runtime", region_name=REGION)

def format_input(model, prompt):
    if model["api_type"] == "messages":
        return json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "messages": [{ "role": "user", "content": prompt }],
            "max_tokens": 300
        })
    elif model["provider"] == "Amazon":
        return json.dumps({
            "inputText": prompt,
            "textGenerationConfig": {
                "maxTokenCount": 200,
                "temperature": 0.7,
                "topP": 0.9
            }
        })
    elif model["provider"] == "AI21":
        return json.dumps({
            "prompt": prompt,
            "numResults": 1,
            "maxTokens": 200,
            "temperature": 0.7
        })
    elif model["provider"] == "Cohere":
        return json.dumps({
            "chat_history": [
                {
                    "role": "USER",
                    "message": "What is an interesting new role in AI if I don't have an ML background"
                },
                {
                    "role": "CHATBOT",
                    "message": "You could explore being a prompt engineer!"
                }
            ],
            "message": prompt
        })
    else:  # Meta, Mistral, etc.
        return json.dumps({
            "prompt": prompt,
            "max_tokens": 200
        })

def test_model(client, model):
    try:
        response = client.invoke_model(
            modelId=model["id"],
            body=format_input(model, PROMPT),
            contentType="application/json",
            accept="application/json"
        )
        response["body"].read().decode("utf-8")  # just confirm it's readable
        print(f"✅ {model['name']} passed")
        return "pass"
    except ClientError as e:
        error_message = e.response['Error'].get('Message', '')
        if "AccessDeniedException" in str(e) or "don't have access" in error_message:
            print(f"⚠️ SKIPPED (no access): {model['name']}")
            return "access"
        print(f"❌ FAIL (config): {model['name']} — {error_message}")
        return "fail"
    except Exception as e:
        print(f"❌ ERROR: {model['name']} — {e}")
        return "fail"

def run_validation():
    print("🔍 Running full model validation...")

    client = get_bedrock_client()
    passed_models = []
    skipped_models = []

    for model in LLM_MODELS:
        result = test_model(client, model)
        if result == "pass":
            passed_models.append(model)
        elif result == "access":
            skipped_models.append(model)
        elif result == "fail":
            print(f"\n🛑 Stopping on failure: {model['name']}")
            break

    # Save validated models
    with open(OUTPUT_VALID, "w") as f:
        f.write("LLM_MODELS = [\n")
        for model in passed_models:
            f.write(f"    {json.dumps(model)},\n")
        f.write("]\n")
    print(f"\n✅ Saved working models to {OUTPUT_VALID}")

    # Save skipped access-denied list
    with open(OUTPUT_SKIPPED, "w") as f:
        json.dump(skipped_models, f, indent=2)
    print(f"⚠️ Skipped models saved to {OUTPUT_SKIPPED}")

if __name__ == "__main__":
    run_validation()