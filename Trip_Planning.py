import boto3
import json

# Prompt data
prompt_data = "I am going to Paris, what should I see?"

# Initialize the Bedrock client
bedrock = boto3.client(service_name="bedrock-runtime")

# Payload for the request
payload = {
    "prompt": "<s>[INST]" + prompt_data + "[/INST]",
    "max_tokens": 800,
    "temperature": 0.7,
    "top_p": 0.7,
    "top_k": 50
}

# Convert payload to JSON string
body = json.dumps(payload)

# Model ID
model_id = "mistral.mixtral-8x7b-instruct-v0:1"

# Invoke the model
response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

# Parse the response body
response_body = json.loads(response['body'].read().decode('utf-8'))

# Print the entire response body to understand its structure
print("Response Body:", json.dumps(response_body, indent=2))

