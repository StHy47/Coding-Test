import sys
input = sys.stdin.readline
n = int(input())

word_list = set()
for _ in range(n):
    word = str(input().strip())
    word_list.add(word)
    
word_list = list(word_list)
word_list = sorted(word_list)
word_list = sorted(word_list, key=len)

for i in word_list:
    print(i)