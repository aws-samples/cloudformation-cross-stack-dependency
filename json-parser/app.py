import json
from crhelper import CfnResource

helper = CfnResource()

@helper.create
def resolve(event, _):
    dictionary = json.loads(event['ResourceProperties']['String'])

    helper.Data.update(dictionary)

def handler(event, context):
    print(event)

    helper(event, context)
