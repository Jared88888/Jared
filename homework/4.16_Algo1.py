###############################################################
# Scenario: Employee Performance Review

# Finding Maximum, Minimum, and Average Performance Scores 
# Without Built-in Functions
# YOU CANNOT USE ANY PYTHON INBUILT FUNCTIONS TO DO THIS.

# A company conducts annual performance reviews for employees. 
# Each employee is given a performance score out of 100. 
# The HR department wants to:

# - Identify the top-performing employee (highest score).
# - Identify the lowest-performing employee (lowest score).
# - Calculate the average performance score, rounded to 2 decimal places.
# - Identify underperforming employees (those with scores below 50) 
#    -> save them into another dictionary called non_performers.
#   and print a performance warning message to all of these employees.

performance_scores = {
    'Alice': 88, 'Benny': 75, 'Charlie': 92, 'David': 85,
    'Emma': 78, 'Farah': 81, 'George': 66, 'Hassan': 94,
    'Ivy': 71, 'Jack': 88, 'Liam': 45, 'Jessica': 98,
    'Samir': 23, 'Jimmy': 5, 'Bryan': 78, 'Estelle': 9}

# write your code here

highest = 0
highest_name = ""
lowest = 1234567890
lowest_name = ""
total = 0
non_performers = {}
num_of_employees = 0
for score in performance_scores:
    if performance_scores[score] > highest:
        highest_name = score
        highest = performance_scores[score]

    if performance_scores[score] < lowest:
        lowest_name = score
        lowest = performance_scores[score]

    total += performance_scores[score]

    if performance_scores[score] < 50:
        non_performers[score] = performance_scores[score]

    num_of_employees += 1

average = round(total/num_of_employees, 2)  

print(f"The highest performer is {highest_name} with a score of {highest}. ")
print(f"The lowest performer is {lowest_name} with a score of {lowest}. ")
print(f"The average rounded to 2 decimal places is {average}. ")
for i in non_performers:
    print(f"{i}, please do better. ")