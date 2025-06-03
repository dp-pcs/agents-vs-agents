import boto3
import json

client = boto3.client("bedrock", region_name="us-east-1")

def list_models():
    response = client.list_foundation_models()
    models = response.get("modelSummaries", [])
    print(f"🧠 You have access to {len(models)} models:\n")
    for m in models:
        print(f"- Name: {m['modelName']}")
        print(f"  ID:   {m['modelId']}")
        print(f"  Provider: {m['providerName']}")
        print(f"  Input Type: {m.get('inferenceTypesSupported')}")
        print("")

if __name__ == "__main__":
    list_models()