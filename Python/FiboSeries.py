nterms = int(input("enter the no. of terms"))
n1,n2 = 0,1
count = 0

print(" fibonacci series is ")
while count < nterms :
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth 
    count += 1