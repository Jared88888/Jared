#task 2

# num_of_animals = 5
# animals = []
# player2score = 0
# while True:
#     p1_animal = input("Player 1, please enter an animal (Type discontinue if you want to stop): ")
#     p1_animal = p1_animal.lower()
#     if p1_animal == "discontinue":
#         break
#     animals.append(p1_animal)
    
# while True:
    
#     if len(animals) == 0:
#         print("Player 2 has guessed all animals")
#         break 

#     p2_guess = input("Player 2, please enter your guess: ")
#     p2_guess = p2_guess.lower()
 

#     if p2_guess not in animals:
#         print("Game over")
#         print(f"Your score is {player2score}")
#         print(animals)
#         break
    

#     if p2_guess in animals:
#         print(f"Player 2 has successfully guessed {p2_guess}")
#         animals.remove(p2_guess)
#         player2score += 1

    

#task 4

def split_sentence(word_string):
    list_sentence = word_string.split()
    return list_sentence

def check_list(word, sentence):
    if word in split_sentence(sentence):
        return "Yes"
    else:
        return "No"

def reverse_sentence(sentencee):
    return split_sentence(sentencee)[::-1]



