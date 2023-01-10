import urllib.request
import json
import os
import logging
import re
import multiprocessing


def SearXNGPing(url: str):
    def _re(str: str):
        try:
            _min = re.search(r'(?<=最短 = )[0-9]+ms', str).group(0)
            _max = re.search(r'(?<=最长 = )[0-9]+ms', str).group(0)
            _med = re.search(r'(?<=平均 = )[0-9]+ms', str).group(0)
            return {'min': _min, 'max': _max, 'med': _med}
        except AttributeError:
            return {'min': '10000ms', 'max': '10000ms', 'med': '10000ms'}

    logging.basicConfig(
        format='[%(asctime)s]%(levelname)s - %(message)s', level=logging.DEBUG, datefmt='%H:%M:%S')

    logging.info(f'正在测试 {url}')
    out = {'url': url}
    url = re.search(r'(?<=https://)[\d\w\.-]+', url).group(0)
    # Ping 检测
    # IPv4测试
    ipv4ping = os.popen(f'ping "{url}" -4').read()
    out['ipv4_ping'] = _re(ipv4ping)
    # IPv6测试
    ipv6ping = os.popen(f'ping "{url}" -6').read()
    out['ipv6_ping'] = _re(ipv6ping)

    return out


if __name__ == '__main__':
    logging.basicConfig(
        format='[%(asctime)s]%(levelname)s - %(message)s', level=logging.DEBUG, datefmt='%H:%M:%S')

    logging.info('获取实例列表中，等会...')
    SearX实例数据 = json.loads(urllib.request.urlopen(
        'https://searx.space/data/instances.json').read())

    SearX数据个数 = 0
    SearX实例列表 = []
    for i in SearX实例数据['instances']:
        # 清除不符合要求的实例并新建列表
        # 判断SearXNG是否是HTTPS实例
        if SearX实例数据['instances'][i]['network_type'] == 'normal':
            # 尝试获取 Error 数据，有的话就不添加
            try:
                SearX实例数据['instances'][i]['error']
            except KeyError:
                SearX数据个数 += 1
                SearX实例列表.append(i)
            else:
                continue

    logging.info(f'获取成功，一共有{str(SearX数据个数)}个SearXNG实例')
    # print(SearX实例列表)
    # 多进程
    logging.info(f'Ping 测试，等会')
    with multiprocessing.Pool(None) as pool:
        out = pool.map(SearXNGPing, SearX实例列表)

    logging.info(f'写入文件中')
    out = sorted(out, key=lambda i: (int(i['ipv4_ping']['med'][:-2])))

    with open('SearXNG.nopush.csv', 'w', encoding='utf-8') as out_file:
        out_file.writelines(
            'SearXNG实例链接,版本,TLS,HTML,IPv4 平均 Ping,IPv6 平均 Ping\n')
        for i in out:
            SearXNG实例链接 = i['url']
            try:
                版本 = SearX实例数据['instances'][i['url']
                                            ]['version'].replace(',', '&')
            except:
                版本 = '未知'
            try:
                TLS = SearX实例数据['instances'][i['url']
                                             ]['tls']['grade'].replace(',', '&')
            except:
                TLS = '未知'
            try:
                HTML = SearX实例数据['instances'][i['url']
                                              ]['html']['grade'].replace(',', '&')
            except:
                HTML = '未知'
            if i['ipv4_ping']['med'] == '10000ms':
                IPv4Ping = 'Ping不通'
            else:
                IPv4Ping = i['ipv4_ping']['med'].replace(',', '&')
            if i['ipv6_ping']['med'] == '10000ms':
                IPv6Ping = 'Ping不通'
            else:
                IPv6Ping = i['ipv6_ping']['med'].replace(',', '&')

            file_a_line = f'{SearXNG实例链接},{版本},{TLS},{HTML},{IPv4Ping},{IPv6Ping}\n'
            out_file.writelines(file_a_line)

    logging.info('检测完成，已经生成在 SearXNG.nopush.csv 中')
    os.system('pause')