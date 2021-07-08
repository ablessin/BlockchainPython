
from classes.block import Block
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

for i in range(4):
    b = c.generate_hash()
    if (b.check_hash(b.base_hash, b.hash)):
        c.add_block(b)
        b2 = b.load(b.hash)
        print('la', b2.parent_hash)
