# 📦 Lambda Function Setup Guide

This document outlines how to set up the AWS Lambda function used for the Text-to-Speech (TTS) API.

---

## 📌 Prerequisites

- AWS account with appropriate permissions.
- An IAM Role for Lambda with:
  - `AmazonPollyFullAccess`
  - `AmazonS3FullAccess` (or restricted access to your target bucket)

---

## 📄 Lambda Function Creation

1. **Go to AWS Lambda Console**
2. Click **Create function**
3. Choose:
   - **Author from scratch**
   - Function name: `textToSpeechLambda`
   - Runtime: `Python 3.12`
4. Click **Create function**

---

## 📄 Add Permissions

1. In your Lambda console, go to **Configuration → Permissions**
2. Click on the **Execution role**
3. Attach these policies:
   - `AmazonPollyFullAccess`
   - `AmazonS3FullAccess`

---

## 📄 Lambda Function Code

Use the following Python code:

```python
import boto3
import json
import uuid

def lambda_handler(event, context):
    data = json.loads(event['body'])
    text = data['text']

    polly_client = boto3.client('polly')
    s3_client = boto3.client('s3')
    bucket_name = 'your-bucket'

    response = polly_client.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId='Joanna'
    )

    audio_stream = response['AudioStream'].read()
    filename = f"audio_{uuid.uuid4()}.mp3"

    s3_client.put_object(Bucket=bucket_name, Key=filename, Body=audio_stream, ContentType='audio/mpeg')

    presigned_url = s3_client.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket_name, 'Key': filename},
        ExpiresIn=300
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'audioUrl': presigned_url}),
        'headers': {'Content-Type': 'application/json'}
    }
```

---

## 📄 Test Lambda

Create a test event:

```json
{
  "body": "{\"text\": \"Hello, this is a test audio.\"}"
}
```

Deploy and test to ensure successful audio generation and S3 upload.
