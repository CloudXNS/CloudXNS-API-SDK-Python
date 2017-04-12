##CloudXNS-API-SDK-Python Package##


##Install##

###Install First###

Extract the archive file downloaded from [CloudXNS-API-SDK-Python.zip](https://github.com//CloudXNS/CloudXNS-API-SDK-Python/archive/master.zip) to your project.
You can install Package:
```shell
pip install restclient
python setup.py install
```

###Install Second###
you can then install using the following command:
```shell
pip install CloudXNS-API-SDK-Python
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
    print result

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

    """
        功能	DDNS快速修改解析记录值
        HTTP请求方式	POST
        URL	https://www.cloudxns.net/api2/ddns
        domain:（必选）已存在的完整域名（如主机记录为@时domain是cloudxns.net，为www时domain是www.cloudxns.net）
        ip:（可选）记录IP值（8.8.8.8）或者多个IP值中间用|分割（8.8.8.8|1.1.1.1）;为空时IP值由API自动获取客户端IP
        line_id:（可选）线路id(通过API获取)，默认值1（全网默认）
    """
    result = api.ddns('ddns.a.com')
    print result
```
