from classes.chain import Chain
from classes.wallet import Wallet

AMOUNT = 0.01

# CREATE BLOCKCHAIN
chain = Chain()


# CREATE WALLET EMETTEUR

emetteur = Wallet()
id = emetteur.generate_unique_id()
emetteur.save()


# CREATE WALLET RECEPTEUR

recepteur = Wallet()
id = recepteur.generate_unique_id()
recepteur.save()


# VERIFICATION EXISTENCE WALLET EMETTEUR ET RECEPTEUR

if not(emetteur.exist() or recepteur.exist()):
    raise Exception("Une wallet n'existe pas")


# CREATE BLOCKS

block = chain.generate_hash()
if (block.check_hash(block.base_hash, block.hash)):

    # ADD BLOCK IN CHAIN
    chain.add_block(block)

    # ADD TRANSACTION IN BLOCK
    cmpt = 0
    for i in range(1000):
        for j in range(10):
            if block.taille < 256:
                chain.add_transaction(block.hash, AMOUNT, emetteur, recepteur)
                cmpt += 1
                print(cmpt)
                block.get_weight()
            else:
                block = chain.generate_hash()
                chain.add_block(block)
                chain.add_transaction(
                    block.hash, AMOUNT, emetteur, recepteur)
                print('isfdni')
                block.get_weight()
