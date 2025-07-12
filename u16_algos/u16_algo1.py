########################################################
# Question 3:
# The student council organised a charity fundraising event. 
# The amount collected from each class is stored in the dictionary below. 
# Identify the class that raised the highest and lowest amounts. 
# Print out the class names and their respective contribution amounts.
########################################################
# donations = {
#     'Class 1A': 320, 'Class 1B': 480, 'Class 1C': 290, 'Class 1D': 375,
#     'Class 1G': 450, 'Class 1H': 530, 'Class 2C': 470, 'Class 3D': 310,
#     'Class 4E': 415, 'Class 5F': 390
# }
# # Answer for Question 3 here

# highestclass = ""
# lowestclass = ""
# highestdon = 0
# lowestdon = 999999999999

# for i in donations:
#     if donations[i] > highestdon:
#         highestdon = donations[i]
#         highestclass = i
#     if donations[i] < lowestdon:
#         lowestdon = donations[i]
#         lowestclass = i

# print(f"{highestclass} {highestdon}")
# print(f"{lowestclass} {lowestdon}")


################################
##################################################################
# Question 5: 
# Hourly temperature measurements (°C) for a specific day are given below. 
# Write Python code to determine the highest and lowest temperatures, 
# along with the corresponding hour of measurement. 
# (First measurement at index 0 corresponds to midnight, 
#  and each subsequent value is measured hourly.)

# Find the average temperature for this day.
##################################################################
hourly_temperatures = [26.4, 25.9, 25.1, 24.6, 24.2, 23.8, 24.5, 25.6, 
                       27.3, 29.0, 30.5, 31.2, 32.0, 33.1, 32.8, 31.6,
                       30.8, 29.4, 28.1, 27.5, 27.0, 26.8, 26.0, 25.7]
# Answer for Question 5 here

highesttemp = hourly_temperatures[0]
lowesttemp = hourly_temperatures[0]

counter = 0

maxhour = 0
minhour = 0
for i in hourly_temperatures:
    if i > highesttemp:
        highesttemp = i
        position = hourly_temperatures.index(i) 
        maxhour = counter
    if i < lowesttemp:
        lowesttemp = i

    counter += 1

counterrrrr = 0
for i in hourly_temperatures:
    counterrrrr += i
print(f"{highesttemp} {maxhour} 00")
print(f"{lowesttemp} {minhour} 00")
average = counterrrrr / len(hourly_temperatures)
print(average)