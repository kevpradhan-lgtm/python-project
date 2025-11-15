
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

def encrypt(word,shift_count,new_word_list):   
    for i in word:
        new_word_list.append(chr(ord(i) + shift_count))
    for j in new_word_list:
        print(str(j),end="")

def decrypt(word,shift_count,new_word_list):
    for i in word:
        new_word_list.append(chr(ord(i) - shift_count))
    for j in new_word_list:
        print(str(j),end="")
print(logo)
word = input("Enter a word : ")
new_word_list = []
print("1: Encrypt\n2: Decrypt\n")
choice = input("Enter your choice : ").capitalize()
shift_count = int(input("Enter the shift count : "))
if choice == "Encrypt":
    encrypt(word,shift_count,new_word_list)
elif choice == "Decrypt":
    decrypt(word,shift_count,new_word_list)


