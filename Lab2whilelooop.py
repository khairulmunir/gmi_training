x = int(input("Enter any number: "))

#Initilize the initial value, set to 0 before counting
oddNumber =  0 
evenNumber = 0

#In this while loop, user input any number that is not zero. When number entered it is divide by 2 first. If no balance (=0), it is even. Then evenNumber += 1 means increase 1 
while x != 0:
    # print("I am in while loop")
    # x = int(input("Enter any number to exit the loop: "))
    
    if x%2 == 0:
        evenNumber += 1
        
    else:
        oddNumber += 1
    
    x = int(input("Enter 0 if you want to exit the loop. Else, keep entering any number: "))
    
    
print("Even number count = ", evenNumber)
print("Odd number count = ", oddNumber)
    