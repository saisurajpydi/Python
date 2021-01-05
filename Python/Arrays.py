# Arrays are not presnt in python and arrays are implemented  using lists 
car = ["bmw","audi","volkswagon","maruthi suzuki","kia","tata"]
print(car[0])
car[0] = "honda"
print("changing index at 0" , car)
car.append("lambergini")
print("using append" , car)
car.pop(1)
print("using pop()",car)
car.remove("kia")
print("remove()" ,car) # remove only deletes only the first occurance of the element
print("length of the car is ",len(car))

for i in car:
    print(i)

from array import*
array1 = array('i',[1,2,3,4,5,6])
for i in array1:
    print(i)
# to insert at a given index
array1.insert(1,100)
print(array1)

print(array1.index(100)) # to get the index of an element 

# to update 

array1[2] = 80
print(array1)
    
