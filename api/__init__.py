'''
api负责管理所有的后端代码
'''

def ok(data={}):
    return {'status':200, 'msg':'', 'data':data}

def fail(msg='', data={}):
    return {'status': 400, 'msg': msg, 'data': data}
