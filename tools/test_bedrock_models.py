import boto3
import json
import os
from botocore.exceptions import BotoCoreError, ClientError

REGION = "us-east-1"

# Define which models use the Messages API
MESSAGES_API_MODELS = [
    "anthropic.claude-3-sonnet-20240229-v1:0",
    "anthropic.claude-3-haiku-20240307-v1:0",
    "anthropic.claude-3-opus-20240229-v1:0"
]

# Define model test config
MODELS_TO_TEST = [
    {
        "model_id": "anthropic.claude-3-sonnet-20240229-v1:0",
        "name": "Claude 3 Sonnet",
        "prompt": "Explain the benefits of AI in plain language."
    },
    # Add more models here as needed
]

def get_bedrock_client():
    try:
        return boto3.client("bedrock-runtime", region_name=REGION)
    except Exception as e:
        print("❌ Could not create Bedrock client:", str(e))
        return None

def uses_messages_api(model_id):
    return model_id in MESSAGES_API_MODELS

def format_body(model_id, prompt):
    if uses_messages_api(model_id):
        return json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "messages": [
                { "role": "user", "content": prompt }
            ],
            "max_tokens": 300
        })
    else:
        return json.dumps({
            "prompt": f"\n\nHuman: {prompt}\n\nAssistant:",
            "max_tokens_to_sample": 200
        })
        
def test_model(client, model_config):
    print(f"\n🔍 Testing: {model_config['name']} ({model_config['model_id']})")

    try:
        body = format_body(model_config['model_id'], model_config['prompt'])
        response = client.invoke_model(
            modelId=model_config['model_id'],
            body=body,
            contentType="application/json",
            accept="application/json"
        )
        result = response['body'].read().decode('utf-8')
        print("✅ Success! Output:\n", result[:500], "\n")
    except ClientError as e:
        print("❌ Client error:", e.response['Error'].get('Message', str(e)))
    except BotoCoreError as e:
        print("❌ BotoCore error:", str(e))
    except Exception as e:
        print("❌ Unexpected error:", str(e))

if __name__ == "__main__":
    print("🔧 Starting Bedrock model test...")

    if "AWS_ACCESS_KEY_ID" not in os.environ:
        print("⚠️  AWS credentials not found. Run `saml2aws login` first.")
        exit(1)

    client = get_bedrock_client()
    if client is None:
        print("❌ Unable to continue without Bedrock client.")
        exit(1)

    for model in MODELS_TO_TEST:
        test_model(client, model)

    print("✅ All tests complete.")