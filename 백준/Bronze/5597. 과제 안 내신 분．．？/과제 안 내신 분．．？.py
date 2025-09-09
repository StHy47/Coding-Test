student = []
for _ in range(28):
    stu = int(input())
    student.append(stu)
    
l = list(range(1,31))
for i in range(28):
    if student[i] in l:
        l.remove(student[i])
        
print(*l, sep='\n')