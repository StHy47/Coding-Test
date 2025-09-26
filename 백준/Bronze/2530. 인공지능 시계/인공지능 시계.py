h,m,s = map(int, input().split())
time = int(input())

t_s = time % 60
t_m = (time // 60) % 60
t_h = ((time // 60 )//60)% 24

c_h = h + t_h
c_m = m + t_m
c_s = s + t_s

if c_s >= 60:
    c_s = c_s - 60
    c_m = c_m + 1
if c_m >= 60:
    c_m = c_m - 60
    c_h = c_h + 1

if c_h >= 24:
    c_h = c_h - 24
    
    
print(c_h, c_m, c_s)
    