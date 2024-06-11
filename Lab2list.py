# myList = [1,5,8,200,4,"Test"] # position array 0,1,2,4..
# print(myList[4]) #read value array 4

# myList[4] = 900
# print(myList[4])

# myList[0] = myList[2] #change value array 0 with value in array 2
# print(myList[0])
# print("New List:", myList)
# print("List length:", len(myList))

# myString = "ABCDEF"
# print("String length:", len(myString))
# print("String at array 3: ", myString[3])
# print("Slice type 1 myString:", myString[1:3]) #same concept as range. [1:3] means discard any value before array 1 and value from array 3 onward
# print("Slice type 2 myString:", myString[-3:-1])
# print("Slice type 3 myString:", myString[:5])
# print("Slice type 4 myString:", myString[2:])
# print("Slice type 5 myString:", myString[:])


###Append

myList = []
myList1 = []

for i in range(5):
    myList.append(i)
    
print("My new list using append method is", myList)

for i in range(5):
    myList1.insert(i,i+5)
    
print("My new list using insert method is", myList1)


