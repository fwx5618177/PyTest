# 介绍
- 用于线下测试`serverless`
- 同时使用`PytTest`进行测试

1. 初始化项目
2. 生成`docker`映像`docker build -t hello-world .`
3. 运行测试`docker run -p 9000:8080 hello-world:latest`
   1. 此命令将映像作为容器运行，并在 localhost:9000/2015-03-31/functions/function/invocations 以本地方式启动终端节点
4. 测试: `curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"first_name": "test","last_name": "test"}'`

# 返回结果
- event: 参数
- context:
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