import os
import sys
import datetime
s=input()
date=datetime.date(int(s[:4]),int(s[4:6]),int(s[6:]))
flag=True
for i in range(99999999):
    date+=datetime.timedelta(days=1)
    s=date.strftime("%Y%m%d")
    if s[:]==s[::-1]:
        if flag==True:
            flag=False
            print(s)
        if s[0]==s[2] and s[1]==s[3]:
            print(s)
            break