#this is the original buggy code
# students = False
# while students == True:
#     comp = input("Enter the Computing test score ")
#     math = int(input("Enter the Mathematics test score ))
#     joint_score = comp + comp
#     if comp > 100 and math > 100:
#         print("Student is awarded a gold award")
#     elif comp >= 100 and math >= 100 or joint_score >= 180:
#         print("Student is awarded a silver award")
#     elif comp >= 75 and math >= 75:
#         print("Student is awarded a bronze award")
#     else:
#         print("NO award this time, keep trying")
#     more_scores = input("Any more test scores to enter? Type 'Y' or 'N' ")
#     if More_scores == 'N':
#         students = True
#     else:
#         students = True

students = True #change to true
while students == True:
    comp = int(input("Enter the Computing test score ")) #change to int
    math = int(input("Enter the Mathematics test score: ")) #adding "
    joint_score = comp + math #changing comp to math
    if comp >= 100 and math >= 100: #change to >=
        print("Student is awarded a gold award")
    elif (comp >= 100 or math >= 100) and joint_score >= 180: #changing ands and ors #adding brackets
        print("Student is awarded a silver award")
    elif comp >= 75 and math >= 75:
        print("Student is awarded a bronze award")
    else:
        print("NO award this time, keep trying")
    more_scores = input("Any more test scores to enter? Type 'Y' or 'N' ").upper() #add .upper function
    if more_scores == 'N': #lower case 
        students = False #change to false
    else:
        students = True