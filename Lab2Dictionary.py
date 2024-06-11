myDict1 = {"FirstName":"Joe","LastName":"Biden"}
myDict2 = {"FirstName":"Alex","LastName":"Siong"}

detail = {
    "Person1": {"FirstName": "Umar","LastName": "Yusof"},
    "Person2": {"FirstName": "Lee","LastName": "Yong"}
}

print(myDict1)
print(myDict1["FirstName"])
print(myDict2["LastName"])
print(detail["Person1"]["FirstName"])

del myDict2["FirstName"] #will delete Firstname value
print(myDict2)

myDict2["FirstName"] = "Wee"
print(myDict2)

myDict2.update({"middleName":"Ka"})
print(myDict2)


combined_info = f"{myDict2['FirstName']} {myDict2['middleName']} {myDict2['LastName']}"
print(combined_info)