import json
import os
import base64

import pytest

from hello_world import app


@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""

    return {
        "body": '{ "test": "body"}',
        "resource": "/{proxy+}",
        "requestContext": {
            "resourceId": "123456",
            "apiId": "1234567890",
            "resourcePath": "/{proxy+}",
            "httpMethod": "POST",
            "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
            "accountId": "123456789012",
            "identity": {
                "apiKey": "",
                "userArn": "",
                "cognitoAuthenticationType": "",
                "caller": "",
                "userAgent": "Custom User Agent String",
                "user": "",
                "cognitoIdentityPoolId": "",
                "cognitoIdentityId": "",
                "cognitoAuthenticationProvider": "",
                "sourceIp": "127.0.0.1",
                "accountId": "",
            },
            "stage": "prod",
        },
        "queryStringParameters": {"foo": "bar"},
        "headers": {
            "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
            "Accept-Language": "en-US,en;q=0.8",
            "CloudFront-Is-Desktop-Viewer": "true",
            "CloudFront-Is-SmartTV-Viewer": "false",
            "CloudFront-Is-Mobile-Viewer": "false",
            "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
            "CloudFront-Viewer-Country": "US",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Upgrade-Insecure-Requests": "1",
            "X-Forwarded-Port": "443",
            "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
            "X-Forwarded-Proto": "https",
            "X-Amz-Cf-Id": "aaaaaaaaaae3VYQb9jd-nvCd-de396Uhbp027Y2JvkCPNLmGJHqlaA==",
            "CloudFront-Is-Tablet-Viewer": "false",
            "Cache-Control": "max-age=0",
            "User-Agent": "Custom User Agent String",
            "CloudFront-Forwarded-Proto": "https",
            "Accept-Encoding": "gzip, deflate, sdch",
        },
        "pathParameters": {"proxy": "/examplepath"},
        "httpMethod": "GET",
        "stageVariables": {"baz": "qux"},
        "path": "/examplepath",
    }


def test_lambda_handler(apigw_event, mocker):
    app.check_output = mocker.MagicMock(return_value=b'G Tesseract OCR')

    ret = app.lambda_handler(apigw_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "result" in ret["body"]    
    assert("Tesseract" in data["result"])


def image_to_json_payload(image_file):
    _, full_file_name = os.path.split(image_file)
    file_name, extention = full_file_name.split('.')

    with open( image_file, 'rb') as f:
        data = base64.b64encode(f.read()) 
    
    with open('tests/unit/'+ file_name +'.json', 'w', encoding='utf-8') as json_file:
        json.dump({ 'name':         file_name,
                    'format':       extention,
                    'encoding':     'base64',
                    'payload':      data.decode('utf-8')}, json_file, indent=1)


def read_json_payload_file(json_file):
    json_file = "tests/unit/example.json"
    with open(json_file, 'rb') as fid:
        data = fid.read()
        content = json.loads(data)
    return content


def test_dev(apigw_event, mocker):
    image_to_json_payload("hello_world/example.png")
    json_data = read_json_payload_file("")

    image_file= "tests/unit/{}.{}".format(json_data['name'], json_data['format'])
    with open(image_file, 'wb') as fid:
        fid.write(base64.b64decode(str.encode(json_data['payload'])))
