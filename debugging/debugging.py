# #this is the original buggy code
# # students = False
# # while students == True:
# #     comp = input("Enter the Computing test score ")
# #     math = int(input("Enter the Mathematics test score ))
# #     joint_score = comp + comp
# #     if comp > 100 and math > 100:
# #         print("Student is awarded a gold award")
# #     elif comp >= 100 and math >= 100 or joint_score >= 180:
# #         print("Student is awarded a silver award")
# #     elif comp >= 75 and math >= 75:
# #         print("Student is awarded a bronze award")
# #     else:
# #         print("NO award this time, keep trying")
# #     more_scores = input("Any more test scores to enter? Type 'Y' or 'N' ")
# #     if More_scores == 'N':
# #         students = True
# #     else:
# #         students = True

# students = True #change to true
# while students == True:
#     comp = int(input("Enter the Computing test score ")) #change to int
#     math = int(input("Enter the Mathematics test score: ")) #adding "
#     joint_score = comp + math #changing comp to math
#     if comp >= 100 and math >= 100: #change to >=
#         print("Student is awarded a gold award")
#     elif (comp >= 100 or math >= 100) and joint_score >= 180: #changing ands and ors #adding brackets
#         print("Student is awarded a silver award")
#     elif comp >= 75 and math >= 75:
#         print("Student is awarded a bronze award")
#     else:
#         print("NO award this time, keep trying")
#     more_scores = input("Any more test scores to enter? Type 'Y' or 'N' ").upper() #add .upper function
#     if more_scores == 'N': #lower case 
#         students = False #change to false
#     else:
#         students = True

#copy or original buggy code
# colour_list = ['red','green', 'blue','orange', 'purple','yellow']
# colour_to_find = input("Which colour would you like to search for? ")
# items = len(colour_to_find)
# item_number = 0
# colour_found = False
# while colour_found == True:
#     while item_number > items:
#         if colour_list[item_number] = colour_to_find
#             print("There are " + str(item) + " colours in the list, " + colour_to_find + " is item " + str(iten_number - 1) + " in the list.")
#             colour_found = True
#             item_number = item_number
#         elif item_number == items - 1:
#             print("The colour is not in the list. ")
#             colour_found = False
#             item_number = items
#         else:
#             item_number = items


colour_list = ['red','green', 'blue','orange', 'purple','yellow']
colour_to_find = input("Which colour would you like to search for? ")
items = len(colour_list) #change to find length of list
item_number = 0
colour_found = False
while colour_found == False: #set to false to start while loop
    while item_number < items: #change to less than
        if colour_list[item_number] == colour_to_find: #add == and :
            print("There are " + str(items) + " colours in the list, " + colour_to_find + " is item " + str(item_number + 1) + " in the list.") #change to items and item number #make it add 1 not minus 1
            colour_found = True
            item_number = items #make it to items #this breaks the loop
            
        elif item_number == items - 1: 
            print("The colour is not in the list. ")
            colour_found = True #change to true
            item_number = items
            
        else:
            item_number += 1 #make it increase by 1