#rather than retesting every model every time, once it passes we move on to the next one
import boto3
import json
import os
import time
from botocore.exceptions import BotoCoreError, ClientError
from bedrock_models_supported import LLM_MODELS

REGION = "us-east-1"
CHECKPOINT_FILE = "progress_checkpoint.json"
STEP = 2

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
            "prompt": prompt,
            "max_tokens": 200,
            "temperature": 0.7
        })
    else:  # generic fallback (Meta, Mistral, etc.)
        return json.dumps({
            "prompt": prompt,
            "max_tokens": 200
        })

def test_model(client, model, prompt="What is the future of AI?"):
    print(f"\n🔍 Testing: {model['name']} ({model['id']})")
    try:
        response = client.invoke_model(
            modelId=model['id'],
            body=format_input(model, prompt),
            contentType="application/json",
            accept="application/json"
        )
        output = response["body"].read().decode("utf-8")
        print("✅ PASS\n")
        return True
    except (ClientError, BotoCoreError) as e:
        print(f"❌ FAIL: {e}\n")
        return False
    except Exception as e:
        print(f"❌ ERROR: {e}\n")
        return False

def load_checkpoint():
    if os.path.exists(CHECKPOINT_FILE):
        with open(CHECKPOINT_FILE, "r") as f:
            return json.load(f).get("last_success_index", 0)
    return 0

def save_checkpoint(index):
    with open(CHECKPOINT_FILE, "w") as f:
        json.dump({ "last_success_index": index }, f)

def progressive_resume_test():
    print("🔧 Starting Incremental Bedrock Model Test...\n")

    if "AWS_ACCESS_KEY_ID" not in os.environ:
        print("⚠️  AWS credentials not found. Run `saml2aws login` first.")
        return

    client = get_bedrock_client()
    total = len(LLM_MODELS)
    start_index = load_checkpoint()

    print(f"🔁 Resuming from model #{start_index}\n")

    for i in range(start_index, total, STEP):
        batch = LLM_MODELS[i:i+STEP]
        print(f"\n🧪 Testing models {i}–{i+len(batch)-1}: {[m['name'] for m in batch]}")

        all_passed = True
        for model in batch:
            if not test_model(client, model):
                print(f"🛑 Stopped due to failure at model #{i}: {model['name']}")
                return

        save_checkpoint(i + STEP)
        print(f"✅ Batch passed! Progress saved at index {i + STEP}")
        time.sleep(1)

    print("🎉 All models validated successfully!")

if __name__ == "__main__":
    progressive_resume_test()