# -*- coding: UTF-8 -*-
import requests
import json

'''
第一种认证方式
'''

url_sessionid = 'http://127.0.0.1:8080/rest/auth/1/session'

param = {
    "username": "jira",
    "password": "github_jira"
}

header = {'content-type': "application/json"}

res_sessionid = requests.post(url=url_sessionid, data=json.dumps(param), headers=header)


print res_sessionid.status_code
print res_sessionid.url
print res_sessionid.text
print res_sessionid.headers
