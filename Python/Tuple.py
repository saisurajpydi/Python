thistuple = ("hello","world","c++","java","dbms")
print("this is a tuple" ,tuple)
# tuple is ordered, unchangable 
# tuple operations 
print(len(thistuple))
print(type(thistuple))

print(thistuple[1]) # to get a element with index
print(thistuple[2:4])

if "world" in thistuple:
    print("world is present")

# to update a tuple it is converted into a list and updations are done

x = list(thistuple)
x.append("hai")
thistuple = tuple(x)
print(thistuple)

# same for remove  elemnt tuple -> list -> element removed -> tuple
#  del operation deletes the whole tuple 

x = list(thistuple)
x.remove("hai")
thistuple = tuple(x)
print(thistuple)

htuple = thistuple
print(htuple)
del thistuple
#print(thistuple)
print(htuple)

# specifying objects i.e unpacking 
(egg,bread,*meat) = htuple
print(egg)
print(bread)
print(meat)

# looping through tuples

for i in htuple:
    print(i)

for i in range(len(htuple)):
    print(htuple[i])

i = 0
while i < len(htuple):
    print(htuple[i])
    i += 1

# to concat the tuples

thistuple = ("this", " is "," tuple")

new = htuple + thistuple
print(new)

# tuple methods  index and count 

print(htuple.count("world"))
print(htuple.index("world"))