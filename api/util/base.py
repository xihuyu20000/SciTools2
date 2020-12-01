def ok(data={}):
    return {'status':200, 'msg':'', 'data':data}

def fail(msg='', data={}):
    return {'status': 400, 'msg': msg, 'data': data}