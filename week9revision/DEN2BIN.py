
# Task 3
# The following program should read a denary non-negative integer from the user. 
# The program will then convert the denary integer to its 
#    binary value and print it to the screen. 
# The “division by 2” method is employed to carry out the conversion. 
# There are several syntax errors and logical errors in the program.

NEW_BASE = 2 #1, use = #4, change to 2
num = input("Enter a non-negative integer: ") #2, use i, add )
num = int(num) #8, use int
result = ""
q = num
r = q % NEW_BASE
result = str(r) + result
q = q // NEW_BASE

while q > 0: #3, add :
    r = q % NEW_BASE
    result = str(r) + result #7, swap pos
    q = q // NEW_BASE #6, use floor divide
print(num, "in Decimal is", result, "in Binary.") #5, swap result and num #9, remove indent
    
# Open the file D2B.py
# Save the file as MYD2B___
# 
# Identify and correct the errors in the program so that it 
# works correctly according to the description above. Save your program.
#  [10] 
