# ########################################################
# # Question 3:
# # The student council organised a charity fundraising event. 
# # The amount collected from each class is stored in the dictionary below. 
# # Identify the class that raised the highest and lowest amounts. 
# # Print out the class names and their respective contribution amounts.
# ########################################################
# # donations = {
# #     'Class 1A': 320, 'Class 1B': 480, 'Class 1C': 290, 'Class 1D': 375,
# #     'Class 1G': 450, 'Class 1H': 530, 'Class 2C': 470, 'Class 3D': 310,
# #     'Class 4E': 415, 'Class 5F': 390
# # }
# # # Answer for Question 3 here

# # highestclass = ""
# # lowestclass = ""
# # highestdon = 0
# # lowestdon = 999999999999

# # for i in donations:
# #     if donations[i] > highestdon:
# #         highestdon = donations[i]
# #         highestclass = i
# #     if donations[i] < lowestdon:
# #         lowestdon = donations[i]
# #         lowestclass = i

# # print(f"{highestclass} {highestdon}")
# # print(f"{lowestclass} {lowestdon}")


# ################################
# ##################################################################
# # Question 5: 
# # Hourly temperature measurements (°C) for a specific day are given below. 
# # Write Python code to determine the highest and lowest temperatures, 
# # along with the corresponding hour of measurement. 
# # (First measurement at index 0 corresponds to midnight, 
# #  and each subsequent value is measured hourly.)

# # Find the average temperature for this day.
# ##################################################################
# hourly_temperatures = [26.4, 25.9, 25.1, 24.6, 24.2, 23.8, 24.5, 25.6, 
#                        27.3, 29.0, 30.5, 31.2, 32.0, 33.1, 32.8, 31.6,
#                        30.8, 29.4, 28.1, 27.5, 27.0, 26.8, 26.0, 25.7]
# # Answer for Question 5 here

# highesttemp = hourly_temperatures[0]
# lowesttemp = hourly_temperatures[0]

# counter = 0

# maxhour = 0
# minhour = 0
# for i in hourly_temperatures:
#     if i > highesttemp:
#         highesttemp = i
#         position = hourly_temperatures.index(i) 
#         maxhour = counter
#     if i < lowesttemp:
#         lowesttemp = i

#     counter += 1

# counterrrrr = 0
# for i in hourly_temperatures:
#     counterrrrr += i
# print(f"{highesttemp} {maxhour} 00")
# print(f"{lowesttemp} {minhour} 00")
# average = counterrrrr / len(hourly_temperatures)
# print(average)


conversion_factors = {
    "B": 1,
    "kB": 1000,
    "MB": 1000**2,
    "GB": 1000**3,
    "TB": 1000**4,
    "PB": 1000**5,
    "KiB": 1024,
    "MiB": 1024**2,
    "GiB": 1024**3,
    "TiB" : 1024**4,
    "PiB" : 1024**5
}

def is_valid_unit(unit): #MB
    if unit in conversion_factors:
        return True
    else:
        return True
    
print(is_valid_unit("MBB"))

# ________________________________________
# Task 4.3 – Conversion Function [7 marks]
# Write a function named convert_storage(value, from_unit, to_unit) that:
# •	Takes in three parameters:
# o	value (a numeric value to convert)
# o	from_unit (the current unit)
# o	to_unit (the target unit)
# •	Converts the value using the following steps:
# 1.	Multiply the value by the conversion factor of the source unit to get the number of bytes
# 2.	Divide the number of bytes by the conversion factor of the target unit to get the result
# •	Returns the final result as a float
# Use the conversion_factors dictionary for all conversions.
# Do not perform any user input or output in this function.
# Do not use if or elif statements to check unit names.
# This function must correctly handle:
# •	Conversion from a larger unit to a smaller unit (e.g. GB → MB)
# •	Conversion from a smaller unit to a larger unit (e.g. KiB → GiB)
def convert_storage(value, from_unit, to_unit):

    convert_to_bytes = value * conversion_factors[from_unit]
    convert_to_wanted = convert_to_bytes / conversion_factors[to_unit]
    print(convert_to_wanted)

convert_storage(5, "TB", "GB")

# # ________________________________________
# # Task 4.4 – User Interaction [8 marks]
# # Write the main program that:
# # •	Repeatedly prompts the user to input:
# # o	A numeric value
# # o	A source unit
# # o	A target unit
# # •	Validates that:
# # o	The numeric value is positive. 
# # o	Both units are supported using the is_valid_unit() function
# # •	Calls the convert_storage() function to perform the conversion
# # •	Displays the result to 4 decimal places, e.g.:
# # •	10 MB is approximately 9.5367 MiB
# # •	Asks the user whether they want to convert another value
# # o	If the user enters "yes", repeat the process
# # o	If the user enters "no", end the program

while True:
    
    while True:
        value = float(input("Enter a number to convert: "))

        if value > 0:
            print(f"{value} is valid")
            break
        else:
            print(f"{value} is not valid. Enter a positive number")

    while True:
        from_unit = input("Enter a unit to convert from: ")
        if is_valid_unit(from_unit):
            print(f"{from_unit} is valid.")
            to_unit = input("Enter a unit to convert: ")
            if is_valid_unit(to_unit):
                output_val = convert_storage(value, from_unit, to_unit)
                output_val = round(output_val, 4)

                print(f"{value} {from_unit} is {output_val} {to_unit}")
                break
            else:
                print(f"{to_unit} is not valid")

        else:
            print(f"{from_unit} is not valid. Try again")
    proceed = input("Do you want to continue(Y/N)? ")
    if proceed == "N":
        break