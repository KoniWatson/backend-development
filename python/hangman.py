import random
from wonderwords import RandomWord

alphabet = [["a", "b", "c", "d"], ["e", "f", "g", "h"], ["i", "j", "k", "l"], ["m", "n", "o", "p"], ["q", "r", "s", "t"], ["u", "v", "w", "x"], ["y", "z", "", ""]]

r = RandomWord()
select_word = r.word()

allowed_turns = len(select_word) + 2
used_turns = 0

correct_chars = list(range(len(select_word)))
guessed_letters = ''

for char in select_word:
    print("_", end=" ")
print()

while used_turns < allowed_turns:
    used_turns += 1
    guess = input("\n\nGuess a character\n")

    for i, char in enumerate(select_word):
        if (char in guess):
            correct_chars[i] = char + " "
        elif (correct_chars[i] == "_ " or type(correct_chars[i]) == int):
            correct_chars[i] = "_ "

    for i in range(7):
        for j in range(4):
            if (alphabet[i][j] in ''.join(correct_chars)):
                print(alphabet[i][j] + '\u0336', end=" ")
            else:
                print(alphabet[i][j], end=" ")
        print()
    
    print("---------------------")
    print(''.join(correct_chars))

    if (''.join(correct_chars) == select_word):
        print("Whoop Whoop, That is right!")
        break
    elif (used_turns >= allowed_turns and ''.join(correct_chars) != select_word):
        print(f"Not quite right, the word was {select_word}")
        break