# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : 20250714-了解arrow时间包使用.py
@Time    : 2025/7/14 14:30
@Author  : Echo Wang
'''

import arrow

now = arrow.now()
print(now)

# now = arrow.now('America/New_York')
# print(now)

timestamp = 12367898
print(arrow.get(timestamp).format('YYYY-MM-DD HH:mm:ss'))

print(arrow.get('2025-7-14 14:54:30'))
# print(arrow.get('2025-7-14 14:54:30','YYYY-MM-DD HH:mm:ss')) # 后边格式不正确

print(arrow.get('2025-7-14 14:54:30').humanize())

# 时间偏移

tomorrow = now.shift(days=1)
print(tomorrow)
past_time = now.shift(hours=-3)
print(past_time)
future_time = now.shift(weeks=1)
print(future_time)
future_time = now.shift(weekday=3)
print(future_time)


formatted = now.format("YYYY-MM-DD HH:mm:ss")
print(formatted)  # 2023-10-25 14:30:45


utc_time = now.to('UTC')
print(utc_time)
print(utc_time.time())


# 生成每小时的时间点
start = arrow.get("2023-10-01")
end = arrow.get("2023-10-03")
for hour in arrow.Arrow.range("hour", start, end):
    print(hour.format("YYYY-MM-DD HH:mm"))

# 生成每天的时间点
for day in arrow.Arrow.range("day", start, end):
    print(day.format("YYYY-MM-DD"))


