# -*- coding: UTF-8 -*-
import requests
import json
from requests.auth import HTTPBasicAuth

# 最简单的用户名密码认证方式
url1 = 'http://127.0.0.1.:8080/rest/auth/1/session'
param1 = {'username': 'jira', 'password': 'github_jira'}

# base64认证方式
sub_url1 = 'http://127.0.0.1:8080/rest/api/2/issue/createmeta'
header1 = {'content-type': 'application/json',
           'Authorization': 'Basic amlyYTpnaXRodWJfamlyYQ=='}  # base64.b64encode(b'jira:github_jira')

get_consum_fieldid_url = 'http://127.0.0.1:8080/rest/api/2/field'  # 获得自定义字段id，调用创建issue-api时需要用到

url_create_issue = 'http://127.0.01:8080/rest/api/2/issue/'  # 创建issue-api

'''
customfield_xxxxx,由Jira自动生成，对应某个创建的自定义字段，如客户联系方式等
'''
param2 = {
    "fields": {
        "project":
            {
                "key": "JIRA"  # 创建项目,项目的Key值
            },
        "summary": "create jira issue",  # title
        "description": "创建一个JIRA问题",
        "issuetype": {
            "name": "缺陷"
        },
        "customfield_10000": "GITHUB",  #
        "customfield_10001": "PYTHON-JIRA-CODE",  #
        'customfield_10002': "JIRA-GITHUB",
        "customfield_10003": "customfield_10003",  # test jira
    }
}
header2 = {'content-type': 'application/json', 'Authorization': 'Basic amlyYTpnaXRodWJfamlyYQ==',  # admin:aispeech
           'Accept': 'application/json'}

header3 = {'content-type': 'application/json',
           'cookie': 'JSESSIONID=3A0FBC1A4FDB0D85348F8FE3C7BF8F49',
           'Accept': 'application/json'}

search_url = 'http://127.0.0.1:8080/rest/api/2/issue/TECH-6'

res = requests.get(url=get_consum_fieldid_url, headers=header2)  # 获得该项目下所有字段等信息，json格式
print res.status_code
print res.url
print res.text
print res.headers

# 创建issue，将获得的JSESSIONID放到请求头的cookie
# res = requests.session()
# res = requests.post(url=url_create_issue, headers=header3, data=json.dumps(param2))
