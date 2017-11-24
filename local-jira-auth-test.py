# -*- coding: UTF-8 -*-
import requests
import json

'''
第一种认证方式，通过post方式，将用户名密码带在请求中，获得JSESSIONID,这是一个JIRA判断登录的一个标志。
第一次请求成功后，获得这个id，在之后的一段时间内，JIRA通过判断JSESSIONID时候存在和准确判断用户是否登录。
第一次的获得JSESSIONID可以存放在Redis等数据库中，以后请求可以使用。
登录状态多久失效根据搭建JIRA自行设置。可以瞧瞧自己的项目结构中的$JIRA_INSTALL/atlassian-jira/WEB-INF/web.xml
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
