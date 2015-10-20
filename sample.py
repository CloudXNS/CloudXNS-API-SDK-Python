#!/usr/bin/env python
#-*- coding:utf-8 -*-


from cloudxns.api import *
try:
    import json
except ImportError:
    import simplejson as json

if __name__ == '__main__':

    print 'CloudXNS API Version: ', Api.vsersion()
    api_key = '$$$$$$$$$'
    secret_key = '#########'
    api = Api(api_key=api_key, secret_key=secret_key)
    # api.set_debug(True)

    # domain list
    # result = api.domain_list()
    # print result['message']
    # print result['data']

    # domain add
    # import random
    # domain = "sdk-test%d.com" % random.randint(1000, 100000)
    # result = api.domain_add(domain)
    # print result

    # domain delete
    # result = api.domain_delete(1347)
    # print result
    # result = api.domain_delete(1356)
    # print result

    # domain stat
    # result = api.domain_stat(domain_id=36574, start_date=20151001, end_date=20151020)
    # result = api.domain_stat(domain_id=5575, start_date=20151001, end_date=20151020)
    # print result

    # host list
    # result = api.host_list(1537, 0, 100)
    # print result

    # delete host
    # result = api.host_delete(14323)
    # print result

    # line list
    # list_all = api.line_list()
    # list_isp = api.line_list(level='isp')
    # list_region = api.line_list(level='region')
    # print 'list_all: ', list_all
    # print 'list_isp: ', list_isp
    # print 'list_isp: ', list_isp

    # ns server list
    # result = api.ns_list()
    # print result

    # record type list
    # result = api.record_type_list()
    # print result

    # record list
    # result = api.record_list(1537, host_id=0)
    # print result
    #
    # record add domain_id, host_name, value, record_type='A', mx=None, ttl=600, line_id=1
    # result = api.record_add(1537, 'www', '1.2.2.3')
    # print result

    # add record spare
    # result = api.record_spare(1537, 14326, 149585, '8.8.8.8')
    # print result

    # update record
    # result = api.record_update(149585, 1537, 'www', '202.114.24.55', spare_ip='114.114.114.112')
    # print result

    # delete record
    # result = api.record_delete(149585, 1537)
    # print result






