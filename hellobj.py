#!/usr/bin/env python
import boto3


def detect_labels(bucket, image):
    print(f"This is the bucket {bucket}, and this is the image {image}")
    rekognition = boto3.client("rekognition")
    response = rekognition.detect_text(
        Image={
            "S3Object": {
                "Bucket": bucket,
                "Name": image,
            }
        },
    )
    return response


result = detect_labels("cvdemosept", "license-ca.jpeg")
print(result)
