# 生成一个雪花视频，用以遮挡视频

import shutil
import PIL.Image
import os
import random

帧速率 = 24
高度 = int(input('高度:'))
宽度 = int(input('宽度:'))
时长 = int(input('时长(s):'))

try:
    os.mkdir('tmp')
except:
    pass

for i in range(时长 * 帧速率):
    image = PIL.Image.new(mode='RGB', size=(高度, 宽度))
    px = image.load()
    for h in range(高度):
        for w in range(宽度):
            px[h, w] = random.choice([(255, 255, 255), (0, 0, 0)])
    image.save(f"tmp/{i}.nopush.bmp")
    image.close()

os.system(f'ffmpeg -f image2 -i "tmp/%d.nopush.bmp" 雪花.nopush.mp4 ')

shutil.rmtree('tmp')
os.system('pause')
