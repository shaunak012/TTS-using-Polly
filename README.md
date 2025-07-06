# 🗣️ Text-to-Speech API using AWS Lambda, Polly, and S3

This project converts input text to speech using Amazon Polly and securely returns a pre-signed URL to the generated MP3 audio.

## 🚀 Tech Stack

- **AWS Lambda** – Serverless compute
- **Amazon Polly** – Neural text-to-speech engine
- **Amazon S3** – Private audio storage
- **API Gateway (REST)** – Secured public endpoint
- **API Key** – Restricts access to only approved clients

## 🧠 How It Works

1. You send a POST request to the API with some text
2. Lambda triggers Polly to convert it into speech
3. The resulting MP3 file is uploaded to S3
4. A secure, short-lived **pre-signed URL** is returned
5. You can click the URL to hear the voice output 🎧

## 🔐 API Security

- The API is secured using an **API Key**
- Only requests with the correct `x-api-key` header are allowed
- Audio files in S3 remain private, accessed only via pre-signed URLs

## 📬 Example Request

**POST** `/generate-audio`

```http
Headers:
  Content-Type: application/json.
  x-api-key: YOUR_API_KEY

Body:
  {
    "text": "Hello world!"
  }

Response:
  {
    "audioUrl": "https://your-bucket.s3.amazonaws.com/audio_xyz123.mp3?AWSAccessKeyId=..."
  }
```


## 📺 Demo Video (Coming Soon)

A video walkthrough of the project, live API calls, and how the secure pre-signed URLs work will be available on [LinkedIn](https://www.linkedin.com/in/shaunak-shukla/).

---

## 📜 License

This project is open-source and intended for educational and personal portfolio use.

---

## ✨ Author

**Shaunak Shukla**  
[LinkedIn](https://www.linkedin.com/in/your-profile)

