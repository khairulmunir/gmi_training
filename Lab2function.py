# #function - same routine called use many times

# def message():
#     print("Test function")

# message()  

# def message1(number=100):
#     print("Test function lagi", number)
    
# message1(10)
# message1(20)
# message1(30)
# message1()


### Method ni just print sahaja value bmi but tak store dalam mana-mana variable
# def bmi(weight, height):
#     bmi_Value  = weight/height**2
#     print("Your BMI is", round(bmi_Value, 1))
    
# bmi(61, 1.69) #positional paramater OR
# bmi(height=1.78, weight=65) #keyword argument passing

def bmi(weight, height):
    bmi_Value  = weight/height**2
    return bmi_Value

#valFun = bmi(61, 1.7) #Cara direct
valFun = bmi((float(input("Berat:"))), (float(input("Tinggi dalam meter:")))) #result of bmi stored in variable valFun, cara lebih flex untuk user masukkan data

#valFun += 2 #add 2 to valFun
print(valFun)