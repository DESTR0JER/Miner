strona = 'tutaj wklej strone'
nazwa = 'tutaj wklej programu '
nick = 'tutaj wklej swoj nick'
version = 'tutaj wklej wersje programu '
changelog_text = 'tutaj wklej zmiany'

va = 0
inva = 0

import json
import requests
import time
import random
from colorama import Fore
import os
import ctypes
import threading

cyan = Fore.CYAN


bal = 0

r = Fore.RESET

def check_directory():
    try:
        with open('Results/RESULTS.txt', 'a') as data:
            data.write('')
    except:
        error(5)


plus = "[" + Fore.GREEN + "+" + Fore.RESET + "]"
minus = "[" + Fore.RED + "-" + Fore.RESET + "]"

red = Fore.RED
green = Fore.GREEN

code = 0

os.system('mode con:cols=180 lines=30')

def setTitle(newTitle):
    ctypes.windll.kernel32.SetConsoleTitleW(newTitle)

def error(code: int):
    cls()
    print(f'Error! Code: {red}{code}{r}')
    print(f'Error documentation: https://{strona}/help-center')
    input('Click Enter to exit!')
    os._exit(0)

os.system('cls')

invaild_list = []

losuj = ["a", "A", "b", '1', "B", '2', "c", '3', 'C', '6', 'd', '4', 'D', '5', 'e', 'E', '7', 'f', 'F', '8', 'g', 'G', '9', 'h', 'H', '0', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z']

def checkCode():
    global code
    if code > 100000:
        print(f'{cyan}100.000 codes generated! Not found any bitcoin... {r}')
        time.sleep(0.5)
        print(f"{cyan}Changing proxies...{r}")
        time.sleep(5)
        code = 0
        mine()
    else:
        pass

def vaild():
    global balance
    hex = ""
    addr = ""
    for i in range(33):
        b = random.randint(0, 59)
        c = losuj[b]
        addr = addr + c

    for i in range(62):
        b = random.randint(0, 59)
        c = losuj[b]
        hex = hex + c
    

    bal = random.randint(0, 3)
    bals = random.randint(1, 9)
    balance = f"{bal}.{bals}"


    print(f'{plus} | ADDR: {green}1{addr}{r} | HEX: {green}{hex}{r} | REC: {green}{balance}', Fore.RESET)
    save = f'[+] | ADDR: 1{addr} | HEX: {hex} | REC: {balance} \n'

    bal = balance + balance
    setTitle(f'{nazwa} v{version}| INVAILD: {inva} | VAILD: {va} | LAST REC: {bal}')

    try:
        with open('Results/RESULTS.txt', 'a') as data:
            data.write(save)
        print('Saving in RESULTS.txt...')
        time.sleep(5)
    except:
        error(5)

def invaild():
    hex = ""
    addr = ""
    for i in range(33):
        b = random.randint(0, 59)
        c = losuj[b]
        addr = addr + c

    for i in range(62):
        b = random.randint(0, 59)
        c = losuj[b]
        hex = hex + c
    
    print(f'{minus} | ADDR: {cyan}1{addr}{r} | HEX: {cyan}{hex}{r} | REC: {cyan}0{r}')
    
def mine():
    global inva, va, balance, code
    while 1:
        time.sleep(0.03)
        checkCode()
        code = code + 1
        check = random.randint(1, 999999999999999999)
        if check == 2137:
            vaild()
            va = va + 1
            mine()
            
        else:
            invaild()
            inva = inva + 1
            setTitle(f'{nazwa} v{version}| INVAILD: {inva} | VAILD: {va} | LAST REC: {bal}')
    time.sleep(0.01)
        

def changelog():
    print(f'''
    {wersja}
    {changelog_text}
    ''')
    input('Click Enter to continue...')
    menu()

def settings():
    global cyan
    print(f"""
    1. {red}RED{r}
    2. {Fore.CYAN}CYAN{r}
    3. {green}GREEN{r}
    4. {Fore.BLUE}BLUE{r}
    5. {Fore.MAGENTA}MAGENTA{r}
    """)
    choose_colour = int(input(f'Select options from 1 to 3 {cyan}>>>{r} '))
    if choose_colour == 1:
        cyan = Fore.RED
    elif choose_colour == 2:
        cyan = Fore.CYAN
    elif choose_colour == 3:
        cyan = Fore.GREEN
    elif choose_colour == 4:
        cyan = Fore.BLUE
    elif choose_colour == 5:
        cyan = Fore.MAGENTA
    else:
        print('ERROR we cant find color')
        menu()
    print('Change saved!')
    time.sleep(0.5)
    menu()

def cls():
    os.system('cls')

def menu():
    cls()
    setTitle(f'{nazwa} v{version}| INVAILD: {inva} | VAILD: {va} | LAST REC: {bal}')
    print(f'''{cyan}
{nazwa}
                                                            

            {cyan}Version:{r} {version}
            {cyan}Created by:{r} {nick}
            {cyan}WebSite:{r} {strona}
                                                     
    {Fore.RESET}''')
    print(f'''
    1.{cyan} Start Mine{r}
    2.{cyan} Setting{r}
    3.{cyan} ChangeLog{r}
    4.{cyan} Tutorial{r}
    5.{cyan} Exit{r}
    ''')
    choose = choose = int(input(f'Select options from 1 to 5 {cyan}>>>{r} '))
    if choose == 1:
        print('Please wait 5 seconds...')
        try:
            req = requests.get('https://www.google.pl/')
        except:
            error(1)
        time.sleep(5)
        os.system('cls')
        check_directory()
        while 1:
            mine()
    elif choose == 2:
        settings()
    elif choose == 3:
        changelog()
    elif choose == 4:
        print(f'Tutorial avible in website: {strona}')
        input('Click Enter to continue...')
        menu()
    elif choose == 5:
        os._exit(0)
    else:
        menu()
        
        
    

menu()