import json
def returnData(code,msg,*kwargs):
    print(*kwargs)
    returndata={
        "code":code,
        "msg":msg,
        "data":kwargs
    }
    return  json.dumps(returndata)