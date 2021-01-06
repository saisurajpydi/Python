"""
Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.
"""
arr = []
k = int(input("enter the sum value : "))
n = int(input("enter the size of the array"))
print("enter the values in the array ")
for i in range(n):
    arr.append(int(input()))
count = 0
for i in range(n):
    for j in range(i+1,n):
        if(arr[i] + arr[j] == k):
            count += 1
print("the count is : ",count)
