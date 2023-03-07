import re
ip=['192.168.1.3','12.34.23.67.4','1234.54.67.456','122.45.67.8']
v_ip=[]
count=0
for i in ip:
    n=re.findall(r'\.',i)
    if len(n)==3:
        v_ip.append(i)
for s in v_ip:
    s.split(".")

    for k in len(s):
        s[k]=int(s[k])
        if s[k]<=255 and s[k]>=1:
            count+=1
        if count==3:
            print(s[k])

