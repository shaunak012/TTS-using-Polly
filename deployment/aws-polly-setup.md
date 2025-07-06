# 🎙️ Amazon Polly Setup Guide

This document explains how to set up Amazon Polly for the Text-to-Speech (TTS) API project.

---

## 📌 Prerequisites

- AWS account with permissions to access Amazon Polly
- An S3 bucket created for storing audio files (e.g., `shaunak-tts-audio-bucket`)

---

## 📄 Create the S3 Bucket

1. Go to **AWS S3 Console**
2. Click **Create bucket**
3. Name your bucket (e.g., `shaunak-tts-audio-bucket`)
4. Leave all defaults for private access
5. Create bucket

---

## 📄 Grant IAM Role Permissions

Ensure the Lambda execution role has:
- `AmazonPollyFullAccess`
- `AmazonS3FullAccess` (for development only — restrict to your bucket in production)

---

## 📄 Test Amazon Polly via CLI (Optional)

Test Polly speech synthesis via AWS CLI:

```bash
aws polly synthesize-speech \
    --output-format mp3 \
    --voice-id Joanna \
    --text "Hello, this is a test." \
    output.mp3
```

This confirms Polly is active on your account.

---

## 📄 Integrating Polly with Lambda

Your Lambda function uses the `boto3` SDK to interact with Amazon Polly:

```python
polly_client = boto3.client('polly')
response = polly_client.synthesize_speech(
    Text=text,
    OutputFormat='mp3',
    VoiceId='Joanna'
)
```

---

## 📌 Notes

- Amazon Polly charges per character outside the AWS Free Tier.
- For voice options, refer to: https://docs.aws.amazon.com/polly/latest/dg/voicelist.html
- Use **SSML markup** for controlling pitch, speed, and volume.
