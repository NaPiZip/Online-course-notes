import os
import json
from subprocess import check_output

# import requests


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LIB_DIR = os.path.join(SCRIPT_DIR, 'lib')

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """


    image_file_path = 'example.png'
    language = 'deu'
    
    command = 'LD_LIBRARY_PATH={} TESSDATA_PREFIX={} ./tesseract {} stdout -l {}'.format(
            LIB_DIR,
            SCRIPT_DIR+'/tessdata',
            image_file_path,
            language
        )

    

    try: 
        output = check_output(command, shell=True) 
        result = str(output,'utf-8')

    except :
        result = "Failed executing: {}".format(command)
        pass

    print("\n",result)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": result
        }),
    }
