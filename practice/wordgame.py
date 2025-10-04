while True:
    word = input("Player 1, enter a word: ").lower() #for player 1 to enter a code
    if len(word) > 10:
        print("cannot be more than 10")
    else:
        break

print(f"Player 1's word contains {len(word)} letters")
for i in range(10):
    letter = input("Player 2, guess a letter. ").lower()
    if letter in word:
        counter = 1
        for i in word:
            if letter != i:
                counter += 1
            else:
                print(f"{letter} is letter number {counter} in the word")
    else:
        print("This letter is not in the word")
print("You have entered 10 letters. ")
guess = input("Enter player 1's word. ").lower()
if guess == word:
    print("That is the correct word. You win!")
else:
    print("That is not the correct word. PLayer 1 wins!")
