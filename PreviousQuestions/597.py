import datetime

i=datetime.date(2000,1,1)
end=datetime.date(2020,10,2)
ans=0
while i!=end:
    if i.weekday()==0 or i.day==1:
        ans+=2
    else:
        ans+=1
    i+=datetime.timedelta(days=1)
print(ans)