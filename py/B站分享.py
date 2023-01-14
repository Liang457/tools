# 获取一个比较适合拿来分享的文本

import urllib.request
import json
import os
import logging

bvid = input('输入稿件BV号(链接也可以): ')

if (bvid[:31].lower() == 'https://www.bilibili.com/video/' and bvid[:31]) or (bvid[:15].lower() == 'https://b23.tv/' and bvid[15:]):
    for j in bvid.split('?'):
        for i in j.split('/'):
            if i[:2].upper() == 'BV':
                bvid = i[:2].upper()+i[2:]
                break

if bvid[:2].upper() != 'BV':
    logging.critical(f'"{bvid}"不是正确的BV号，请输入正确的BV号')
    os.system('pause')
    exit(-1)

api_url = f'https://api.bilibili.com/x/web-interface/view?bvid={bvid}'
s_url = f'https://b23.tv/{bvid[:2].upper()+bvid[2:]}'
data_s = urllib.request.urlopen(api_url)
data_s = json.loads(data_s.read().decode('utf-8'))

if data_s['code'] != 0:
    logging.critical(f'不存在"{bvid}"，你确定吗？')
    os.system('pause')
    exit(-1)

print(f"\n[{data_s['data']['title']} - {data_s['data']['owner']['name']}] {s_url}\n")
os.system('pause')
