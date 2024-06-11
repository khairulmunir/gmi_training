# #### for loop using range. (5) one argument, 5 means range up to 5 with initial start number is 0. 5 is not include at the end.

# for i in range (5): # initial value of i = 0. range(5) the 'for loop' will look the i number, increasing 0,1,2,3,4. at 5 it will stop. Last i number is 4 then printed at line 4
#     print(i)
    
# print("Outside for loop.", i)


# #### for loop using range. (2, 5) 2 arguments, 5 means range up to 5 with initial start number is 2

# for i in range (2,5): # range(2,5) = range(start, end). i start at 2
#     print(i)
    
# print("Outside for loop.", i)

# # for i in range (2,10,2): # range(2,10,2) = range(start, end, incrementvalue). i start at 2 end at 10, but increment for every number is 2
# #     print(i)
    
# # print("Outside for loop.", i)


# # for i in range (2,10,2): # range(2,10,2) = range(start, end, incrementvalue). i start at 2 end at 10, but increment for every number is 2
# #     if i == 6:
# #         break #exit for loop if i=6
# #     print("Still inside for loop, i")
    
# # print("Outside for loop.", i)



# for i in range (2,10,2): # range(2,10,2) = range(start, end, incrementvalue). i start at 2 end at 10, but increment for every number is 2
#     if i == 6:
#         continue #continue for loop even i=6 until end of the range
#     print("Still inside for loop", i)
    
# print("Outside for loop.", i)



# for i in range (2,20,2): # range(2,10,2) = range(start, end, incrementvalue). i start at 2 end at 10, but increment for every number is 2
#     if i == 6 or i == 10:
#         continue #continue for loop even i=6 until end of the range
#     print("Still inside for loop", i)
    
# print("Outside for loop.", i)



#### QUIZ 

for i in range (20): # range(2,10,2) = range(start, end, incrementvalue). i start at 2 end at 10, but increment for every number is 2
    if i == 6 or i%2 > 0:
        continue #continue for loop even i=6 until end of the range
    print("Still inside for loop", i)
    
print("Outside for loop.", i)