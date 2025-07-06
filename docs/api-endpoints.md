# 📑 API Endpoints Documentation

## 🎙️ Text-to-Speech Audio Generation API

This API allows you to convert input text into speech using Amazon Polly via AWS Lambda. The generated audio is stored privately in S3, and a temporary pre-signed URL is returned for public download.

---

## 🔐 Authentication

**This API requires an API Key for access.**  
Requests without a valid API Key will receive a `403 Forbidden`.

**API Key Header**

| Key        | Value            |
|:------------|:----------------|
| `x-api-key` | `YOUR_API_KEY_HERE` |

---

## 📌 Endpoint

**Method:** `POST`  
**URL:** `https://your-api-id.execute-api.ap-south-1.amazonaws.com/production/generate-audio`

---

## 📄 Request Format

**Headers:**

| Key               | Value               |
|:------------------|:--------------------|
| `Content-Type`     | `application/json`    |
| `x-api-key`        | `YOUR_API_KEY_HERE` |

**Body (raw JSON):**

```json
{
  "text": "Hello World!"
}
```

---

## 📥 Response Format

**Success — `200 OK`**

```json
{
  "audioUrl": "https://shaunak-tts-audio-bucket.s3.ap-south-1.amazonaws.com/audio_xxx.mp3?X-Amz-Expires=300&X-Amz-Signature=..."
}
```

- `audioUrl` is a **temporary pre-signed URL** valid for **5 minutes (300 seconds)**.

**Error — `403 Forbidden`**  
If no valid API Key is provided.

---

## 🚀 Example

**Curl Command:**

```bash
curl -X POST "https://your-api-id.execute-api.ap-south-1.amazonaws.com/production/generate-audio" \
-H "Content-Type: application/json" \
-H "x-api-key: YOUR_API_KEY_HERE" \
-d '{ "text": "Hello world!" }'
```

---

## 📌 Notes
- Audio files are stored privately in S3.
- Pre-signed URLs allow public download for a limited time.
- API is secured via API Key enforced by an API Gateway Usage Plan.

---

## 📞 Contact

Built by **Shaunak Shukla**  
For queries or collaboration: [LinkedIn](https://www.linkedin.com/in/shaunak-shukla/)


