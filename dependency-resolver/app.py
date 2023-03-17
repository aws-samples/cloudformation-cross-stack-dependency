import json, boto3, os, requests
from crhelper import CfnResource

ssm = boto3.client('ssm')
helper = CfnResource()

DEPENDENCY_ID=os.environ["DEPENDENCY_ID"]
SUBNET_ID=os.environ["SUBNET_ID"]

@helper.create
def resolve(*args):
    response = ssm.get_parameters_by_path(
        Path = f'/cf-deps/{DEPENDENCY_ID}',
        Recursive=True
    )

    for param in response['Parameters']:
        try:
            requests.put(
                url = param['Value'],
                json = {
                    'Status': 'SUCCESS',
                    'UniqueId': 'subnetId',
                    'Data': SUBNET_ID,
                }
            )
        except Exception:
            print(f'Error trying to signal to ${param["Name"]}' )
            pass


def handler(event, context):
    print(event)

    if (event.get("StackId")):
        print('Calling as a Cloudformation custom resource')
        helper(event, context)
    else:
        print('Calling as a EventBridge rule')
        resolve()
