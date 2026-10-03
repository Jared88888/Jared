def getgradepoint(mark):
    if mark >= 75 and mark <= 100:
        return 1
    elif mark >= 70 and mark <= 74:
        return 2
    elif mark >= 65 and mark <= 69:
        return 3
    elif mark >= 60 and mark <= 64:
        return 4
    elif mark >= 55 and mark <= 59:
        return 5
    elif mark >= 50 and mark <= 54:
        return 6
    elif mark >= 45 and mark <= 49:
        return 7
    elif mark >= 40 and mark <= 44:
        return 8
    else:
        return 9

def L1R5(result):
    L1R5 = 0
    dictwithgrade = {}
    for subject in result:
        dictwithgrade[subject] = getgradepoint(result[subject])
    if dictwithgrade["English"] < dictwithgrade["Higher Chinese"]:
        L1R5 += dictwithgrade["English"]
    else:
        L1R5 += dictwithgrade["Higher Chinese"]
    for subject1 in dictwithgrade:
        if subject1 != "English" and subject1 != "Higher Chinese":
            L1R5 += dictwithgrade[subject1]
    return L1R5

# print(L1R5({"English":71, "Higher Chinese":50, "Chemistry":65, "Geography":87, "Mathematics":43, "Physics":58,"Computing":69}))

grades = {}
for i in range(7):
    subject = input("Enter subject: ")
    while True:
        score = int(input("Enter a valid number from 0 to 100: "))
        if score >= 0 and score <= 100:
            grades[subject] = score
            break
print(L1R5(grades))

scoredict = {1:"A1", 2:"A2", 3:"B3", 4:"B4", 5:"C5", 6:"C6", 7:"D7", 8:"E8", 9:"F9"}
with open("resultslip.txt" ,"w") as file:
    for subject2 in grades:
        file.write(f"{subject2}: {grades[subject2]}({scoredict[getgradepoint(grades[subject2])]}) \n")
    file.write(f"Computed L1R5: {L1R5(grades)}")
        