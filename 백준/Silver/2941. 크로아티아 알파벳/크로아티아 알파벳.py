croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()


for i in croa:
    c = [word.find(i) for i in croa]
    word = word.replace(i,'9')

print(len(word))