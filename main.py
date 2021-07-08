
from classes.wallet import Wallet


# CREATE WALLET
w = Wallet()
id = w.generate_unique_id()

entry = {"unique_id": id, "balance": w.balance}

w.save(id, entry)
