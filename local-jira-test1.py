# -*- coding: UTF-8 -*-
import requests
import json
from requests.auth import HTTPBasicAuth

'''
使用第一种认证方式
'''

url1 = 'http://127.0.0.1.:8080/rest/auth/1/session'
param1 = {'username': 'jira', 'password': 'github_jira'}

sub_url1 = 'http://127.0.0.1:8080/rest/api/2/issue/createmeta'
header1 = {'content-type': 'application/json', 'Authorization': 'Basic amlyYTphaXNwZWVjaA=='}  # Authorization:base64编码

get_consum_fieldid_url = 'http://127.0.0.1:8080/rest/api/2/field'

url_create_issue = 'http://127.0.01:8080/rest/api/2/issue/'

param2 = {
    "fields": {
        "project":
            {
                "key": "JIRA"  # 创建项目,项目的Key值
            },
        "summary": "create jira issue",  # title
        "description": "创建一个JIRA问题",
        "customfield_10003": "customfield_10003",  # jest jira
        "issuetype": {
            "name": "缺陷"
        },
        "customfield_10000": "GITHUB",  #
        "customfield_10002": "PYTHON-JIRA-CODE",  #
        'customfield_10001': "JIRA-GITHUB",
    }
}
header2 = {'content-type': 'application/json', 'Authorization': 'Basic YWRtaW46YWlzcGVlY2g=',  # admin:aispeech
           'Accept': 'application/json'}

header3 = {'content-type': 'application/json',
           'cookie': 'JSESSIONID=3A0FBC1A4FDB0D85348F8FE3C7BF8F49',
           'Accept': 'application/json'}

search_url = 'http://127.0.0.1:8080/rest/api/2/issue/TECH-6'

# res = requests.session()
# res = requests.post(url=url_create_issue, headers=header3, data=json.dumps(param2))

res = requests.get(url=get_consum_fieldid_url, headers=header2)  # 获得该项目下所有字段等信息，json格式
print res.status_code
print res.url
print res.text
print res.headers
