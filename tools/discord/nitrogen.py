# -*- coding: utf-8 -*-
# omaiga
from concurrent.futures import ThreadPoolExecutor # ------- #
from colorama import Fore, init # ------------------------- #
from datetime import datetime # --------------------------- #
from random import choice # ------------------------------- #
import concurrent.futures # ------------------------------- #
from queue import Queue # --------------------------------- #
from pystyle import * # ----------------------------------- #
import tls_client # --------------------------------------- #
import threading # ---------------------------------------- #
import requests # ----------------------------------------- #
import colorama # ----------------------------------------- #
import aiohttp # ------------------------------------------ #
import random # ------------------------------------------- #
import ctypes # ------------------------------------------- #
import json # --------------------------------------------- #
import uuid # --------------------------------------------- #
import time # --------------------------------------------- #
import os # ----------------------------------------------- #

spade = """

┌┼┐┌─┐┌─┐┌┬┐┌─┐
└┼┐├─┘├─┤ ││├┤ 
└┼┘┴  ┴ ┴─┴┘└─┘
"""
lock = threading.Lock()
code = 0



def rn(clr="saygex"):
    if clr == "saygex":
        thing = Fore.GREEN
    else:
        thing = Fore.RED
    t = datetime.now().strftime('%H:%M:%S:%f')[:-4]
    return f"{Fore.LIGHTBLACK_EX}{t}     {Fore.RESET}    |    {Fore.RED}Spade{Fore.RESET}    |     [{thing}>{Fore.RESET}]{Fore.LIGHTBLACK_EX}    "

def fetch():
    try:
        response = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all')
        print(f"{rn()}Got Proxies")

        proxies = response.text

        with open('proxies.txt', 'w') as x:
            x.write(proxies)
        with open('proxies.txt', 'r') as file:
            proxy_list = [line.strip() for line in file if line.strip()]
        with open('proxies.txt', 'w') as omagad:
            omagad.write('\n'.join(proxy_list))
    except requests.RequestException as e:
        print(f"{rn()}[{Fore.RED}/{Fore.RESET}] Spade      | Couldn't fetch proxies. {e}")
        return []


def gen(proxy):
    def post(*args, **kwargs):
        while True:
            try:
                return requests.post(*args, **kwargs)
            except Exception as e:
                continue

    def generate_code(session, proxy):
        global code
        try:
            response = post('https://api.discord.gx.games/v1/direct-fulfillment', json={'partnerUserId': str(uuid.uuid4())}, proxies={'http': proxy, 'https': proxy})
        except RequestException as e:
            print(f'{rn()} Error [prob in connection with proxy]')
            return

        if response.status_code == 429:
            print(f'{rn()} Rate limit')
            return

        ptoken = response.json().get('token', '')
        if not ptoken:
            print(f'Error: Unable to retrieve token from the response')
            return

        link = f"https://discord.com/billing/partner-promotions/1180231712274387115/{ptoken}"
        print(f"{rn()} Generated a new code")

        with lock:
            code += 1
            open("promos.txt", 'a').write(f"{link}\n")
            ctypes.windll.kernel32.SetConsoleTitleW(f"Spade | Generated : {code}")

    threads = []
    for i in range(10):
        thread = threading.Thread(target=generate_code, args=(i, proxy))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def gpl():
    print(f"{rn()} Started New thread")
    try:
        pr = "http://" + choice(open("proxies.txt").read().splitlines())
    except:
        pr = None

    while True:
        try:
            gen(pr)
        except Exception as er:
            continue

def splg(nth):
    threads = []
    for _ in range(nth):
        thread = threading.Thread(target=gpl)
        threads.append(thread)

    try:
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        pass


def req():
    print(f"\nNOTE: {Fore.RED}[15 workers per thread. Amounts like 20-30 is enough. Anything larger than that will give rate limits only.]{Fore.RESET}\n")
    omaigad = int(input(f"{rn()} Threads > "))
    splg(omaigad)



if __name__ == "__main__":
    os.system('cls')
    os.system('title Spade [*] Starting')
    print(Colorate.Vertical(Colors.red_to_purple, Center.XCenter(spade)))
    print('\n\n')
    fetch()
    req()