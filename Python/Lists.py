fruits = ["apple","banana","orange","kiwi"]
fruits.append("cherry")# to add element at last
print(fruits)
fruits.insert(2,"watermelon") # to add at index 2
print(fruits)
print(fruits[1]) # to get the element at index 1
print(fruits[1:4]) # to get the element from 1-3
# print using for loop
for i in fruits:
    print(i)

print("using while loop ")
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1 
print(" using another loop method " )
[print(x) for x in fruits]

tropical = ["mango", "pineapple", "papaya"] # new list
fruits.extend(tropical) # to merge the lists
print(fruits)

# to copy one list to another



# remove pop del clear 
fruits.remove("banana")
print("remove " ,fruits)
fruits.pop(1)
print("pop(1) " ,fruits)
fruits.pop()
print("pop() " ,fruits)
del fruits[2]
print(" del fruits(2) " ,fruits)
tropica = ["mango", "pineapple", "papaya"] # new list
del tropica
print("tropica  deletes whole list" , tropica)
tropic = ["mango", "pineapple", "papaya"] # new list
tropic.clear()
print("clears tropic list" , tropic)

