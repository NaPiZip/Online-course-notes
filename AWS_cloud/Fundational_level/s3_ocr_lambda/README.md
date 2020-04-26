<img src="https://blog.scottlogic.com/dsmith/assets/featured/aws-logo.png" alt="AWS logo" height="42px" width="84px" align="left"><br>

# Small project: S3 image OCR parser with AWS Lambda
<div>
    <a href="https://github.com/NaPiZip/Tipps-and-tricks">
        <img src="https://img.shields.io/badge/Document%20Version-0.0.1-brightgreen"/>
    </a>  
</div>

# Introduction
In this project I would like to improve my skills in and knowledge about the `AWS Lambda` service. I would like to trigger a Lambda function based on an image file upload into a S3 bucket. After the upload, the invoked Lambda function should extract the text out of the image using a generic optical character recognition (OCR) library in Python. A pretty similar example can be found [here](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-example-s3.html).

@TODO Adding a architecture image

The plan is to use `python 3.8` as well es the following libs:
- py-tesseract
- PIL


## The Toolchain
I am using `SAM` and `localstack` for development, they can both be executed locally, this comes in handy for development, so you don't have to actually use the paid AWS service.

<p align="center">
<img src="https://image.slidesharecdn.com/09112017-serverless-local-test-92e8f092-7d1c-43e4-809c-a40335e29637-2097706900-170913194001/95/local-testing-and-deployment-best-practices-for-serverless-applications-aws-online-tech-talks-19-638.jpg?cb=1505331628" alt="SAM example"/></p>

"The AWS Serverless Application Model (SAM) is an open-source framework for building serverless applications. It provides shorthand syntax to express functions, APIs, databases, and event source mappings. With just a few lines of configuration, you can define the application you want and model it." see [here](https://github.com/awslabs/aws-sam-cli).

I use `localstack` for testing purposes. `localstack` is a nice tool for running AWS services locally, see [link](https://localstack.cloud/).

<p align="center">
<img src="https://localstack.cloud/images/diagram.png" alt="localstack example"/></p>

## Prerequisite
In order to use `tesseract` in labmda there is a little bit of work needed, since the `py-tesseract` library is only a wrapper, I need to provide the binary to the lambda function as well. This means I need to build `tesseract` on the target. The aws documentation [link](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html), provides the following information in a python 3.8 environment:

| Name | Identifier | AWS SDK for Python | Operating System |
| Python 3.8 | python3.8 |boto3-1.12.22 botocore-1.15.22 | Amazon Linux 2 |
	
In order to build everything I am folowing this stackoverflow [post](https://stackoverflow.com/questions/33588262/tesseract-ocr-on-aws-lambda-via-virtualenv).

**Notes**
I after building `leptonica` you need to make sure the linker is able to find the library files, after `make install`. It just copied the `pkgconfig` file:

```
$ cd /usr/lib64/pkgconf
$ sudo cp /usr/local/lib/pkgconfig/* .
```


## Getting it done
The exercise contains of the following tasks:
1. Trigger lambda on file upload in S3.
 `sam local invoke --event SampleEvent.json` [here](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-example-s3.html#serverless-example-s3-test-locally).
2. Lambda display file information e.g. file name and type, but using a local s3 endpoint.
```python
  s3 = boto3.resource('s3', endpoint_url = 'http://192.168.99.100:4572',
                            aws_access_key_id     = 'AccessKey',
                            aws_secret_access_key = 'SecertKey')

  bucket = s3.Bucket('my-bucket')

  def lambda_handler(event, context):
    for obj in bucket.objects.all():
          print(obj.key)
          # display content
          print(obj.get()['Body'].read().decode(encoding="utf-8",errors="ignore"))
```
3. Lambda download file locally file.
4. Lambda perform operation on file.
5. Lambda save operation result in special S3 location.

**Notes**
I realized that for some reason on WSL the paths within docker container do not work so you need to make sure that you run the following commands in order to mount properly, [link](https://github.com/awslabs/aws-sam-cli/issues/336):

```
$ sudo mkdir /c
$ sudo mount --bind /mnt/c /c
$ cd /c/path/to/project
```

## Contributing
To get started with contributing to my GitHub repository, please contact me [Slack](https://join.slack.com/t/napi-friends/shared_invite/enQtNDg3OTg5NDc1NzUxLWU1MWNhNmY3ZTVmY2FkMDM1ODg1MWNlMDIyYTk1OTg4OThhYzgyNDc3ZmE5NzM1ZTM2ZDQwZGI0ZjU2M2JlNDU).
