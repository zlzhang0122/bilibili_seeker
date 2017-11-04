#!/usr/bin/python
# -*- encoding:utf-8 -*-
#author:zhangjiaogg
#github:https://github.com/zlzhang0122/

import threading
from collections import namedtuple
from concurrent import futures
import time
import csv

import requests

header = ["aid", "view", "danmaku", "reply", "favorite", "coin", "share"]
Video = namedtuple('Video', header)
headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}
total = 1
result = []
lock = threading.Lock()

def run(url):
    global total
    req = requests.get(url, headers = headers, timeout=6).json()
    time.sleep(0.5)
    try:
        data = req['data']
        video = Video(data['aid'],
                      data['view'],
                      data['danmaku'],
                      data['reply'],
                      data['favorite'],
                      data['coin'],
                      data['share']
                      )
        with lock:
            result.append(video)
            print(total)
            total += 1
    except:
        pass

def save():
    with open("result.csv", "w+") as f:
        f_csv = csv.writer(f)
        f_csv.writerow(header)
        f_csv.writerow(result)

if __name__ == "__main__":
    urls = ["http://api.bilibili.com/archive_stat/stat?aid={}".format(i)
            for i in range(1000)]
    with futures.ThreadPoolExecutor(32) as executor:
        executor.map(run, urls)
    save()