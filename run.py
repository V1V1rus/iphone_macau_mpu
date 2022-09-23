#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
import requests
import time
import hmac
import hashlib
import base64
import urllib.parse
import random


def run():
    r = requests.get(config.url, headers=config.headers)
    result = r.json()

    try:
        stores = result['stores']
    except:
        print("预约网站已维护，10分钟后重新启动")
        time.sleep(60 * 10)
        run()

    for store_key in config.stores:
        if store_key in stores:
            data = stores[store_key]
            # data['MLE63CH/A'] = {'availability': {'contract': False, 'unlocked': True}}
            for key in data:
                if data[key]['availability']['unlocked'] and key in config.iPhones:
                    store_name = config.stores[store_key]
                    name = config.iPhones[key]
                    subfamily = config.subfamily[key]
                    subfamily = subfamily.replace(' ', '+')
                    color = config.colors[key]
                    capacity = config.capacity[key]
                    url = 'https://reserve-prime.apple.com/MO/zh_MO/reserve/A?subfamily={}&color={}&capacity={}' \
                          '&quantity=1&anchor-store=R672&store={}&partNumber={}&channel=&sourceID=&iUID=' \
                          '&iuToken=&iUP=N&appleCare=&rv=&path=&plan=unlocked' \
                        .format(subfamily, color, capacity, store_key, key)
                    message = '[ALERT] {} {}店铺有货!直达链接：{}'.format(name, store_name, url)
                    ding(message)


def ding(message):
    '''发送钉钉通知'''
    params = {
        "msgtype": "text",
        "text": {
            "content": message,
        },
    }
    timestamp = str(round(time.time() * 1000))
    secret_enc = config.secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, config.secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    url = '{}&timestamp={}&sign={}'.format(config.dingtalk, timestamp, sign)
    requests.post(url, json=params)


if __name__ == "__main__":
    while (1):
        run()
        time.sleep(random.randint(3, 9))
