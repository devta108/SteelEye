"""
This module uploads file to s3
"""
import logging
import boto3
import os


def upload_file(file_name=None, bucket=None, object_name=None):
    """Upload a file to an S3 bucket
    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    s3 = boto3.resource(
        service_name='s3',
        region_name='us-east-1',
        aws_access_key_id=os.getenv('aws_access_key_id'),
        aws_secret_access_key=os.getenv('aws_secret_access_key')
    )
    logging.info('Started Uploading File to S3 Bucket')
    s3.Bucket(bucket).upload_file(file_name, object_name)
    logging.info('File Uploaded Successfully on S3')
