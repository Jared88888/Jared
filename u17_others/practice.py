
# Scenario 1: Finding Gold, Silver, and Bronze in a 200m Sprint (Using a List)
# You cannot use any in-built functions to do this.

# A sports coach has recorded race completion times (in seconds) 
# for 15 athletes in a 200m sprint event. 
# The fastest times (lowest values) win the medals.

# - Identify the Gold, Silver, and Bronze medalists.
# - Print their times and their original positions in the list.

#Expected Output
# Gold Medalist: 19.5 seconds (Index: 12)
# Silver Medalist: 19.6 seconds (Index: 8)
# Bronze Medalist: 19.7 seconds (Index: 4)


# race_times = [20.4, 19.9, 21.3, 20.1, 19.7, 22.0, 21.8, 20.8, 
#               19.6, 23.5, 21.2, 22.5, 19.5, 20.6, 21.1]
# Write your code here
# gold = race_times[0]
# silver = race_times[0]
# bronze = race_times[0]


# for i in race_times:
 
#     if gold > i:  
#         bronze = silver  
#         silver = gold  
#         gold = i 

#     elif silver > i:  
#         bronze = silver  
#         silver = i

#     elif bronze > i:  
#         bronze = i

#         print(f"Gold is {gold}, silver is {silver}, bronze is {bronze}.")


#######################################################################

# # Scenario 2: Finding the Top 3 Scores in a Programming Competition (Using a List)
# # You cannot use any in-built functions to do this.

# # A coding competition ranks students based on their final scores. 
# # The top 3 highest scores win prizes.

# # - Identify the top 3 scores.
# # - Print their values and original positions in the list.

# # Expected output
# # 1st Place: 100 (Index: 12)
# # 2nd Place: 99 (Index: 11)
# # 3rd Place: 98 (Index: 4)


# # List of programming competition scores
# competition_scores = [95, 87, 92, 90, 98, 85, 88, 91, 96, 89, 94, 99, 100, 97, 93]
# # Write your code here







# #######################################################################
# # Scenario 3: Identifying the Top 3 Best-Selling Products (Using a Dictionary)
# # You cannot use any in-built functions to do this.
# # A retail company tracks monthly sales for different products.

# # - Identify the 3 best-selling products based on the number of units sold.
# # - print the position and the units sold

# # Expected output
# # 1st Best-Selling Product: Smartphone (230 units sold)
# # 2nd Best-Selling Product: Headphones (210 units sold)
# # 3rd Best-Selling Product: Smartwatch (190 units sold)


# # Dictionary of product sales data (units sold)
# sales_data = {
#     'Laptop': 150, 'Smartphone': 230, 'Tablet': 180, 'Monitor': 170, 
#     'Keyboard': 140, 'Mouse': 130, 'Headphones': 210, 'Smartwatch': 190, 
#     'Printer': 120, 'Camera': 160
# }
# # Write your code here







# #######################################################################
# # Scenario 4: Identifying the Top 3 Swimmers in a National Championship 
# # You cannot use any in-built functions to do this.

# # A swimming competition ranks athletes based on their 
# # 100m freestyle times (in seconds). 

# # The fastest times (lowest values) win.
# # - Identify the top 3 fastest swimmers and their swim time.

# #Expected output
# # 1st Place: Caeleb (46.9 seconds)
# # 2nd Place: Florent (47.5 seconds)
# # 3rd Place: Michael (47.8 seconds)

# # Dictionary of swimmers' 100m freestyle times (lower times are better)
# swimming_times = {
#     'Michael': 47.8, 'Ryan': 48.2, 'Joseph': 49.5, 'Nathan': 48.0, 
#     'Kyle': 47.9, 'Caeleb': 46.9, 'Bruno': 48.7, 'Chad': 49.1, 'Florent': 47.5
# }
# # Write your code here







# #######################################################################
# # Scenario 5: Finding the Top 3 Most Expensive Cars 
# # You cannot use any in-built functions to do this.

# # A luxury car dealership wants to identify the three 
# # most expensive cars in their inventory.
# # Extract the top 3 highest-priced cars and their price

# # expected output
# # 1st Most Expensive Car: Bugatti Chiron ($3000000)
# # 2nd Most Expensive Car: Ferrari SF90 ($625000)
# # 3rd Most Expensive Car: Lamborghini Aventador ($507000)


# # Dictionary of car prices
# car_prices = {
#     'Ferrari SF90': 625000, 'Lamborghini Aventador': 507000, 'Porsche 911 GT3': 200000,
#     'McLaren 720S': 315000, 'Rolls Royce Ghost': 345000, 'Bugatti Chiron': 3000000,
#     'Aston Martin DBS': 316000, 'Bentley Continental GT': 250000, 'Maserati MC20': 230000
# }
# Write your code here






###################################################################

##################################
# Assignment
# Scenario: Identifying Star Students for an Award Ceremony
    
# Your school is preparing for the end-of-year award ceremony.
# The principal wants to recognise "Star Students" — those who have shown:
# - Excellent attendance (at least 90%)
# - Strong academic performance (score of at least 85)

# You're given two separate dictionaries:
# - One with student attendance (in %)
# - One with student scores (out of 100)

# Extract the names of students who meet both criteria.
# (1) Store them in a list called star_students.
    
# (2) Loop through the star_students list and 
#      print a congratulatory message to each star student like this:
# "Congratulations Chloe Lim! With an attendance of 95% and a score of 92,
# you are awarded the Star Student Award!""

# You may assume that the same keys exist in both dictionaries.

attendance = {
    "Alex Tan": 92, "Benjamin Lee": 88, "Chloe Lim": 95,
    "Dana Ong": 87, "Ethan Raj": 91, "Farah Bte Ahmad": 94,
    "Gerald Chan": 78, "Hannah Goh": 85, "Ivan Wong": 96,
    "Jolene Ng": 93, "Kishore Menon": 70, "Liyana Yusof": 90
}

scores = {
    "Alex Tan": 84, "Benjamin Lee": 86, "Chloe Lim": 92,
    "Dana Ong": 81, "Ethan Raj": 89, "Farah Bte Ahmad": 90,
    "Gerald Chan": 65, "Hannah Goh": 88, "Ivan Wong": 93,
    "Jolene Ng": 79, "Kishore Menon": 72, "Liyana Yusof": 85
}

star_students = []
for student in attendance:
    if attendance[student] >= 90 and scores[student] >= 85:
        star_students.append(student)

for student in star_students:
    print(f"Congratulations {student}! With an attendance of {attendance[student]}% and a score of {scores[student]}, you are awarded the Star Student Award!")
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

# performance_scores = {
#     'Alice': 88, 'Benny': 75, 'Charlie': 92, 'David': 85,
#     'Emma': 78, 'Farah': 81, 'George': 66, 'Hassan': 94,
#     'Ivy': 71, 'Jack': 88, 'Liam': 45, 'Jessica': 98,
#     'Samir': 23, 'Jimmy': 5, 'Bryan': 78, 'Estelle': 9}

# # write your code here

