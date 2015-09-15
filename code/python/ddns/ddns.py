# -*- coding: utf-8 -*-

import urllib2
import os
import json
import requests
import time
import daemon

from config import target, public_data

headers = {
    'UserAgent': 'NAIVE DDNS Client/1.0.0 (naive@aliyun.com)'
}

name = target.split('.')[0]
domain = '.'.join(target.split('.')[-2:])

domain_list_api = 'https://dnsapi.cn/Domain.List'
record_modify_api = 'https://dnsapi.cn/Record.Modify'
record_list_api = 'https://dnsapi.cn/Record.List' 

ip = ''

# At first we dont get the ip in record, so get it once,
# and then we dont need it if ip has not been changed.
def try_modify_record_if_ip_changed():
    global ip

    ipinfo = json.loads(os.popen('curl http://ipinfo.io').read())
    if ip == ipinfo['ip']:
        return

    r = requests.post(domain_list_api, data=public_data, headers=headers)
    domains = {i['punycode']: i['id'] for i in r.json()['domains']}

    record_list_data = public_data.copy()
    record_list_data['domain_id'] = domains[domain]

    r = requests.post(record_list_api, data=record_list_data, headers=headers)
    records = {i['name']: i['id'] for i in r.json()['records']}
    records_ip = {i['name']: i['value'] for i in r.json()['records']}
    if records_ip[name] == ipinfo['ip']:
        print('ip no change since last start.')
        ip = ipinfo['ip']
        return

    record_modify_data = record_list_data.copy()
    record_modify_data['record_id'] = records[name]
    record_modify_data['record_type'] = 'A'
    record_modify_data['record_line'] = u'默认'
    record_modify_data['value'] = ipinfo['ip']
    record_modify_data['mx'] = 5
    record_modify_data['sub_domain'] = name
    r = requests.post(record_modify_api, data=record_modify_data, headers=headers)
    print(r.json())
    print('new ip: '+ipinfo['ip']+' old ip:'+ip)
    ip = ipinfo['ip']

def main():
    while 1:
        try_modify_record_if_ip_changed()
        time.sleep(30)

if __name__ == '__main__':
    with daemon.DaemonContext():
        main()
