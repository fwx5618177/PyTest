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
    "first_name": "wenxuan",
    "last_name": "feng"
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