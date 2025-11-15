import random
print("""
 _                                             
( )                                            
| |__    _ _  ___    __   ___ ___    _ _  ___  
|  _  \/ _  )  _  \/ _  \  _   _  \/ _  )  _  \\
| | | | (_| | ( ) | (_) | ( ) ( ) | (_| | ( ) |
(_) (_)\__ _)_) (_)\__  |_) (_) (_)\__ _)_) (_)
                  ( )_) |                      
                   \___/                 

""")

notfound_counter = 0
words = [
    "apple", "banana", "cherry", "date",
    "grape", "orange", "lemon", "mango", "peach", "pear",
    "plum", "kiwi", "melon", "apricot"
]
choice_word = random.choice(words)
correct_guesses = []
for i in choice_word:
    print("_ ",end='')

while notfound_counter<=6:
    print()
    choose_char = input("\nChoose a character: ");
    print()
    if choose_char in choice_word and choose_char not in correct_guesses:
        correct_guesses.append(choose_char)

    for i in choice_word:
        if i in correct_guesses:
            print(i, end=' ')
        else:
            print("_ ",end='')
    print()

    if choose_char not in choice_word:
        print("Incorrect choice!")
        print("")
        notfound_counter = notfound_counter + 1
        print()
        if notfound_counter == 1:
            print(" |-----|")
            print(" |     |")
            print(" |   /---\\")
            print(" |  |     |")
            print(" |   \\---/")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("---")

        elif notfound_counter == 2:
            print(" |-----|")
            print(" |     |")
            print(" |   /---\\")
            print(" |  |     |")
            print(" |   \\---/")
            print(" |     |")
            print(" |     |")
            print(" |     |")
            print(" |     |")
            print(" |     |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("---")

        if notfound_counter == 3:
            print(" |-----|")
            print(" |     |")
            print(" |   /---\\")
            print(" |  |     |")
            print(" |   \\---/")
            print(" |     |")
            print(" |     |")
            print(" |     |")
            print(" |     |")
            print(" |     |")
            print(" |    |")
            print(" |   |")
            print(" |  |")
            print(" | |")
            print("---")

        elif notfound_counter == 4:
            print(" |-----|")
            print(" |     |")
            print(" |   /---\\")
            print(" |  |     |")
            print(" |   \\---/")
            print(" |     |")
            print(" |     |")
            print(" |     |")
            print(" |     |")
            print(" |     |")
            print(" |    | |")
            print(" |   |   |")
            print(" |  |     |")
            print(" | |       |")
            print("---")

        elif notfound_counter == 5:
            print(" |-----|")
            print(" |     |")
            print(" |   /---\\")
            print(" |  |     |")
            print(" |   \\---/")
            print(" |    /|")
            print(" |   / |")
            print(" |  /  |")
            print(" | /   |")
            print(" |     |")
            print(" |    | |")
            print(" |   |   |")
            print(" |  |     |")
            print(" | |       |")
            print("---")

        elif notfound_counter == 6:
            print(" |-----|")
            print(" |     |")
            print(" |   /---\\")
            print(" |  |     |")
            print(" |   \\---/")
            print(" |    /|\\")
            print(" |   / | \\")
            print(" |  /  |  \\")
            print(" | /   |   \\")
            print(" |     |")
            print(" |    | |")
            print(" |   |   |")
            print(" |  |     |")
            print(" | |       |")
            print("---")
        
        
    guessed_all = True
    for char in choice_word:
        if char not in correct_guesses:
            guessed_all = False
            break

    if guessed_all == True:
        print("\nCongratulations! You guessed the word:", choice_word)
        break
        
if notfound_counter == 6:

    print("Game Over!")
