##CloudXNS-API-SDK-Python Package##


##Install##

Extract the archive file downloaded from [CloudXNS-API-SDK-Python.zip](https://github.com//CloudXNS/CloudXNS-API-SDK-Python/archive/master.zip) to your project.
You can install Package:
```shell
pip install restclient
python setup.py install
```

##Demo##
==================================================
```python
#!/usr/bin/env python
#-*- coding:utf-8 -*-


from cloudxns.api import *
try:
    import json
except ImportError:
    import simplejson as json

if __name__ == '__main__':

    print 'CloudXNS API Version: ', Api.vsersion()
    api_key = 'XXXXXX'
    secret_key = 'XXXXXX'
    api = Api(api_key=api_key, secret_key=secret_key)
    # api.set_debug(True)

    """
    功能 域名列表
    HTTP 请求方式 GET
    URL https://www.cloudxns.net/api2/domain
    :return: String
    """
    result = api.domain_list()
    print result['message']
    print result['data']


    """
    功能 添加域名
    HTTP 请求方式 POST
    URL https://www.cloudxns.net/api2/domain
    :return: String
    """
    import random
    domain = "sdk-test%d.com" % random.randint(1000, 100000)
    result = api.domain_add(domain)
    print result

    """
    功能 删除域名
    HTTP 请求方式 DELETE
    URL https://www.cloudxns.net/api2/domain
    :return: String
    """
    result = api.domain_delete(32224)
    print result
```
