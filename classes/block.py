from classes.wallet import Wallet
import json
import os
import hashlib
import random

FOLDER_NAME = "./content/blocs"


class Block:

    def __init__(self):
        self.taille = 0
        self.hash = '00'
        self.parent_hash = '00'
        self.transactions = []
        self.base_hash = 0

    def check_hash(self, base_hash, goodhash):
        hash = '0000' + hashlib.sha256(base_hash.encode()).hexdigest()
        if hash == goodhash:
            return True
        else:
            return False

    def add_transaction(self, amount, emetteur: Wallet, recepteur: Wallet):

        # VERIFICATION DU SOLDE DU WALLET EMETTEUR
        if (emetteur.balance < amount):
            raise Exception(
                "Le montant de votre wallet est insuffisant pour faire la transaction")

        self.transactions.append(
            {'id_transaction': random.randint(1, 1000000), 'emetteur': emetteur.unique_id, 'amount': amount, 'recepteur': recepteur.unique_id})

        self.save(self.hash)

        emetteur.balance = emetteur.sub_balance(amount)
        emetteur.save()
        recepteur.balance = recepteur.add_balance(amount)
        recepteur.save()

    def get_weight(self):
        self.taille = os.path.getsize(
            FOLDER_NAME + '/' + self.hash + '.json') / 1024
        print("Actual size: " + str(self.taille) + " KO")
        return self.taille

    def save(self, hash):

        entry = {'taille': self.taille,
                 'hash': hash,
                 'parent_hash': self.parent_hash,
                 'transactions': self.transactions,
                 'base_hash': self.base_hash}

        if (os.path.exists(FOLDER_NAME)):
            try:
                fileName = str(hash) + ".json"
                path = FOLDER_NAME + '/' + fileName+'.json'
                if (os.path.exists(path)):
                    with open(path, "w") as jsf:
                        json.dump(entry, jsf)
                else:
                    fpJ = os.path.join(FOLDER_NAME, fileName)
                    with open(fpJ, "w") as jsf:
                        json.dump(entry, jsf)
            except Exception as e:
                print('titi', e)

    def load(self, hash):

        fileName = str(hash) + ".json"
        with open(FOLDER_NAME+"/"+fileName, 'r') as jsonFile:
            jsonObject = json.load(jsonFile)
        b = Block()
        b.hash = hash
        b.taille = jsonObject['taille']
        b.parent_hash = jsonObject['parent_hash']
        b.transactions = jsonObject['transactions']
        b.base_hash = jsonObject['base_hash']

        return b
