# 2d array 
from array import *
#      T[0]       T[1]      T[2]

T = [[1,2,3,4],[5,6,7,8],[9,10,11]]

for i in T:
    for c in i:
        print(c,end=" ")
    print()

print( T[1])

del T[1]
print(T)

T[1] = [111,1111,11111]
print(T)
T[1][2] = 1000

print(T)

T.insert(3,[100,101,102])

print(T)