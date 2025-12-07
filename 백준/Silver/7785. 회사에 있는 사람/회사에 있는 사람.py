import sys
input = sys.stdin.readline
n = int(input())
people = set()
for _ in range(n):
    name, company = map(str, input().split())
    if company == 'enter':
        people.add(name)
    else:
        people.remove(name)

people= sorted(list(people), reverse=True)
for i in people:
    print(i)