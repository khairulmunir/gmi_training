
# myVar = 20
# my_Var = "21"
# myFloat = 20.3

# # print("Enter any value below:")
# myInput = input("Enter any value: ")

# print(myVar)
# print(my_Var)
# print(myFloat)
# print(myVar, my_Var, myFloat, sep= "--")
# print(myVar*2, my_Var*3, sep="--") #string if time 3, will print 3 times
# print("Your Input:", myInput)
# print(f"Your Input is {myInput}")

print("BMI CALCULATOR")

height = float(input("Masukkan ketinggian anda dalam meter: ")) #reason using float/int because input is string so cannot do arithmetic operation
weight = float(input("Masukkan berat badan anda dalam kg: ")) #reason using float/int because input is string so cannot do arithmetic operation

bmi = weight/(height**2)

if bmi < 18.5:
    print("Berat anda kurang")
    
elif bmi >= 18.5 and bmi < 25:
    print("Berat anda normal")

elif bmi >= 25 and bmi < 40:
    print("Berat anda berlebihan")
    
else:
    print("Berat anda kategori Obese")
    
print("BMI anda ialah: ", round(bmi, 1)) 