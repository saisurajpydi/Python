a = int(input("enter a number "))
b = int(input("enter a number "))

def gcd(a,b):
    if(a == 0):
        return b
    if(b == 0):
        return a
    if(a == b):
        return a
    if(a > b):
        return gcd(a-b,b)
    return gcd(a,b-a)

if(gcd(a,b)):
    print("Gcd of",a,  "and" , b, 'is', gcd(a, b))
else:
    print('no gcd')

print('LCM is' , (a*b)/gcd(a,b))


