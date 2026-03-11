#this is the original code

import math

#### do not change this code
devices = {
    "523WR": ["Telmo",  "Speed23",  "PMD",     0.70, 1.10],
    "924MN": ["Lambo",  "Comfit1",  "PMD",     0.60, 1.15],
    "32XC" : ["Lambo",  "Zipline",  "Scooter", 0.35, 0.60],
    "A101X": ["Volt",   "Feather",  "Scooter", 0.32, 0.52],
    "D404Q": ["RoadMax","Urban",    "PMD",     0.66, 1.18],
}

print("Mobility Device Classifier (kNN, k = 1)")
print("Total devices loaded:", len(devices))
#### do not change this code

# Task 2.1 - Complete the function below
def distance2(p1x, p1y, p2x, p2y):
    # Task 2.1 – To be completed by student
    pass # remove this and replace with code.


# Task 2.2 - Complete the function below
def predict_type_2d(devices_dict, newdevice_width, newdevice_length):
    # Task 2.2 – To be completed by student
    pass # remove this and replace with code.

# --- main flow (to be refined by you) ---
# Students will add input validation and output formatting later

################
import math

#### do not change this code
devices = {
    "523WR": ["Telmo",  "Speed23",  "PMD",     0.70, 1.10],
    "924MN": ["Lambo",  "Comfit1",  "PMD",     0.60, 1.15],
    "32XC" : ["Lambo",  "Zipline",  "Scooter", 0.35, 0.60],
    "A101X": ["Volt",   "Feather",  "Scooter", 0.32, 0.52],
    "D404Q": ["RoadMax","Urban",    "PMD",     0.66, 1.18],
}

print("Mobility Device Classifier (kNN, k = 1)")
print("Total devices loaded:", len(devices))
#### do not change this code

# Task 2.1 - Complete the function below
def distance2(p1x, p1y, p2x, p2y):
    return math.sqrt( (p1x - p2x)**2 + (p1y - p2y)**2 )

print(distance2(2,3,4,5))
# Task 2.2 - Complete the function below
def predict_type_2d(devices_dict, newdevice_width, newdevice_length):
    shortest_value = 9999
    shortest_name = ""
    for key, value in devices_dict.items():
        if distance2(newdevice_length, newdevice_width, value[-1], value[-2]) < shortest_value:
            shortest_value = distance2(newdevice_length, newdevice_width, value[-1], value[-2])
            shortest_name = key
    return devices[shortest_name][2]
    
while True:
    length= float(input("Enter length: "))
    if length > 0:
        break

while True:
    width = float(input("Enter breadth: "))
    if width > 0:
        break

results = predict_type_2d(devices, width, length)
print(f"Predicted type: {results}")
# --- main flow (to be refined by you) ---
# Students will add input validation and output formatting later