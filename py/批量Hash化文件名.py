# 输入文件夹地址。批量使用文件Hash重命名
# 使用SHA3-256

import os
import hashlib

输入的文件夹路径 = input('输入文件夹路径: ')

if 输入的文件夹路径[0] == '"' and 输入的文件夹路径[-1] == '"':
    输入的文件夹路径 = 输入的文件夹路径[1:-1]
前缀 = input('文件前缀(可选):')
os.chdir(输入的文件夹路径)
for i in os.listdir(输入的文件夹路径):
    with open(i, 'rb') as f:
        hash结果 = hashlib.sha3_256(f.read()).hexdigest()
    新文件名 = f'{前缀}{hash结果}{os.path.splitext(i)[1]}'
    os.rename(i, 新文件名)

print('文件Hash化成功')
os.system('pause')
