print("""
                                                                                                         
                                                                                                         
                        ,--,                             ,--,                  ___                       
                      ,--.'|                           ,--.'|                ,--.'|_                     
                      |  | :                      ,--, |  | :                |  | :,'   ,---.    __  ,-. 
                      :  : '                    ,'_ /| :  : '                :  : ' :  '   ,'\ ,' ,'/ /| 
   ,---.     ,--.--.  |  ' |      ,---.    .--. |  | : |  ' |     ,--.--.  .;__,'  /  /   /   |'  | |' | 
  /     \   /       \ '  | |     /     \ ,'_ /| :  . | '  | |    /       \ |  |   |  .   ; ,. :|  |   ,' 
 /    / '  .--.  .-. ||  | :    /    / ' |  ' | |  . . |  | :   .--.  .-. |:__,'| :  '   | |: :'  :  /   
.    ' /    \__\/: . .'  : |__ .    ' /  |  | ' |  | | '  : |__  \__\/: . .  '  : |__'   | .; :|  | '    
'   ; :__   ," .--.; ||  | '.'|'   ; :__ :  | : ;  ; | |  | '.'| ," .--.; |  |  | '.'|   :    |;  : |    
'   | '.'| /  /  ,.  |;  :    ;'   | '.'|'  :  `--'   \;  :    ;/  /  ,.  |  ;  :    ;\   \  / |  , ;    
|   :    :;  :   .'   \  ,   / |   :    ::  ,      .-./|  ,   /;  :   .'   \ |  ,   /  `----'   ---'     
 \   \  / |  ,     .-./---`-'   \   \  /  `--`----'     ---`-' |  ,     .-./  ---`-'                     
  `----'   `--`---'              `----'                         `--`---'                                 
                                                                                                         
      """)

print("""
_____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
""")
Permission="y"
def calculator(number1,next_number,operation):
    if operation=="+":      
        return float(number1+next_number)
    elif operation=="-":
        return float(number1-next_number)
    elif operation=="*":
        return float(number1*next_number)
    else:
        return float(number1/next_number)
       
# while Permission=="n":    
number1=eval(input("What's the first number?:\n"))
print("+\n-\n*\n/")
while Permission=="y":
 operation=input("Pick an opeartion:\n")
 next_number=eval(input("What's the next number?:"))
 result = calculator(number1,next_number,operation)
 print(f"{float(number1)}{operation}{float(next_number)}={calculator(number1,next_number,operation)}\n")

 Permission=input(f"Type 'y' to continue calculating with {(number1)} , or type 'n' to start a new calculation:\n").lower()


