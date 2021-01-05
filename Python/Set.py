# set is a unordered and unindexed
# but set is changeable
# it is given in { }
hset = {"hello","world","this","is","chitti","the","robo"}
print(hset)

# add and update are used 

hset.add("vasikar")
print(hset)
hset.update("mehh")
print(hset)
hset.update(["mehh"])
print(hset)
# for length
print(len(hset))

# to remove and discard both do same wrk but if the eleemt to b removed is not prst then discard() wont show any error
hset.remove("robo")
hset.discard("world")

print(hset)

# pop() clear del also used

# to join 
# set1.update(set2)
# set1.union(set2)
