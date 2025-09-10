n = int(input())

for _ in range(n):
    word = list(input())
    a = word[0]
    z = word[len(word)-1]
    print(a, z, sep='')