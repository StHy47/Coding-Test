score = str(input())

if 'A' in score:
    an = 4
elif 'B' in score:
    an = 3
elif 'C' in score:
    an = 2
elif 'D' in score:
    an = 1
else:
    an = 0
    
if '+' in score:
    an += 0.3
elif '-' in score:
    an -= 0.3
else:
    an = an
    
print(f'{an:.1f}')