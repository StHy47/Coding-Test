while True:
    a,b,c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    else:
        x,y,z = sorted([a,b,c])
        if z >= x+y:
            print('Invalid')
        elif x == y == z:
            print('Equilateral')
        elif x!= y and y!=z and z!= x:
            print('Scalene')
        else:
            print('Isosceles')