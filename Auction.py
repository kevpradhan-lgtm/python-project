import os
logo = '''
  _______ _             _____ _ _            _                        _   _             
 |__   __| |           / ____(_) |          | |       /\             | | (_)            
    | |  | |__   ___  | (___  _| | ___ _ __ | |_     /  \  _   _  ___| |_ _  ___  _ __  
    | |  | '_ \ / _ \  \___ \| | |/ _ \ '_ \| __|   / /\ \| | | |/ __| __| |/ _ \| '_ \ 
    | |  | | | |  __/  ____) | | |  __/ | | | |_   / ____ \ |_| | (__| |_| | (_) | | | |
    |_|  |_| |_|\___| |_____/|_|_|\___|_| |_|\__| /_/    \_\__,_|\___|\__|_|\___/|_| |_|                                                                                        
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
permission = "yes"
empty_dictionary={}

while permission=="yes":
    print("Welcome to the secret auction program.")
    name = input("What is your name?: ")
    bids = int(input("What's your bid?: $"))
    empty_dictionary[name] = bids
    permission=input("Are there any other bidders? Type 'yes or 'no").lower()
    if permission=="yes":
     os.system('cls')

max_bid=0
winner = ""
for name, bid in empty_dictionary.items():
    if bid > max_bid:
        max_bid = bid
        winner = name
 

print(f"The winner is {winner} with a bid of ${max_bid}")
