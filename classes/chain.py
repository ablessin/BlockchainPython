from classes.block import Block
import string
import random
import hashlib
import os
import json

FOLDER_NAME = "./content/blocs"


class Chain:

    # INITIALISATION DU PREMIER BLOCK DE LA CHAINE
    def __init__(self):
        firstBlock = Block()
        firstBlock.save(firstBlock.hash)
        self.blocks = [firstBlock]

    # GENERATION D UNE STRING
    def generate_string(self):
        length_of_string = 30
        res = (''.join(random.choice(string.ascii_letters + string.digits)
                       for _ in range(length_of_string)))
        return res

    # RECUPERE LA STRING ET LA HASH
    def generate_hash(self):
        newB = Block()
        string = self.generate_string()
        newB.base_hash = string
        hash = hashlib.sha256(string.encode()).hexdigest()
        newB.hash = hash
        cpt = 0

        # APELLE LA FONCTION POUR VOIR SI LE HASH EST CORRECT SINON EN
        # REGENERE UN NOUVEAU
        while not(self.verify_hash(hash)):
            string = self.generate_string()
            newB.base_hash = string
            hash = hashlib.sha256(string.encode()).hexdigest()
            newB.hash = hash
            self.verify_hash(hash)

        # COMPTE LE NOMBRE DE HASH GENERER PARCE QUE CEST MARRANT
        cpt = cpt+1
        return newB

    # VERIFIE SI LE HASH EXISTE PAS DEJA ET SI IL COMMENCE PAR "0000"
    # AVEC LA FONCTION STARTSWITH
    def verify_hash(self, hash):
        if not(os.path.exists(FOLDER_NAME + "/" + hash + ".json")):
            return hash.startswith('0000')
        else:
            return False

    # PERMET D AJOUTER UN BLOCK A LA CHAIN
    def add_block(self, newB: Block):

        newB.parent_hash = self.blocks[len(self.blocks)-1].hash
        newB.save(newB.hash)
        self.blocks.append(newB)
        print(self.blocks)

    # PERMET DE RECUPERER LES INFORMATIONS D UN BLOCK DE LA CHAIN VIA SON HASH
    def get_block(self, hash):
        fileName = hash + ".json"
        with open(FOLDER_NAME+"/"+fileName, 'r') as jsonFile:
            jsonObject = json.load(jsonFile)
        b = Block()
        b.taille = jsonObject['taille']
        b.parent_hash = jsonObject['parent_hash']
        b.transactions = jsonObject['transactions']
        b.base_hash = jsonObject['base_hash']
        b.hash = hash

        return b

    # AJOUTE UNE TRANSACTION ENTRE DEUX WALLETS ET APELLE
    # LA FONCTION HOMONYME DANS BLOCK.PY
    def add_transaction(self, hash, amount, emetteur, recepteur):

        block = self.get_block(hash)
        block.add_transaction(amount, emetteur, recepteur)

        # find_transaction()

        # get_last_transaction_number()
