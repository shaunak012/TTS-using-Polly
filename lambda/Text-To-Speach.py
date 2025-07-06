import boto3
import json
import uuid

def lambda_handler(event, context):
    try:
        if 'body' in event:
            data = json.loads(event['body'])
        else:
            data = event 
        
        text = data['text']

        polly_client = boto3.client('polly')
        s3_client = boto3.client('s3')
        bucket_name = 'Bucket name'

        response = polly_client.synthesize_speech(
            Text=text,
            OutputFormat='mp3',
            VoiceId='Joanna'
        )

        audio_stream = response['AudioStream'].read()
        filename = f"audio_{uuid.uuid4()}.mp3"

        # Upload to S3
        s3_client.put_object(Bucket=bucket_name, Key=filename, Body=audio_stream, ContentType='audio/mpeg')

        # Pre-signed URL valid for 5 mins
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

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
