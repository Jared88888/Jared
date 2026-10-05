# total = 0
# highest = 0
# lowest = 999
# numDays = int(input("Enter number of days: "))
# for i in range(numDays):
#     for j in range(3):
#         psi = int(input("Enter PSI: "))
#         if psi > 300:
#             print("Hazardous")
#         elif psi >= 201 and psi <=300:
#             print("Very unhealthy")
#         elif psi >= 101 and psi <= 200:
#             print("Unhealthy")
#         else:
#             print("Ok")

#         total += psi
#         if psi < lowest:
#             lowest = psi
#         if psi > highest:
#             highest = psi
# average = total / (numDays * 3)

psilist = []

numDays = int(input("Enter number of days: "))

for i in range(numDays):
    for j in range(3):
        psi = int(input("Enter PSI: "))
        if psi > 300:
            print("Hazardous")
        elif psi > 200:
            print("Very unhealthy")
        elif psi > 100:
            print("Unhealthy")
        else:
            print("OK")
        psilist.append(psi)

highest = max(psilist)
lowest = min(psilist)
average = sum(psilist) / len(psilist)

print(f"Highest PSI is {highest}")
print(f"Lowest PSI is {lowest}")
print(f"Average PSI is {round(average, 2)}")

with open("psiTable.txt", "w") as file:
    count = 1
    readings = ""
    for psi in psilist:
        readings = readings + str(psi) + " "
        if count % 3 == 0:
            file.write(readings + "\n")
            readings = ""
        count += 1

# with open("psiTable.txt", "w") as fobj:

 

#     tempstr = ""

#     count = 1

#     for psi in psilist:

 

#         tempstr = tempstr + str(psi) + " "

#         # print(f"count {count} and [{tempstr}]") # uncomment to see what's happening

 

#         # go to a new line for every 3rd data point

#         if count %3 == 0 :

 

#             fobj.write(tempstr+"\n")

#             tempstr = ""

 

#         count += 1