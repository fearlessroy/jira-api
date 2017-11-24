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

# url_use_sessionid = 'http://172.16.10.176:8080/rest/api/2/issue/TECH-6'
# header1 = {
#     "content-type": 'application/json',
#     'cookie': 'JSESSIONID=6B43D4B4FCA9C257C1ED628B7F5895C2',
#     "Accept": "application/json"
# }
# res_use_sessionid = requests.get(url=url_use_sessionid, headers=header1)
#
# print res_use_sessionid.status_code
# print res_use_sessionid.url
# print res_use_sessionid.text
# print res_use_sessionid.headers
