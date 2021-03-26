from itertools import product
from string import ascii_lowercase, ascii_uppercase, digits
import requests, time, os

def check(code):
    req = requests.get(f"https://discord.com/api/v8/invites/{code}?with_counts=true")
    if not str(req.status_code).startswith("2"):
        return False
    else:
        return req.json()

def main():
    n = 1
    characters = ascii_uppercase + ascii_lowercase + digits

    while True:
        codes = (''.join(i) for i in product(characters, repeat=n))
        for code in codes:
            print(code)
            discord = check(code)
            if discord:
                info = f'https://discord.gg/{discord["code"]} | {discord["guild"]["name"]} | {discord["approximate_member_count"]} members'
                with open("discord-invites.txt", "a", encoding="utf-8") as f:
                    f.write(info.encode('utf-8', 'replace').decode() + "\n")
        n += 1

if __name__ == '__main__':
    main()