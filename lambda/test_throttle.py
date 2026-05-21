import boto3
import threading
import json
from botocore.exceptions import ClientError

# 1. Region check karein (Nova aksar us-east-1 ya us-west-2 mein hota hai)
client = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')

def call_bedrock(id):
    # Amazon Nova ka Model ID (Micro fast test ke liye best hai)
    model_id = "amazon.nova-micro-v1:0" 
    
    # Nova ka body format
    body = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": [{"text": "hi"}]
            }
        ],
        "inferenceConfig": {"max_new_tokens": 10}
    })

    try:
        response = client.invoke_model(
            modelId=model_id,
            body=body
        )
        print(f"Request {id}: Success ✅")
    except ClientError as e:
        code = e.response['Error']['Code']
        print(f"Request {id}: FAILED ❌ - Error Code: {code}")

# 30 requests ka load
threads = []
print("Starting Load Test with Amazon Nova...")
for i in range(150):
    t = threading.Thread(target=call_bedrock, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
print("Test Completed.")