
from classes.wallet import Wallet


# CREATE WALLET
w = Wallet()
id = w.generate_unique_id()

entry = {"unique_id": id, "balance": w.balance}

w.save(id, entry)

w2 = w.load('996e2906-8626-48e5-a465-586215739619')
print(w2.balance)
