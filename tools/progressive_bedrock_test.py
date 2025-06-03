import boto3
import json
import os
import time
from botocore.exceptions import BotoCoreError, ClientError
from bedrock_models_supported import LLM_MODELS

REGION = "us-east-1"

def get_bedrock_client():
    return boto3.client("bedrock-runtime", region_name=REGION)

def format_input(model, prompt):
    if model["api_type"] == "messages":
        return json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "messages": [{ "role": "user", "content": prompt }],
            "max_tokens": 300
        })
    elif model["api_type"] == "completion":
        return json.dumps({
            "prompt": f"{prompt}",
            "max_tokens": 200
        })
    else:
        raise ValueError(f"Unsupported API type: {model['api_type']}")

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

def progressive_test():
    print("🔧 Starting Progressive Bedrock Model Test...\n")
    
    if "AWS_ACCESS_KEY_ID" not in os.environ:
        print("⚠️  AWS credentials not found. Run `saml2aws login` first.")
        return

    client = get_bedrock_client()
    total = len(LLM_MODELS)
    step = 2

    for i in range(step, total + 1, step):
        current_batch = LLM_MODELS[:i]
        print(f"\n🧪 Testing {len(current_batch)} model(s): {[m['name'] for m in current_batch]}")
        
        all_passed = True
        for model in current_batch:
            if not test_model(client, model):
                all_passed = False
                break
        
        if not all_passed:
            print(f"🛑 Stopped at {len(current_batch)} models due to failure.")
            return
        else:
            print(f"✅ All {len(current_batch)} models passed!\n")
            time.sleep(2)  # Small delay between batches

    print("🎉 All models validated successfully!")

if __name__ == "__main__":
    progressive_test()