#T = int(input("enter no. of test cases : "))
n = int(input("enter the size of array "))
arr = []
print('enter the array elements ')
for i in range(n):
    arr.append(int(input()))
m = int(input("enter the no. of students " ))
result = 1000 # any big value
arr.sort() 
print(arr)
for i in range(n-m):
    result = min(result , arr[i+m-1] - arr[i])
print(result)