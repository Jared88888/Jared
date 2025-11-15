with open("FiveLetterWords.txt", "r") as fobj:
    contents = fobj.read()
    # print(contents)

listofwords = contents.split(",")

#choose random word
import random

correctword = listofwords[random.randint(0, 5757)]

#wordle strategy
one_vowel = []
two_vowel = []
three_vowel = []
four_vowel = []
five_vowel = []

vowels = ["a", "e", "i", "o", "u"]

for i in listofwords:
    vowel_count = 0
    for v in vowels:
        if v in i:
            vowel_count += 1
    if vowel_count == 1:
        one_vowel += [i]
    elif vowel_count == 2:
        two_vowel += [i]
    elif vowel_count == 3:
        three_vowel += [i]
    elif vowel_count == 4:
        four_vowel += [i]
    elif vowel_count == 5:
        five_vowel += [i]

print(four_vowel)


