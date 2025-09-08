h,m = map(int, input().split()) #now_time
c = int(input()) #cooking time

if c >=60:
    c_h = int(c/60)
    c_m = c%60
else:
    c_h = 0
    c_m = c

cook_h = h+ c_h
cook_m = m + c_m

if cook_m >=60:
    cook_m = cook_m - 60
    cook_h = cook_h + 1
else:
    cook_m = cook_m
    
    
if cook_h >=24:
    cook_h = cook_h-24
else :
    cook_h = cook_h
    

print(cook_h, cook_m)