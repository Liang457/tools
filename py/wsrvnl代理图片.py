# 输入一个链接，然后输出wsrl.nl的代理图片链接
# wsrv.nl是一个图片加速服务

import os
while True:
    url = input('输入图片链接:')
    print(f'\nhttps://wsrv.nl/?url={url}\n')
