import json
from classes.wallet import Wallet
# with open("./content/wallets/wallets.json") as jsonFile:
#     jsonObject = json.load(jsonFile)
#     jsonFile.close()


# balance = jsonObject['balance']
# unique_id = jsonObject['unique_id']

# CREATE WALLET
w = Wallet()
id = w.generate_unique_id()
with open("./content/wallets/wallets.json", 'w') as jsonFile:
    json.dump({"unique_id": id, "balance": w.balance}, jsonFile)
    jsonFile.close()
