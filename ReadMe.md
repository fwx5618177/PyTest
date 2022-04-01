# serverless初探-awa lambda初次接触

- `serverless`为未来的发展方向之一，主要面对的是`SAAS`
- 国内资料大都是摘抄自外网资料的只言片语，内容极其糟糕

# 1. 配置
- 安装`docker`
- 写`dockerfile`安装`aws lambda`

```dockerfile
FROM public.ecr.aws/lambda/python:3.8

# Copy function code and package.json
COPY app.py   ./

# Set the CMD to your handler
CMD ["app.handler"]
```

```python
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
```

1. 初始化项目
2. 生成`docker`映像`docker build -t hello-world .`
3. 运行测试`docker run -p 9000:8080 hello-world:latest`
   1. 此命令将映像作为容器运行，并在 localhost:9000/2015-03-31/functions/function/invocations 以本地方式启动终端节点
4. 测试: `curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"first_name": "test","last_name": "test"}'`

# 2. 返回结果
- event: 参数
- context:
```json
{
    "statusCode":200,
    "body":"\"Hello from Lambda!\"",
    "event":{},
    "context":{
        "callbackWaitsForEmptyEventLoop":true,
        "functionVersion":"$LATEST",
        "functionName":"test_function",
        "memoryLimitInMB":"3008",
        "logGroupName":"/aws/lambda/Functions",
        "logStreamName":"$LATEST",
        "invokedFunctionArn":"arn:aws:lambda:us-east-1:012345678912:function:test_function",
        "awsRequestId":"f05bac9a-10ed-488a-a138-e192fec03081"
    }
} 
```

# 3. `Pytest`测试
## 1. `pytest.ini`配置
```ini
[pytest]
addopts = -vs
testpaths = ./
python_files = test_*.py
```

# 使用介绍

## 1.安装
- `pip install -r requirements.txt`
- 阅读`dockerConnect`，下载`docker`

## 2. 配置-[pytest.ini]
- addopts:附加

## 3. 使用
- `pytest`

```txt
requests
pytest
pytest-html
pytest-xdist
pytest-ordering
pytest-rerunfailures
allure-pytest
itunesiap
```
- pytest.py
```py
import pytest
import requests
import json

url = 'http://localhost:9000'
queryApi = '/2015-03-31/functions/function/invocations'
deleteApi = '/2015-03-31/functions/function/invocations'
headers = {
    'content-type': 'application/json'
}
payload = {
    "first_name": "John",
    "last_name": "Smith"
}

stopStatus = 'done'

def queryRunId():
    res = requests.post(url + queryApi, data = json.dumps(payload), headers = headers)
    dataSet = res.json()
    # 获取指定的json data
    run_id = dataSet['data']['run_id']
    return run_id

def deleteRunId(run_id):
    run_id = queryRunId()
    res = requests.post(url + deleteApi, data = json.dumps(payload), headers = headers)
    dataSet = res.json()
    # 获取停止后的状态
    fail_status = dataSet['status']
    return fail_status

def testDeleteRunId():
    res = queryRunId()
    result = deleteRunId(res)
    assert(result == stopStatus)    
    
if __name__ == "__main__":
    pytest.main(['./test_print.py'])
```

