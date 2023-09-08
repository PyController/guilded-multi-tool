from colorama import Fore, Style, init
from pystyle import Write, System, Colors, Colorate
import tls_client
from tls_client import Session
import random
import concurrent.futures
import time
import json
import os
import ctypes
import spammer
import realistic
import sender
import check


titulo_terminal = '[PYGG] by PyController'
if os.name == 'posix':
    os.system('clear')
    os.system(f'echo -n -e "\033]0;{titulo_terminal}\007"')
elif os.name == 'nt':
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f'{titulo_terminal}')

while True:
    Write.Print("""
\t\t\t\t\t██████╗ ██╗   ██╗ ██████╗  ██████╗ 
\t\t\t\t\t██╔══██╗╚██╗ ██╔╝██╔════╝ ██╔════╝ 
\t\t\t\t\t██████╔╝ ╚████╔╝ ██║  ███╗██║  ███╗
\t\t\t\t\t██╔═══╝   ╚██╔╝  ██║   ██║██║   ██║
\t\t\t\t\t██║        ██║   ╚██████╔╝╚██████╔╝
\t\t\t\t\t╚═╝        ╚═╝    ╚═════╝  ╚═════╝ 
\t\t\t\t\t    (Python Guilded Generator)
\t\t\t\t        By: PyController (and a random guy)
\t\t\t\t\t   On: github.com/PyController
\t
\t            
[1] Bot Gen + Joiner     |     [2] Realistic Generator     |     [3] Spammer     |     [4] Account Checker
            
""", Colors.yellow_to_red, interval=0.000)

    opcion = str(input(Fore.YELLOW + "[" + Fore.RED + ">" + Fore.YELLOW + "] " + Fore.WHITE))
    mensaje = 'Accounts successfully generated with PYGG!'
    if opcion == '1':
        titulo_terminal = '[PYGG] by PyController - Bot Gen + Joiner'
        if os.name == 'posix':
            os.system('clear')
            os.system(f'echo -n -e "\033]0;{titulo_terminal}\007"')
        elif os.name == 'nt':
            os.system('cls')
            ctypes.windll.kernel32.SetConsoleTitleW(f'{titulo_terminal}')
        
        Write.Print("""
\t\t\t\t\t██████╗ ██╗   ██╗ ██████╗  ██████╗ 
\t\t\t\t\t██╔══██╗╚██╗ ██╔╝██╔════╝ ██╔════╝ 
\t\t\t\t\t██████╔╝ ╚████╔╝ ██║  ███╗██║  ███╗
\t\t\t\t\t██╔═══╝   ╚██╔╝  ██║   ██║██║   ██║
\t\t\t\t\t██║        ██║   ╚██████╔╝╚██████╔╝
\t\t\t\t\t╚═╝        ╚═╝    ╚═════╝  ╚═════╝ 
            
""", Colors.yellow_to_red, interval=0.000)
        
        mensaje = 'Accounts successfully generated with PYGG!'
        spammer.spammer()
    elif opcion == '2':
        titulo_terminal = '[PYGG] by PyController - Realistic Generator'
        if os.name == 'posix':
            os.system('clear')
            os.system(f'echo -n -e "\033]0;{titulo_terminal}\007"')
        elif os.name == 'nt':
            os.system('cls')
            ctypes.windll.kernel32.SetConsoleTitleW(f'{titulo_terminal}')
        
        Write.Print("""
\t\t\t\t\t██████╗ ██╗   ██╗ ██████╗  ██████╗ 
\t\t\t\t\t██╔══██╗╚██╗ ██╔╝██╔════╝ ██╔════╝ 
\t\t\t\t\t██████╔╝ ╚████╔╝ ██║  ███╗██║  ███╗
\t\t\t\t\t██╔═══╝   ╚██╔╝  ██║   ██║██║   ██║
\t\t\t\t\t██║        ██║   ╚██████╔╝╚██████╔╝
\t\t\t\t\t╚═╝        ╚═╝    ╚═════╝  ╚═════╝ 
            
""", Colors.yellow_to_red, interval=0.000)
        
        mensaje = 'Accounts successfully generated with PYGG!'
        realistic.realistic()
    elif opcion == '3':
        titulo_terminal = '[PYGG] by PyController - Spammer'
        if os.name == 'posix':
            os.system('clear')
            os.system(f'echo -n -e "\033]0;{titulo_terminal}\007"')
        elif os.name == 'nt':
            os.system('cls')
            ctypes.windll.kernel32.SetConsoleTitleW(f'{titulo_terminal}')
        
        Write.Print("""
\t\t\t\t\t██████╗ ██╗   ██╗ ██████╗  ██████╗ 
\t\t\t\t\t██╔══██╗╚██╗ ██╔╝██╔════╝ ██╔════╝ 
\t\t\t\t\t██████╔╝ ╚████╔╝ ██║  ███╗██║  ███╗
\t\t\t\t\t██╔═══╝   ╚██╔╝  ██║   ██║██║   ██║
\t\t\t\t\t██║        ██║   ╚██████╔╝╚██████╔╝
\t\t\t\t\t╚═╝        ╚═╝    ╚═════╝  ╚═════╝ 
            
""", Colors.yellow_to_red, interval=0.000)
        
        mensaje = 'Messages successfully sended with PYGG!'
        sender.iniciar()
    elif opcion == '4':
        titulo_terminal = '[PYGG] by PyController - Account Checker'
        if os.name == 'posix':
            os.system('clear')
            os.system(f'echo -n -e "\033]0;{titulo_terminal}\007"')
        elif os.name == 'nt':
            os.system('cls')
            ctypes.windll.kernel32.SetConsoleTitleW(f'{titulo_terminal}')
        
        Write.Print("""
\t\t\t\t\t██████╗ ██╗   ██╗ ██████╗  ██████╗ 
\t\t\t\t\t██╔══██╗╚██╗ ██╔╝██╔════╝ ██╔════╝ 
\t\t\t\t\t██████╔╝ ╚████╔╝ ██║  ███╗██║  ███╗
\t\t\t\t\t██╔═══╝   ╚██╔╝  ██║   ██║██║   ██║
\t\t\t\t\t██║        ██║   ╚██████╔╝╚██████╔╝
\t\t\t\t\t╚═╝        ╚═╝    ╚═════╝  ╚═════╝ 
            
""", Colors.yellow_to_red, interval=0.000)

        mensaje = 'Accounts successfully checket with PYGG'
        check.iniciar()
    else:
        print(Fore.RED + "[x] Incorrect option.")
        opcion = str(input(Fore.YELLOW + "[" + Fore.RED + ">" + Fore.YELLOW + "] " + Fore.WHITE))

    opcion = 0
    print(Fore.GREEN + "[✓] " + Fore.WHITE + mensaje)
    time.sleep(2.5)
    titulo_terminal = '[PYGG] by PyController'
    if os.name == 'posix':
        os.system('clear')
        os.system(f'echo -n -e "\033]0;{titulo_terminal}\007"')
    elif os.name == 'nt':
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW(f'{titulo_terminal}')
    