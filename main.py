
from classes.chain import Chain
from classes.wallet import Wallet


# # CREATE WALLET
# w = Wallet()
# id = w.generate_unique_id()

# entry = {"unique_id": id, "balance": w.balance}

# w.save(id, entry)

# print(w.unique_id)

# w2 = w.load('996e2906-8626-48e5-a465-586215739619')

c = Chain()


# print(c.generate_string())

c.add_block()
print(c.blocks)
