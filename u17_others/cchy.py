# Exercise 1
# Task 1a
# You are to create a database of employees for a company. 
# Save your program as “employeeDB_Task1a1b”.

# The information you need to store is:

# Data needed	Variable name	Data type
# Name of staff	staff	String
# Department	dept	String
# Years served	years	integer

# You are to ask the user to key in the above information of a staff member. 
# Continue to get input until the user wants to stop. 
# Each staff details will be stored using dictionary. 
# Then store the database in a list.

# Sample
# 	Staff	dept	years
# Record 1	Wong	ICT	28
# Record 2	Tan	Math	15
# Record 3	Khoo	Sci	4


# Staff 1 
# Name: WONG 
# Dept: ICT 
# Years served: 28 

# Staff 2 
# Name: TAN 
# Dept: Math 
# Years served: 15 

# Staff 3 
# Name: KHOO 
# Dept: Sci 
# Years served: 4 


# At the end of all input, write a function “staffListing()”  
# to display the output of all the staff.
staff = [] 
i = 0
def staffListing(): 
    # i = 0  
    global i
    for thisstaff in staff:
        print(f"Staff {i+1}")
        print(f"Name: {name}")
        print(f"Department: {dept}")
        print(f"Years served: {years}")
        print()
        i += 1


while True: 
    employee = {}
    name = input("Enter the staff name: ") 
    dept = input("Enter the department: ") 
    years = int(input("Enter the number of years: ")) 
   
    employee["Name"] = name
    employee["Department"] = dept
    employee["Years"] = years
    # staff.append(staffnum)
    staff.append(employee)

    proceed = input("Want to continue (y/n)?")
    if proceed.lower() == "n":
        break

[ {"Name":"David","Department":"IT", "YearsWorked":5}, {"Name":"Mary","Department":"Finance", "YearsWorked":47} ]
staffListing()
###########################################
# Task 1b

# Continue to edit your program in task 1a.

# You are to ask user to search for a staff name.
# Output “Not our employee” if the staff name does not appear in the database. Continue to ask the user to search for another staff until the user indicates to stop searching.

# Output “Yes our employee” if the staff name appears in the database. 


while True:
    staffname = input("Type a name to search: ")
    found = False

    for thisstaff in staff:
        if staffname.lower() == thisstaff["StaffName"].lower():
            found = True
            break
    
    if found:
        print("Yes our employee.")
    else:
        print("Not our employee.")

    searchagain = input("Continue to search? (y/n)? ")
    if searchagain.lower() == 'n':
        break

##########################################################
# Task 1c
# Save your program as “employeeDB_Task1c”.
# If the user searching for a staff name exists in the database, ask user to update or delete the staff record.
# Update or delete accordingly.
# Continue to ask the user to search for another staff until the user indicates to stop searching.