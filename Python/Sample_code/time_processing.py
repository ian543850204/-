# Python time_processing
# create by Ian
# 2022/4/18

#時間處理套件
import time, datetime
from datetime import timedelta
from datetime import datetime #import date函式
import sys
import math

#現在時間
today = datetime.now()

print("今天日期 : "+str(today))

#指定日期時間
SC_date_fixed = datetime(2022,4,18)
print("設定日期")
print(SC_date_fixed)

#日期天數加 1
SC_date_fixed = SC_date_fixed + timedelta(days=1)
print("設定日期加 1 天")
print(SC_date_fixed)