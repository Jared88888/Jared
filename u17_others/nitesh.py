#question 1

# namelist = []
# while True:
#     new = input("Enter a new name ('X' to quit): ")
#     if new == "X":
#         break
#     else:
#         namelist.append[new]

# j = 1
# for i in namelist:
#     print(f"{j} {i}")
#     j += 1



#question 2 and 3
#classlist = ["Ben", "Dino", "Ethan", "Ivan", "Navan", "Shion"]

# change = input("Enter name to change: ")
# changed = input("Enter new name: ")

# position = classlist.index(change)  
# classlist[position] = changed

# remove = input("Enter name to remove: ")
# classlist.remove(remove)

# j = 1
# for i in classlist:
#     print(f"{j} {i}")
#     j += 1



#question 4
# students = ['Vani','Ethan','Jay']
# weightlist = []
# heightlist = []
# BMIlist = []
# n = 0
# for i in range (len(students)):
#     print(f"Enter data for {students[n]}")
#     weight = int(input("Enter weight in kg: "))
#     weightlist.append(weight)
#     height = float(input("Enter height in m: "))
#     heightlist.append(height)
#     BMI = weight / height **2
#     BMIlist.append(BMI)
#     n += 1

# j = 0
# for i in range (len(students)):
#     print(f"{students[j]} is {weightlist[j]} {heightlist[j]} with a BMI {BMIlist[j]}")
#     if BMIlist[j] > 30:
#         print(f"{students[j]} is obese")
#     j += 1