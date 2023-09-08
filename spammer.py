import tls_client
from tls_client import Session
import random
import concurrent.futures
import time
import json
import colorama
from colorama import Fore, Style, init


def spammer():

    with open('config.json', 'r') as f:
        config = json.load(f)

    with open("proxies.txt") as proxies:
        proxy = proxies.readlines()
        random_proxy = random.choice(proxy).strip()

    cuantas_generar = int(input(Fore.YELLOW + "[" + Fore.RED + ">" + Fore.YELLOW + "] " + Fore.WHITE + "How many accounts would you like to generate? "))
    threads = int(input(Fore.YELLOW + "[" + Fore.RED + ">" + Fore.YELLOW + "] " + Fore.WHITE + "How many threads would you like to use? "))

    invite = (config['invite'])
    bio = (config['bio'])
    tagline = (config['tagline'])
    guild_id = (config['guild_id'])
    referral_code = (config['referral_code'])



    def generate_account():
        with open("users.txt", encoding="utf-8") as users:
            usernames = users.readlines()
            random_username = random.choice(usernames).strip()

        session = tls_client.Session(
            client_identifier=f"chrome_{random.randint(103, 112)}",
            random_tls_extension_order=True
        )

        session.proxies = {
            "http": "http://" + random_proxy,
            "https": "https://" + random_proxy
        }

        email = f"pycontroller{random.randint(0, 10000000)}@pycontrollermail{random.randint(0, 99999999)}.com"
        password = f"PycontrollerOnTop{random.randint(0, 10000000)}"

        res = session.post(
            f"https://www.guilded.gg/api/users?type=email?r={referral_code}",
            json={
                "email": email,
                "platform": "desktop",
                "fullName": random_username,
                "name": random_username,
                "password": password
            }
        )

        if res.status_code == 200:

            json_response = res.json()
            id = json_response['user']['id']

            print(Fore.YELLOW + "[" + Fore.GREEN + "+" + Fore.YELLOW + "] " + Fore.WHITE + Fore.GREEN + f"Account created {random_username}")
            account_details = str(f"{email}:{password}\n")
            with open("spammer_accs.txt", "a") as file:
                file.write(account_details)
        else:
            print(Fore.YELLOW + "[" + Fore.RED + "-" + Fore.YELLOW + "] " + Fore.WHITE + Fore.MAGENTA + f"Error creating account. Status code: {res.status_code}")

            session = tls_client.Session(
            client_identifier=f"chrome_{random.randint(110, 115)}",
            random_tls_extension_order=True
            )

        res = session.put(
            f"https://www.guilded.gg/api/invites/{invite}?teamId={guild_id}&includeLandingChannel=true",
        )

        if res.status_code == 200:
            print(Fore.YELLOW + "[" + Fore.GREEN + "+" + Fore.YELLOW + "] " + Fore.WHITE + Fore.YELLOW + f"Account joined! {invite}")
        else:
            print(Fore.YELLOW + "[" + Fore.RED + "-" + Fore.YELLOW + "] " + Fore.WHITE + Fore.MAGENTA + f"Error joining server. Status code: {res.status_code}")

        res = session.put(
            f"https://www.guilded.gg/api/users/{id}/profilev2",

            json = {
                    "userId": id,
                    "aboutInfo": {
                        "bio": bio,
                        "tagLine": tagline,
                    },
                },

        )

        if res.status_code == 200:
            print(Fore.YELLOW + "[" + Fore.GREEN + "+" + Fore.YELLOW + "] " + Fore.WHITE + Fore.BLUE + f"Added tagline and bio")
        else:
            print(Fore.YELLOW + "[" + Fore.RED + "-" + Fore.YELLOW + "] " + Fore.WHITE + Fore.MAGENTA + f"Error adding tagline and bio. Status code: {res.status_code}")


    counter = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            futures = [executor.submit(generate_account) for _ in range(cuantas_generar)]
            concurrent.futures.wait(futures)