#original buggy code
# name_list = []
# mark_list = []
# dist_list = []
# pass_list = []
# fail_list = []
# count = 1

# flag = True
# while flag == False:
#     name = input('Enter student's name: ')
#     name_list += [name]
#     while True:
#         mark = int(input('Enter score of student: '))
#         if mark >= 0 or mark <= 100:
#             break
#         else:
#             print('Invalid mark!')
#         mark_list += [mark]
#     count += 1
#     if mark > 75:
#         dist_list += [name]
#     elif mark >= 50:
#         pass_list += [name]
#     else:
#         fail_list += (name)
#     more = int(input('Would you like to enter another score, Y or N?: '))
#     if more == 'N':
#         flag = False
# average = round(max(mark_list)/len(mark_list), 2)
# num_dist = len(dist_list)
# num_fail = len(fail_list)
# print("You entered " + count + " scores.")
# print(str(num_dist) + " students score distinction and " + str(num_fail) + " students failed.")
# print("Average score is " + str(average))


name_list = []
mark_list = []
dist_list = []
pass_list = []
fail_list = []
count = 0 #6, start from 0

flag = True
while flag == True: #1, change to true
    name = input("Enter student's name: ") #2, change to ""
    name_list += [name]
    while True:
        mark = int(input('Enter score of student: '))
        if mark >= 0 and mark <= 100: #8 use and
            break
        else:
            print('Invalid mark!')
    mark_list += [mark] #4, remove indent
    count += 1
    if mark >= 75: #3, change to >=
        dist_list += [name]
    elif mark >= 50:
        pass_list += [name]
    else:
        fail_list += [name] #10, change to square bracket
        print(fail_list)
    more = input('Would you like to enter another score, Y or N?: ') #5, remove int
    if more == 'N':
        flag = False
average = round(sum(mark_list)/len(mark_list), 2) #7, use sum 
num_dist = len(dist_list)
num_fail = len(fail_list)
print("You entered " + str(count) + " scores.") #9 change to str
print(str(num_dist) + " students score distinction and " + str(num_fail) + " students failed.")
print("Average score is " + str(average))