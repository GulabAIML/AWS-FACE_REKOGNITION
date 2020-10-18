import boto3

if __name__ == "__main__":

    
    fileName = 'Horse.jpg'
    bucket = 'ai-on-cloud'

    client = boto3.client('rekognition', region_name='us-west-1',aws_access_key_id = 'XXXXX',
    aws_secret_access_key = 'XXXXXX')

    response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':fileName}})

    print('Detected Labels for ' + fileName)
    for label in response['Labels']:
        print(label['Name'] + ':' + str(label['Confidence']))