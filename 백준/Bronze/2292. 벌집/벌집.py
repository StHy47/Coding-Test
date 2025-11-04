n = int(input())
end_num = 1
r = 1
while n > end_num:
    end_num += 6*r
    r += 1
print(r)