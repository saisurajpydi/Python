arr= [1,2,4,-1,9]
n = len(arr)
sum = 0
maxi = arr[0]
for i in range (n):
    sum = sum + arr[i]
    if(sum > maxi):
        maxi = sum
    if( sum < 0):
        maxi = 0
print(maxi)