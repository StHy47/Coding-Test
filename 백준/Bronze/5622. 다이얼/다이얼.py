word= input().lower()

n = 0
for i in range(len(word)):
    if word[i] in ['a','b','c']:
        n += 3
    elif word[i] in ['d','e','f']:
        n += 4
    elif word[i] in ['g','h','i']:
        n += 5
    elif word[i] in ['j','k','l']:
        n += 6
    elif word[i] in ['m','n','o']:
        n += 7
    elif word[i] in ['p','q','r','s'] :
        n += 8
    elif word[i] in ['t','u','v']:
        n += 9
    elif word[i] in ['w','x','y','z']:
        n += 10
    else:
        n += 0

print(n)