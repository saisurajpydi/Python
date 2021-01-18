arr = [3,0,0,2,0,4]
n = len(arr)
result = 0
# method 1 using loops
"""
for i in range (n):
    left = arr[i]
    for j in range(0,i):
        left = max( left , arr[j])
    right = arr[i]
    for j in range(i+1,n):
        right = max(right , arr[j])
    result += min(left,right)-arr[i]
print(result)
"""
# method 2 O(N) time and space complexity
lmax = [0]*n
rmax = [0]*n
lmax[0] = arr[0]
rmax[n-1] = arr[n-1]

for i in range(1,n):
    lmax[i] = max(lmax[i-1], arr[i])
print(lmax)

for i in range(n-2,-1,-1):
    rmax[i] = max(rmax[i+1], arr[i])
print(rmax)

result = 0
for i in range(n):
    result += max(lmax[i],arr[i]) - arr[i]
print(result )