# #Task 2.1
# word_list = []
# while True:
#     word = input("Enter a word containing at least 5 letters: ")
#     if len(word) < 5:
#         print("Length of word must be at least 5. ")
#     if word.isalpha() = False:
#         print("Word must contain only alphabetic letters. ")
#     if len(word) >= 5 and word.isalpha():
#         word_list.append(word)
#         break

#Task2.2
# word_list = []
# while True:
    
#     while True:
#         word = input("Enter a word containing at least 5 letters: ")
#         if len(word) < 5:
#             print("Length of word must be at least 5. ")
#         if word.isalpha() == False:
#             print("Word must contain only alphabetic letters. ")
#         if len(word) >= 5 and word.isalpha():
#             word_list.append(word)
#             break
#     more = input("Would you like to add another word(Y/N): ")
#     if more == "N":
#         break

#Task 2.3
# vowel_count = {'a': 0 , 'e': 0, 'i': 0, 'o': 0, 'u': 0}
# word_list = []
# while True:
    
#     while True:
#         word = input("Enter a word containing at least 5 letters: ")
#         if len(word) < 5:
#             print("Length of word must be at least 5. ")
#         if word.isalpha() == False:
#             print("Word must contain only alphabetic letters. ")
#         if len(word) >= 5 and word.isalpha():
#             word_list.append(word)
#             break
#     more = input("Would you like to add another word(Y/N): ")
#     if more == "N":
#         break

# for word1 in word_list:
#     for letter in word1:
#         if letter in vowel_count:
#             vowel_count[letter] = vowel_count[letter] + 1

# print(vowel_count)
# for vowel in vowel_count:
#     print(f"{vowel} appeared {vowel_count[vowel]} times. ")


#Task 3
# valid = 0
# invalid = 0 #1, start from 0

# print("Welcome to the Email Validator!")
# print("Type 'exit' to quit the program.\n")

# while True: #2, add :
#     email = input("Enter an email address: ").strip()

#     if email.lower() == "exit": #3, add ()
#         break #10, should break

#     if len(email) < 10: #4, change to <
#         print("Email is too short.\n")
#         invalid += 1
#         continue

#     at_index = email.find("@") #5, change to =

#     if at_index == -1 or email.find("@", at_index + 1) != -1:
#         print("Email must contain exactly one '@' symbol.\n")
#         invalid += 1
#         continue

#     if at_index == 0 or at_index == len(email) - 1: #8, add brackets for len
#         print("'@' cannot be at the start or end of the email.\n")
#         invalid += 1
#         continue

#     dot_index = email.find(".", at_index + 1)

#     if dot_index == -1 or dot_index == at_index + 1:
#         print("There must be a '.' after the '@' symbol, and not immediately after it.\n")
#         invalid += 1 #6, change to 1
#         continue

#     print("Valid Email!\n")
#     valid += 1 #9, change to valid


# print("\nTotal valid emails entered: ", valid) #7, add )
# print("Total invalid emails entered: ", invalid)

#Task 4

weather_data = [
    [30.0, 8.0, "No Rain"],
    [29.0, 12.0, "No Rain"],
    [27.0, 18.0, "Rain"],
    [25.0, 22.0, "Rain"],
    [32.0, 6.0, "No Rain"],
    [26.0, 16.0, "Rain"],
    [31.0, 10.0, "No Rain"],
    [28.0, 20.0, "Rain"]
]

def calculate_distance(temp1, wind1, temp2, wind2):
    distance = ((temp1 - temp2)**2 + (wind1 - wind2)**2)**0.5
    return distance

def find_nearest(distance_list):
    smallest = distance_list[0]
    smallest_index = 0
    for i in range(len(distance_list)):
        if distance_list[i] < smallest:
            smallest = distance_list[i]
            smallest_index = i
    return smallest_index

def predict_rain(current_temp, current_wind_speed, weather_data):
    distances = []
    for data in weather_data:
        distances.append(calculate_distance(current_temp, current_wind_speed, data[0], data[1]))
    return((weather_data[find_nearest(distances)])[2])

prediction_records = []
while True:
    current_temperature = float(input("Enter the current temperature: "))
    current_wind = float(input("Enter the current wind speed: "))
    prediction = predict_rain(current_temperature, current_wind, weather_data)
    print(f"The prediction is: {prediction}.")
    prediction_records.append([current_temperature, current_wind, prediction])

    another = input("Is another prediction required(Y/N): ").upper()
    if another == "N":
        break
with open("weather_predictions.txt", "w") as file:
    for prediction in prediction_records:
        file.write(prediction[2] + "\n")