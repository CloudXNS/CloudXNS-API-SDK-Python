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
    #result = api.domain_list()
    #print result['message']
    #print result['data']


    """
    功能 添加域名
    HTTP 请求方式 POST
    URL https://www.cloudxns.net/api2/domain
    :return: String
    """
    #import random
    #domain = "sdk-test%d.com" % random.randint(1000, 100000)
    #result = api.domain_add(domain)
    #print result

    """
    功能 删除域名
    HTTP 请求方式 DELETE
    URL https://www.cloudxns.net/api2/domain
    :return: String
    """
    #result = api.domain_delete(32224)
    #print result

    """
    功能 域名统计
    HTTP 请求方式 GET
    URL https://www.cloudxns.net/api2/domain_stat/:id
        请求参数：
            参数名称 类型 必填 描述
            host String 是 主机名，查询全部传 all
            code String 是 统计区域 Id 或统 ISP Id，查询全部传 all
            start_date Date 是 开始时间 格式：yyyy-mm-dd
            end_date Date 是 结束时间 格式：yyyy-mm-dd
    :return: String
    """
    #result = api.domain_stat(domain_id=2125, start_date=20151001, end_date=20151020)
    #print result

    """
    功能 主机记录
    HTTP 请求方式 GET
    URL https://www.cloudxns.net/api2/host/:domain_id?offset=:offset&row_num=:row_num
        请求参数：
            参数名称 类型 必填 描述
            domain_id Integer 是 域名ID
            offset Integer  否 记录开始的偏移,第一条记录为 0,依次类推
            row_num Integer 否 要获取的记录的数量,比如获取 30 条,则为 30,最大可取 2000条
    :return: String
    """
    #result = api.host_list(2125, 0, 30)
    #print result

    """
    功能 删除主机记录
    HTTP 请求方式 GET
    URL https://www.cloudxns.net/api2/host/:id
        请求参数：
            参数名称 类型 必填 描述
            hostId Integer 是 主机记录id
    :return: String
    """
    #result = api.host_delete(295167)
    #print result

    """
    功能 线路列表
    HTTP 请求方式 GET
    URL https://www.cloudxns.net/line
    :return: String
    """
    #list_all = api.line_list()
    #list_isp = api.line_list(level='isp')
    #list_region = api.line_list(level='region')
    #print 'list_all: ', list_all
    #print 'list_isp: ', list_isp
    #print 'list_region: ', list_region

    """
    功能 NS服务器列表
    HTTP 请求方式 GET
    URL https://www.cloudxns.net/api2/ns_server
    :return: String
    """
    #result = api.ns_list()
    #print result

    """
    功能 记录类型列表
    HTTP 请求方式 GET
    URL https://www.cloudxns.net/api2/type
    :return: String
    """
    #result = api.record_type_list()
    #print result

    """
    功能 解析记录列表
    HTTP 请求方式 GET
    URL https://www.cloudxns.net/api2/record/:domain_id?host_id=0&offset=:offset&row_num=:row_num
        请求参数：
            参数名称 类型 必填 描述
            domain_id Integer 是 域名ID
            offset Integer  否 记录开始的偏移,第一条记录为 0,依次类推
            row_num Integer 否 要获取的记录的数量,比如获取 30 条,则为 30,最大可取 2000条
    :return: string
    """
    #result = api.record_list(2125, 0, 0, 30)
    #print result


    """
    功能 添加解析记录
    HTTP 请求方式 GET
    URL https://www.cloudxns.net/api2/record
        请求参数：
            参数名称 类型 必填 描述
            domain_id Integer  域名 id
            host_name String  主机记录名称 如 www, 默认@
            value String 记录值, 如IP:8.8.8.8,CNAME:cname.cloudxns.net., MX: mail.cloudxns.net.
            record_type String 记录类型,通过 API 获得记录类型,大写英文,比如:A
            mx Integer 优先级,范围 1-100。当记录类型是 MX/AX/CNAMEX 时有效并且必选
            ttl Integer TTL,范围 60-3600,不同等级域名最小值不同
            line_id Integer 线路id,(通过 API 获得记录线路 id)
        :return: String
    """
    #result = api.record_add(2125, 'w0', '3.3.3.3', 'A', 55, 600, 1)
    #print result


    """
    功能 添加备记录
    HTTP 请求方式 GET
    URL https://www.cloudxns.net/api2/record/spare
        请求参数：
            参数名称 类型 必填 描述
            domain_id Integer  域名 id
            host_id Integer  主机记录名称 如 www, 默认@
            record_id Integer 解析记录id
            value String 记录值, 如IP:8.8.8.8,CNAME:cname.cloudxns.net., MX: mail.cloudxns.net.
        :return: String
    """
    # add record spare
    #result = api.record_spare(2125, 295170, 629121, '192.168.100.222')
    #print result

    """
    功能 更新解析记录
    HTTP 请求方式 GET
    URL https://www.cloudxns.net/api2/record/:id
        请求参数：
            参数名称 类型 必填 描述
            record_id Integer 解析记录id
            domain_id Integer 域名id
            host_name String 主机记录名称 如 www, 默认@
            value String 记录值, 如IP:8.8.8.8,CNAME:cname.cloudxns.net., MX: mail.cloudxns.net.
            record_type String 记录类型,通过 API 获得记录类型,大写英文,比如:A
            mx Integer 优先级,范围 1-100。当记录类型是 MX/AX/CNAMEX 时有效并且必选
            ttl Integer TTL,范围 60-3600,不同等级域名最小值不同
            line_id Integer 线路 id,(通过 API 获得记录线路 id)
        :return: String
    """
    #result = api.record_update(629125, 2125, 'w1111111', '192.168.100.210', 'AX', 55, 600, 1)
    #print result

    """
    功能 删除解析记录
    HTTP 请求方式 GET
    URL https://www.cloudxns.net/api2/record/:id/:domain_id
        请求参数：
            参数名称 类型 必填 描述
            record_id Integer 解析记录id
            domain_id Integer  域名 id
        :return: String
    """
    #result = api.record_delete(629125, 2125)
    #print result






