import time
import os

def handler(event, context):
    message = 'Hello {} {}!'.format(event['first_name'], event['last_name']) 

    print("Lambda function ARN:", context.invoked_function_arn)
    print("CloudWatch log stream name:", context.log_stream_name)
    print("CloudWatch log group name:",  context.log_group_name)
    print("Lambda Request ID:", context.aws_request_id)
    print("Lambda function memory limits in MB:", context.memory_limit_in_mb)
    time.sleep(1) 

    print("Lambda time remaining in MS:", context.get_remaining_time_in_millis())

    return { 
        'message' : message,
        'context' : str(context),
        'pwd': os.getcwd(),
        'status': 'done',
        'data': {
            'run_id': '1111'
        }
    }