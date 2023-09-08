import tls_client
from tls_client import Session
import random
import concurrent.futures
import time
import base64
import json
import colorama
from colorama import Fore, Style, init
import string
import uuid

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def iniciar():
    message = str(input(Fore.YELLOW + "[" + Fore.RED + ">" + Fore.YELLOW + "] " + Fore.WHITE + "What message do u like to send? "))
    channel_id = str(input(Fore.YELLOW + "[" + Fore.RED + ">" + Fore.YELLOW + "] " + Fore.WHITE + "What is the channel ID? "))
    quantity = int(input(Fore.YELLOW + "[" + Fore.RED + ">" + Fore.YELLOW + "] " + Fore.WHITE + "How many messages do u like to send? "))
    threads = int(input(Fore.YELLOW + "[" + Fore.RED + ">" + Fore.YELLOW + "] " + Fore.WHITE + "How many threads do u like to use? "))

    def spam():
        
        with open('realist_accs.txt', 'r') as file:
            accounts = [line.strip().split(':') for line in file if ':' in line]

        with open("proxies.txt") as proxies:
            proxy = proxies.readlines()
            random_proxy = random.choice(proxy).strip()

        for email, password in accounts:
            session = tls_client.Session(
                client_identifier=f"chrome_{random.randint(103, 112)}",
                random_tls_extension_order=True
            )

            session.proxies = {
                "http": "http://" + random_proxy,
                "https": "https://" + random_proxy
            }

            res = session.post(
                f"https://www.guilded.gg/api/login",
                json={
                    "email": email,
                    "getMe": True,
                    "password": password
                }
            )

            if res.status_code == 200:
                print(Fore.YELLOW + "[" + Fore.GREEN + "+" + Fore.YELLOW + "] " + Fore.WHITE + Fore.YELLOW + f"Logged in")
            else:
                print(Fore.YELLOW + "[" + Fore.RED + "-" + Fore.YELLOW + "] " + Fore.WHITE + Fore.MAGENTA + f"Not logged in")

            res = session.post(
                f"https://www.guilded.gg/api/channels/{channel_id}/messages",
                json={"messageId": str(uuid.uuid4()),"content":{"object":"value","document":{"object":"document","data":{},"nodes":[{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":f"{message}","marks":[]}]}]}]}},"repliesToIds":[],"confirmed":False,"isSilent":False,"isPrivate":False}
            )

            if res.status_code == 200:
                print(Fore.YELLOW + "[" + Fore.GREEN + "+" + Fore.YELLOW + "] " + Fore.WHITE + Fore.GREEN + f"Message sent")
                sender += 1
            else:
                print(Fore.YELLOW + "[" + Fore.RED + "-" + Fore.YELLOW + "] " + Fore.WHITE + Fore.MAGENTA + f"Message didn't send")


    counter = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            futures = [executor.submit(spam) for _ in range(quantity)]
            concurrent.futures.wait(futures)