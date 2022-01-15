import os
from dotenv import load_dotenv

import boto3 as b3

# WIP
# Application to snip image from screen
# Random image name using datetime
# Application displays text to be copied


# return image file name
def upload_image(bucket, imageName):

    folder = './crops/'
    fileExt = '.png'

    folderExist = os.path.exists(folder)
    
    if not folderExist:
        os.makedirs(folder)

    imgDir = folder + imageName + fileExt 
    imgFile = imageName + fileExt 

    s3 = b3.resource('s3')

    s3.Bucket(bucket).upload_file(imgDir, imgFile)

    print('Uploaded', imgFile, 'to', bucket, 'bucket.\n')

    return imgFile

# WIP - return detectedTexts to be displayed on Application
def detect_text(bucket, photo):

    client = b3.client('rekognition')

    response = client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})

    textDetections = response['TextDetections']

    for text in textDetections:
        print('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%", end = "\t")
        print('Text: ' + text['DetectedText'])


def main():
    
    load_dotenv()

    bucket = os.getenv('BUCKET')

    # change later
    photoName = '833344' 

    file = upload_image(bucket, photoName)

    detect_text(bucket, file)

if __name__ == "__main__":
    main()

