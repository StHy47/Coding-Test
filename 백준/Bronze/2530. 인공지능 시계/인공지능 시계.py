h,m,s = map(int, input().split())
time = int(input())

cook = time + h*60*60 + m*60 + s

sec = cook % 60
mit = (cook // 60) %60
hour  = ((cook //60) // 60 ) % 24

print(hour, mit, sec)