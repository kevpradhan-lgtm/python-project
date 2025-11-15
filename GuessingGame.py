import random
logo="""
 ━━━━━━━━━━━━┏┓━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━┃┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┏━┓━┏┓┏┓┏┓┏┓┃┗━┓┏━━┓┏━┓━━━━┏━━┓┏┓┏┓┏━━┓┏━━┓┏━━┓┏┓┏━┓━┏━━┓━━━━┏━━┓┏━━┓━┏┓┏┓┏━━┓
┃┏┓┓┃┃┃┃┃┗┛┃┃┏┓┃┃┏┓┃┃┏┛━━━━┃┏┓┃┃┃┃┃┃┏┓┃┃━━┫┃━━┫┣┫┃┏┓┓┃┏┓┃━━━━┃┏┓┃┗━┓┃━┃┗┛┃┃┏┓┃
┃┃┃┃┃┗┛┃┃┃┃┃┃┗┛┃┃┃━┫┃┃━━━━━┃┗┛┃┃┗┛┃┃┃━┫┣━━┃┣━━┃┃┃┃┃┃┃┃┗┛┃━━━━┃┗┛┃┃┗┛┗┓┃┃┃┃┃┃━┫
┗┛┗┛┗━━┛┗┻┻┛┗━━┛┗━━┛┗┛━━━━━┗━┓┃┗━━┛┗━━┛┗━━┛┗━━┛┗┛┗┛┗┛┗━┓┃━━━━┗━┓┃┗━━━┛┗┻┻┛┗━━┛
━━━━━━━━━━━━━━━━━━━━━━━━━━━┏━┛┃━━━━━━━━━━━━━━━━━━━━━━┏━┛┃━━━━┏━┛┃━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━┗━━┛━━━━━━━━━━━━━━━━━━━━━━┗━━┛━━━━┗━━┛━━━━━━━━━━━━━
 """
def guessing_game(easy_difficult, attempts, number_guessed):
    if easy_difficult == "easy":
        chance = 10
    elif easy_difficult == "difficult":
        chance = 5
    while chance > 0:
        Guess=int(input("Make a guess:"))
        attempts += 1
        if Guess==number_guessed:
                print("Congratulations! you guessed correct number")
                print(f"You took {attempts} attempts to guess the number.")
                return 0
        else:
                chance-=1
                print(f"you are left with {chance} chances")
print(logo)
attempts=0
print("Welcome to the Number Guessing Gmae!")
print("I'm thinking of a number between 1 and 10.")
# label: tryagain
easy_difficult=input("Choose a dificulty. Type 'easy' or 'difficult'").lower()
number_guessed=random.choice(range(10))
print("Computer's guess : ",number_guessed)
 
if easy_difficult == "easy":
    guessing_game(easy_difficult, attempts, number_guessed)
elif easy_difficult == "difficult":
    guessing_game(easy_difficult, attempts, number_guessed)
else:
    print("Invalid input, type easy or difficult")

    # goto tryagain
