import json
import requests
import os

def chat_with_healthai(question):
    api_key = "ABSx-wO3cXaqpNGBK_qsvx8IjPvg2em91oc36aOZDPIk"
    project_id = "71168a4b-b1c7-4bf9-b1c1-9eae5e7ba0f9"
    url = "https://us-south.ml.cloud.ibm.com"

    model_id = "ibm/granite-13b-instruct-v2"  # Ensure it's available in your region

    # Step 1: Get IAM Token
    iam_url = "https://iam.cloud.ibm.com/identity/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = f"apikey={api_key}&grant_type=urn:ibm:params:oauth:grant-type:apikey"

    response = requests.post(iam_url, data=data, headers=headers)
    if response.status_code != 200:
        return f"❌ Error getting IAM Token. Reason: {response}"

    iam_token = response.json()["access_token"]

    # Step 2: Prepare Generation Payload
    gen_url = f"{url}/ml/v1/text/generation?version=2024-05-01"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {iam_token}",
    }

    payload = {
        "model_id": model_id,
        "input": question,
        "parameters": {
            "decoding_method": "greedy",
            "max_new_tokens": 150
        },
        "project_id": project_id
    }

    gen_response = requests.post(gen_url, headers=headers, json=payload)

    if gen_response.status_code != 200:
        return f"❌ Error generating response: {gen_response.text}"

    return gen_response.json().get("results", [{}])[0].get("generated_text", "No response received.")
