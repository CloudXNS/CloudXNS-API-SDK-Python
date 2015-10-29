#-*- coding:utf-8 -*-

import hashlib
import time
import httplib2
import urllib
from restclient import GET, POST, PUT, DELETE, fix_params
try:
    import json
except ImportError:
    import simplejson as json


__API_URL__ = 'https://www.cloudxns.net/api2/'


class Api:
    def __init__(self, api_key=None, secret_key=None):
        self.__debug = False
        self.__content_type = 'application/json'
        self.__headers = {
            'API-FORMAT': 'json',
            'Content-Type': self.__content_type,
            'user-agent': 'CloudXNS-Python/v2 (CloudXNS-API-SDK-Python) Python-httplib2/0.9.2'
        }
        self.__api_key = ''
        self.__secret_key = ''
        if api_key:
            self.set__api_key(api_key)
        if secret_key:
            self.set__secret_key(secret_key)

    def set_debug(self, debug=True):
        self.__debug = debug
        if debug:
            httplib2.debuglevel = 1
        else:
            httplib2.debuglevel = 0

    def __header_update(self, uri, data=None):
        if data:
            data = json.dumps(data)
        else:
            data = ''
        md5 = hashlib.md5()
        date = time.strftime('%a %b %d %H:%M:%S %Y', time.localtime())
        md5.update(self.__api_key + __API_URL__ + uri + data + date + self.__secret_key)
        self.__headers['API-HMAC'] = md5.hexdigest()
        self.__headers['API-REQUEST-DATE'] = date

    def set__api_key(self, api_key):
        self.__api_key = api_key
        self.__headers['API-KEY'] = api_key

    def set__secret_key(self, secret_key):
        self.__secret_key = secret_key

    def __request(self, method, uri, data=None):
        if method not in ['GET', 'POST', 'PUT', 'DELETE']:
            raise Exception("Invalid HTTP request method")

        if method in ['POST', 'PUT']:
            self.__header_update(uri, data=data)
        elif data:
            params = urllib.urlencode(fix_params(data))
            self.__header_update(uri + '?' + params)
        else:
            self.__header_update(uri)

        if self.__debug:
            resp, content = eval(method)(__API_URL__ + uri,
                                                params=data, headers=self.__headers, resp=self.__debug, async=False)
            return resp, content

        else:
            content = eval(method)(__API_URL__ + uri,
                                          params=data, headers=self.__headers, resp=self.__debug, async=False)

            return content

    @staticmethod
    def vsersion():
        return GET(__API_URL__ + 'version')

    def domain_list(self):
        """
        功能 域名列表
        HTTP 请求方式 GET
        URL https://www.cloudxns.net/api2/domain
        :return: String
        """
        return self.__request('GET', 'domain')

    def domain_add(self, domain_name):
        """
        功能 添加域名
        HTTP 请求方式 POST
        URL https://www.cloudxns.net/api2/domain
        :return: String
        """
        data = {"domain": domain_name}
        return self.__request('POST', 'domain', data=data)

    def domain_delete(self, domain_id):
        """
        功能 删除域名
        HTTP 请求方式 DELETE
        URL https://www.cloudxns.net/api2/domain
        请求参数：
            参数名称 类型 必填 描述
            domain_id Integer 是 域名ID
        :return: String
        """
        if isinstance(domain_id, int):
            domain_id = str(domain_id)
        return self.__request('DELETE', 'domain/' + domain_id)

    def domain_stat(self, domain_id, start_date, end_date, host='all', code='all'):
        """
        功能 获取某域名解析量统计数据
        HTTP 请求方式 GET
        URL https://www.cloudxns.net/api2/domain_stat/:id
        URL 参数说明 Id：域名 ID
        请求参数：
            参数名称 类型 必填 描述
            host String 是 主机名，查询全部传 all
            code String 是 统计区域 Id 或统 ISP Id，查询全部传 all
            start_date Date 是 开始时间 格式：yyyy-mm-dd
            end_date Date 是 结束时间 格式：yyyy-mm-dd
        :return:
        """
        if isinstance(domain_id, int):
            domain_id = str(domain_id)
        data = {
            'host': host,
            'code': code,
            'start_date': start_date,
            'end_date': end_date
        }
        return self.__request('GET', 'domain_stat/' + domain_id, data=data)

    def host_list(self, domain_id, offset=0, row_num=2000):
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
        if isinstance(domain_id, int):
            domain_id = str(domain_id)
        if row_num > 2000:
            raise Exception("param 'row_num' max is 2000")
        return self.__request('GET', 'host/'+domain_id, {"offset": offset, "row_num": row_num})

    def host_delete(self, host_id):
        """
        功能 删除主机记录
        HTTP 请求方式 GET
        URL https://www.cloudxns.net/api2/host/:id
            请求参数：
                参数名称 类型 必填 描述
                host_id Integer 是 主机记录id
        :return: String
        """
        if isinstance(host_id, int):
            host_id = str(host_id)
        return self.__request('DELETE', 'host/'+host_id)

    def line_list(self, level=''):
        """
        功能 线路列表
        HTTP 请求方式 GET
        URL https://www.cloudxns.net/line
        :return: String
        """
        if level not in ['', 'region', 'isp']:
            raise Exception("param 'level' mast be '' or 'region' or 'isp' ")
        if level != '':
            uri = 'line/'+level
        else:
            uri = 'line'
        return self.__request('GET', uri)

    def ns_list(self):
        """
        功能 NS服务器列表
        HTTP 请求方式 GET
        URL https://www.cloudxns.net/api2/ns_server
        :return: String
        """
        return self.__request('GET', 'ns_server')

    def record_type_list(self):
        """
        功能 记录类型列表
        HTTP 请求方式 GET
        URL https://www.cloudxns.net/api2/type
        :return: String
        """
        return self.__request('GET', 'type')

    def record_list(self, domain_id, host_id=0, offset=0, row_num=30):
        """
        功能 获取解析记录列表
        HTTP 请求方式 GET
        URL https://www.cloudxns.net/api2/record/:domain_id?host_id=0&offset=:offset&row_num=:row_num
        URL 参数说明
            domain_id:域名 id
            host_id:主机记录 id(传 0 查全部)
            offset:记录开始的偏移，第一条记录为 0，依次类推,默认取 0
            row_num:要获取的记录的数量， 比如获取 30 条， 则为 30,最大可取 2000
            条,默认取 30 条.
        :return:
            code int 请求状态，详见附件 code 对照表
            message String 操作信息，提示操作成功或错误信息
            total int 总记录条数
            offset int 记录开始的偏移
            row_num int 要获取的记录的数量
            data array 记录列表
                record_id: 解析记录 id
                host_id:主机记录 id
                host：主机记录名
                line_id：线路 ID
                line_zh：中文名称
                line_en：英文名称
                mx：优先级
                Value：记录值
                Type：记录类型
                Status：记录状态(ok 已生效 userstop 暂停)
                create_time：创建时间
                update_time：更新时间
        """
        if isinstance(domain_id, int):
            domain_id = str(domain_id)
        if row_num > 2000:
            raise Exception("param 'row_num' max is 2000")
        return self.__request('GET', 'record/'+domain_id, {"host_id": host_id, "offset": offset, "row_num": row_num})

    def record_add(self, domain_id, host_name, value, record_type='A', mx=None, ttl=600, line_id=1):
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
        if record_type not in ["A", "CNAME", "NS", "MX", "TXT", "AAAA", "LINK", "AX",
                               "CNAMEX", "SRV", "DR301X", "DR302X", "DRHIDX"]:
            raise Exception("Invalid record type")

        data = {
            "domain_id": domain_id,
            "host": host_name,
            "value": value,
            "type": record_type,
            "ttl": ttl,
            "line_id": line_id
        }

        if (mx is not None) and (mx >= 1 or mx <= 100):
            data['mx'] = mx

        return self.__request('POST', 'record', data=data)

    def record_spare(self, domain_id, host_id, record_id, value):
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
        data = {
            "domain_id": domain_id,
            "host_id": host_id,
            "record_id": record_id,
            "value": value
        }
        return self.__request('POST', 'record/spare', data=data)

    def record_update(self, record_id, domain_id, host_name, value,
                      record_type='A', mx=None, ttl=600, line_id=1, spare_data=None):
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
                spare_data String 备IP
            :return: String
        """
        if record_type not in ["A", "CNAME", "NS", "MX", "TXT", "AAAA", "LINK", "AX",
                               "CNAMEX", "SRV", "DR301X", "DR302X", "DRHIDX"]:
            raise Exception("Invalid record type")

        data = {
            "domain_id": domain_id,
            "host": host_name,
            "value": value,
            "type": record_type,
            "ttl": ttl,
            "line_id": line_id
        }

        if (mx is not None) and (mx >= 1 or mx <= 100):
            data['mx'] = mx

        if spare_data:
            data['bak_ip'] = spare_data

        if isinstance(record_id, int):
            record_id = str(record_id)

        return self.__request('PUT', 'record/' + record_id, data=data)

    def record_delete(self, record_id, domain_id):
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
        if isinstance(record_id, int):
            record_id = str(record_id)

        if isinstance(domain_id, int):
            domain_id = str(domain_id)

        return self.__request('DELETE', 'record/' + record_id + '/' + domain_id)
