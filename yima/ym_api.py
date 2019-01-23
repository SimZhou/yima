# -*- coding: utf-8 -*-
# python3.5

# 易码短信服务平台开放接口范例代码
# 语言版本：python版
# 官方网址：www.51ym.me
# 技术支持QQ：2114927217
# 发布时间：217-12-11

from urllib import parse, request
import time
import re

header_dict = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}

# 登陆/获取TOKEN
username = ''  # 账号
password = ''  # 密码
url =  'http://api.fxhyd.cn/UserInterface.aspx?action=login&username=' + \
    username+'&password='+password
TOKEN1 = request.urlopen(request.Request(
    url=url, headers=header_dict)).read().decode(encoding='utf-8')
if TOKEN1.split('|')[0] == 'success':
    TOKEN = TOKEN1.split('|')[1]
    print('TOKEN是'+TOKEN)
else:
    print('获取TOKEN错误,错误代码'+TOKEN1+'。代码释义：1001:参数token不能为空;1002:参数action不能为空;1003:参数action错误;1004:token失效;1005:用户名或密码错误;1006:用户名不能为空;1007:密码不能为空;1008:账户余额不足;1009:账户被禁用;1010:参数错误;1011:账户待审核;1012:登录数达到上限')


TOKEN = ''  # 输入TOKEN
# 获取账户信息
url = 'http://api.fxhyd.cn/UserInterface.aspx?action=getaccountinfo&token='+TOKEN+'&format=1'
ACCOUNT1 = request.urlopen(request.Request(
    url=url, headers=header_dict)).read().decode(encoding='utf-8')
if ACCOUNT1.split('|')[0] == 'success':
    ACCOUNT = ACCOUNT1.split('|')[1]
    print(ACCOUNT)
else:
    print('获取TOKEN错误,错误代码'+ACCOUNT1)

# 获取手机号码
ITEMID = '27474'  # 项目编号
EXCLUDENO = ''  # 排除号段170_171
url = 'http://api.fxhyd.cn/UserInterface.aspx?action=getmobile&token=' + \
    TOKEN+'&itemid='+ITEMID+'&excludeno='+EXCLUDENO
MOBILE1 = request.urlopen(request.Request(
    url=url, headers=header_dict)).read().decode(encoding='utf-8')
if MOBILE1.split('|')[0] == 'success':
    MOBILE = MOBILE1.split('|')[1]
    print('获取号码是:\n'+MOBILE)
else:
    print('获取TOKEN错误,错误代码'+MOBILE1)

# 获取短信，注意线程挂起5秒钟，每次取短信最少间隔5秒
TOKEN = TOKEN  # TOKEN
ITEMID = ITEMID  # 项目id
MOBILE = MOBILE  # 手机号码
WAIT = 100  # 接受短信时长60s
url = 'http://api.fxhyd.cn/UserInterface.aspx?action=getsms&token=' + \
    TOKEN+'&itemid='+ITEMID+'&mobile='+MOBILE+'&release=1'
text1 = request.urlopen(request.Request(
    url=url, headers=header_dict)).read().decode(encoding='utf-8')
TIME1 = time.time()
TIME2 = time.time()
ROUND = 1
while (TIME2-TIME1) < WAIT and not text1.split('|')[0] == "success":
    time.sleep(5)
    text1 = request.urlopen(request.Request(
        url=url, headers=header_dict)).read().decode(encoding='utf-8')
    TIME2 = time.time()
    ROUND = ROUND+1

ROUND = str(ROUND)
if text1.split('|')[0] == "success":
    text = text1.split('|')[1]
    TIME = str(round(TIME2-TIME1, 1))
    print('短信内容是'+text+'\n耗费时长'+TIME+'s,循环数是'+ROUND)
else:
    print('获取短信超时，错误代码是'+text1+',循环数是'+ROUND)

# 释放号码
url = 'http://api.fxhyd.cn/UserInterface.aspx?action=release&token=' + \
    TOKEN+'&itemid='+ITEMID+'&mobile='+MOBILE
RELEASE = request.urlopen(request.Request(
    url=url, headers=header_dict)).read().decode(encoding='utf-8')
if RELEASE == 'success':
    print('号码成功释放')

# 提取短信内容中的数字验证码
pat = "[0-9]+"
IC = 0
IC = re.search(pat, text)
if IC:
    print("验证码是:\n"+IC.group())
else:
    print("请重新设置表达式")
