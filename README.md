# 易码API - Python接口
## 1. 简介：
本python包旨在为[易码api](http://www.51ym.me/User/apidocs.html)提供一个python封装包，使调用变得更简单。
## 2. 使用方法：
### 2.1 安装
    pip install yima
### 2.2 导入
    import yima as ym
### 2.3 功能速览
#### 2.3.1 创建易码客户端实例

    client1 = ym.YMClient('username', 'password', 'token')

通过简单的一句代码，可以创建一个名为client1的易码客户端实例，其参数中：
- 用户名 username 和密码 password 为必填项，token为选填项
- 如果没有填写token，那么客户端实例在初始化时会自动获取token并记录在客户端实例中，因此省去了去官网登录下载token的步骤。

#### 2.3.2 常用功能

客户端创建完毕后，就可以开始操作了。

    client1.get_mobile("itemid")

将项目ID itemid 填入get_mobile()的参数，即可获取一个该项目的手机号。关于项目ID的获取，请移步[项目查询](http://www.51ym.me/User/MobileItemList.aspx)。然后该实例会返回一个手机号。

    client1.get_sms("itemid", "mobile")
    
get_sms()可以返回该手机号所接收到的短信，如果短信还没获取到，或发生其他错误，则会返回错误代码+错误信息。

    client1.release("itemid", "mobile")
    
release()可以释放手机。

如果在上面get_sms()中加入release=1参数（默认为None），那么release()操作则不是必须，获取完短信后会自动释放该手机。

    client1.fetch_sms_until_succeed("itemid", "mobile", timeout=90)
    
上面这句代码可以简易地在发送短信后获取回复的信息，运行这段代码后，程序会开始每隔5秒获取一次短信，直到获取到短信为止。`timeout`为超时参数，默认为90秒，如果90秒后还未获取到短信，代码将会停止获取。

#### 2.3.3 其他功能

    client1.get_token()                     # 向服务器发送请求获取Token
    
    client1.token                           # 获取已经保存到客户端实例中的Token

    client1.get_account_info()              # 获取账户信息
    
    client1.add_ignore("itemid", "mobile")  # 拉黑号码


    
#### 2.3.4 施工中

发送短信功能待开发中。


## 3. 版本历史
### 2019.11.10 - 停更
- 易码凉了，不再更新。
### 2019.1.28 - 版本 0.1.3
- 现在使用fetch_sms_until_succeed()函数，仅在返回错误码为“3001”-“尚未收到短信”时才会尝试重试，如果返回的是其它错误码，则会raise报错信息。如果超时,则会raise超时错误。

### 2019.1.24 - 版本 0.1.2
- 修复了如果服务器返回错误代码时，程序会出现 `NameError: name 'error_codes' is not defined` 的错误
- 在get_sms()函数中添加了release参数的接口
- 现在如果在创建客户端实例时，用户名和密码不正确，会返回报错信息。

### 2019.1.23 - 版本 0.1.1
- 修复了依赖库中包含基础库“time”而导致pip install不成功的bug

### 2019.1.23 - 版本 0.1.0
- 添加易码api基础功能
- 第一次尝试发PyPI包，好紧张啊，会不会有潜规则啊

## 4. Bug反馈及功能需求添加
如有发现bug或有其它功能需求，请直接发Issue或者联系：yihua.zhou@outlook.com。

