import tls_client
from tls_client import Session
import random
import concurrent.futures
import time
import base64
import json
import colorama
from colorama import Fore, Style, init

def realistic():

    with open("proxies.txt") as proxies:
        proxy = proxies.readlines()
        random_proxy = random.choice(proxy).strip()

    with open('config.json', 'r') as f:
        config = json.load(f)

    invite = (config['invite'])
    bio = (config['bio'])
    tagline = (config['tagline'])
    guild_id = (config['guild_id'])
    tittle_feed = (config['tittle_feed'])
    text_feed = (config['text_feed'])
    referral_code = (config['referral_code'])

    cuantas_generar = int(input(Fore.YELLOW + "[" + Fore.RED + ">" + Fore.YELLOW + "] " + Fore.WHITE + "How many accounts would you like to generate? "))
    threads = int(input(Fore.YELLOW + "[" + Fore.RED + ">" + Fore.YELLOW + "] " + Fore.WHITE + "How many threads would you like to use? "))



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
            account_details = str(f"{email}:{password}\n")
            with open("realist_accs.txt", "a") as file:
                file.write(account_details)
        else:
            print(Fore.YELLOW + "[" + Fore.RED + "-" + Fore.YELLOW + "] " + Fore.WHITE + Fore.MAGENTA + f"Error joining server. Status code: {res.status_code}")

        res = session.post(
            f"https://www.guilded.gg/api/users/{id}/posts",

            json={"userId":f"{id}","title":f"{tittle_feed}","message":{"object":"value","document":{"object":"document","data":{},"nodes":[{"object":"block","type":"paragraph","data":{},"nodes":[{"object":"text","leaves":[{"object":"leaf","text":f"{text_feed}","marks":[]}]}]}]}}}
        )

        if res.status_code == 200:
            print(Fore.YELLOW + "[" + Fore.GREEN + "+" + Fore.YELLOW + "] " + Fore.WHITE + Fore.BLUE + f"Feed added")
            time.sleep(2)
        else:
            print(Fore.YELLOW + "[" + Fore.RED + "-" + Fore.YELLOW + "] " + Fore.WHITE + Fore.MAGENTA + f"Error adding feed. Status code: {res.status_code}")
            time.sleep(2)

        pfps_list = ["https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/6e30a4fc068204762c300b1311a3cbea-Large.png?w=450&h=450",
                      "https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/800a0c61ae30d972ef2a99be9447d298-Large.png?w=450&h=450",
                      "https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/e31f7c5699cb49678c0c812ce225cbaa-Large.png?w=450&h=450",
                      "https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/dd843aeb5150f46c984d2cf386e6c659-Large.png?w=450&h=450",
                      "https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/c40262696603d83f6f010314db51847d-Large.png?w=450&h=450",
                      "https://s3-us-west-2.amazonaws.com/www.guilded.gg/UserAvatar/de30a4417e710011c9baae4f96eb7040-Large.png?w=450&h=450",
                      "https://devforum-uploads.s3.dualstack.us-east-2.amazonaws.com/uploads/original/4X/9/0/f/90f25d6a2527e12dedbe03da1f6c5670d0c4902d.png?w=450&h=450",
                      "https://e1.pxfuel.com/desktop-wallpaper/140/271/desktop-wallpaper-hans-on-twitter-roblox-profile.jpg?w=450&h=450",]
        res = session.post(f'https://www.guilded.gg/api/users/me/profile/images', data=json.dumps({
                    "imageUrl": random.choice(pfps_list)
                }))

        if res.status_code == 200:
            print(Fore.YELLOW + "[" + Fore.GREEN + "+" + Fore.YELLOW + "] " + Fore.WHITE + Fore.BLUE + f"Pfp added")
            time.sleep(2)
        else:
            print(Fore.YELLOW + "[" + Fore.RED + "-" + Fore.YELLOW + "] " + Fore.WHITE + Fore.MAGENTA + f"Error adding pfp. Status code: {res.status_code}")
            time.sleep(2)

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
            time.sleep(2)
        else:
            print(Fore.YELLOW + "[" + Fore.RED + "-" + Fore.YELLOW + "] " + Fore.WHITE + Fore.MAGENTA + f"Error adding tagline and bio. Status code: {res.status_code}")
        time.sleep(2)
    
    counter = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            futures = [executor.submit(generate_account) for _ in range(cuantas_generar)]
            concurrent.futures.wait(futures)
