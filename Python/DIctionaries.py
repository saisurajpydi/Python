# it stores data as key value pairs
hdic = {
    "key1"   : "data1",
    "key2"   : "data2",
    "key3"   : "data3"
}

print(hdic)

# to get value of a key
x = hdic["key1"]
y = hdic.get("key2")
print(x,y)

# to change value 
hdic["key2"] = "my wish"

print(hdic)

# looping in a dic in keys and values

for i in hdic:
    print(i) # prints keys 
for i in hdic:
    print(hdic[i]) # print values

# looping for values and keys, values

for i in hdic.values():
    print(i)

for x , y in hdic.items():
    print(x,y)

# to check whether a key or value is present in a dic

if "key2" in hdic:
    print(" am present")

# for length

print(len(hdic))

# to add 

hdic["saal"] = " ee sala cup namde "
print(hdic)

# to delete 
# pop()  ,  popitem(),  del , clear

hdic.pop("key1")
print("after pop of key 1" , hdic)

hdic.popitem()
print("pops the last item " , hdic)

del hdic["key2"]
print(" using del to particular ele del" , hdic)

# to copy use copy() , dict()
mydict = hdic.copy()
print("this is mydict",mydict)

heldict = dict(mydict)
print("this is heldict",heldict)

# nested dictionaries

# type  1

myfinal = {
    "child 1" : {
        "name" : "bongu",
        "age"   : 7
    },
    "child 2" : {
        "name " : "bandar",
        "age" : 8
    }
}

print("new nested type 1", myfinal)

# nested type 2

child1 = {
    "name" : "sai",
    "age" : 100
}
child2 = {
    "name" : "paul",
    "age" : 1
}
findict = {
    "child 1" : child1,
    "child 2" : child2
}
print(" this is using type 2",findict)