# 导入datetime模块
import datetime
# 获取当前日期
now = datetime.datetime.now()
# 两位数年份
year = now.year % 100
# 获取本年度第几周
week = now.isocalendar()[1]
# 提示用户输入一个字符串
input_str = input("请输入一个字符串：")[:1]
# 输出结果
print(f"{year}Y{week}W{input_str}")

input('键入 Enter 退出: ')