# ffmpeg合并音频和无音频的视频为.mp4文件
# 不重新编码

import os

f1 = ''
f2 = ''
f3 = ''

while True:
    f1 = input('输入第一个文件')
    if f1:
        break

while True:
    f2 = input('输入第二个文件')
    if f2:
        break

f3 = f2[:-1]+'.new.mp4"'

print(f'ffmpeg -i {f1} -i {f2} -c copy {f3}')
with open('tmp.bat', 'w') as f:
    f.write(f'ffmpeg -i {f1} -i {f2} -c copy {f3}')
os.system('tmp.bat')
os.remove('tmp.bat')

os.system('pause')