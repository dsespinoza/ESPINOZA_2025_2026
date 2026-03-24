students = []

for i in range(3):
    dictionary= {}
    dictionary["Name"]= input("Enter name: ")
    dictionary["Age"]= input("Enter age: ")
    dictionary["Grade"]= input("Enter grade: ")
    print("\n")
    students.append(dictionary)


print("Class Directory: ")
for i in students:
    print("", i["Name"], "| Age:", i["Age"],"| Grade:", i["Grade"])