def split_sentence(word_string):
    list_sentence = word_string.split()
    return list_sentence

def check_list(word, word_string):
    if word in split_sentence(word_string): #use previous function split, check if inside list
        return "Yes"
    else:
        return "No"
    
def reverse_sentence(word_string):
    new_sentence = "" #create variable to add to later on
    for i in split_sentence(word_string): #loop through
        new_sentence = i + new_sentence #keep adding to front
    return new_sentence

string_of_words = input("Enter a string of words: ") #ask user for string of words
word_to_search = input("Enter word you would like to search: ") #ask user for word
print(split_sentence(string_of_words)) #split the string
print(reverse_sentence(string_of_words)) #reverse the string
if check_list(word_to_search, string_of_words) == "Yes": #if word is present
    print("The word is found in the string of words. ") #output that it is found
else:
    print("The word is not found in the string of words. ") #else output that it is not found