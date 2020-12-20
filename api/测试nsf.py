import json

import requests

headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
data = {"query": "", "fieldCode": "", "supportType": "", "organizationID": "", "title": "", "authorID": "", "journalName": "", "projectName": "",
          "orderBy": "rel", "orderType": "desc", "year": "", "pageNum": 65100, "pageSize": 10}
resp = requests.post('http://ir.nsfc.gov.cn/baseQuery/data/paperQueryForOr', headers=headers, data=json.dumps(data))
jj = json.loads(resp.text)
for art in jj['data']:
    print(art)
