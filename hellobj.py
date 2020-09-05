#!/usr/bin/env python
import boto3
import click


def detect_labels(bucket, name):
    print(f"This is the bucket {bucket}, and this is the image {name}")
    rekognition = boto3.client("rekognition")
    response = rekognition.detect_text(
        Image={
            "S3Object": {
                "Bucket": bucket,
                "Name": name,
            }
        },
    )
    return response


@click.command()
@click.option(
    "--bucket",
    prompt="S3 Bucket",
    help="This is the S3 Bucket that contains your image",
)
@click.option(
    "--name",
    prompt='S3 image object name: i.e. husky.png"',
    help="This is the name of the image to be analyzed",
)
def cli(bucket, name):
    """This is a computer vision cli that extracts text from an image in S3
    To use the tool do the following:
    ./hellobject --bucket foo --name bar"""

    result = detect_labels(bucket, name)
    detect_text = result["TextDetections"]
    click.echo(
        click.style(f"Found Text for bucket: {bucket} and name {name} ", fg="red")
    )
    for detected in detect_text:
        if detected["Confidence"] > 0.99:
            text = detected["DetectedText"]
            click.echo(click.style(f"FOUND TEXT: {text}", bg="blue", fg="white"))


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    cli()
