import sys
input = sys.stdin.readline
n = int(input())
file_list = {}
for _ in range(n):
    file_name = input().strip()
    file = file_name.split('.')
    if file[1] in file_list:
        file_list[file[1]] += 1
    else:
        file_list[file[1]] = 1
        
        
        
file_list = dict(sorted(file_list.items()))

for i in file_list:
    print(i,file_list[i])