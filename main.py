from classes.chain import Chain
from classes.wallet import Wallet

# MONTANT DE LA TRANSACTION
AMOUNT = 0.011

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
# CHECK SI BASE_HASH EST = A HASH UNE FOIS BASE HASH HASCHE
if (block.check_hash(block.base_hash, block.hash)):

    # ADD BLOCK IN CHAIN
    chain.add_block(block)

    # ADD TRANSACTION IN BLOCK
    for i in range(1000):
        for j in range(10):
            # SI TAILLE DU BLOC INFERIEUR A 256KO
            if block.taille < 256:
                chain.add_transaction(block.hash, AMOUNT, emetteur, recepteur)
                block.get_weight()

            # SI TAILLE DU BLOC SUPERIEUR A 256KO ON RECREER UN BLOCK
            else:
                # CREER UN NOUVEAU BLOC
                block = chain.generate_hash()
                # AJOUTE LE BLOC A LA CHAIN
                chain.add_block(block)
                chain.add_transaction(
                    block.hash, AMOUNT, emetteur, recepteur)
                block.get_weight()
