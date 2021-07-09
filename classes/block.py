from classes.wallet import Wallet
import json
import os
import hashlib
import random

FOLDER_NAME = "./content/blocs"


class Block:
    # INITIALISE D UN BLOC DE BASE
    def __init__(self):
        self.taille = 0
        self.hash = '00'
        self.parent_hash = '00'
        self.transactions = []
        self.base_hash = 0

    # VERIFIE SI LE HASH CORRESPOND AU BASE_HASH UNE FOIS BASE_HASH HASHE
    # NE SAIT PAS QUAND L'UTILISER DANS MAIN.PY MAIS FONCTIONNE
    def check_hash(self, base_hash, goodhash):
        hash = hashlib.sha256(base_hash.encode()).hexdigest()
        if hash == goodhash:
            return True
        else:
            return False

    # RECUPERE LES DEUX WALLETS ET EFFECTUE LES TESTS POUR
    # SAVOIR SI LA TRANSACTIONS EST POSSIBLES
    def add_transaction(self, amount, emetteur: Wallet, recepteur: Wallet):

        # VERIFICATION DU SOLDE DU WALLET EMETTEUR SINON ON SORT DE LA FONCTION
        if (emetteur.balance < amount):
            raise Exception("Le montant de votre wallet est insuffisant")

        # RECUPERE TOUTES LES INFORMATIONS POUR LES
        # AJOUTER AUX TRANSACTIONS DU BLOCK
        self.transactions.append({
            'id_transaction': random.randint(1, 1000000),
            'emetteur': emetteur.unique_id,
            'amount': amount,
            'recepteur': recepteur.unique_id})
        self.save(self.hash)

        # EFFECTUE LES OPERATIONS DES WALLETS ET
        # SAUVEGARDE LES DIFFERENTES WALLETS
        emetteur.balance = emetteur.sub_balance(amount)
        emetteur.save()
        recepteur.balance = recepteur.add_balance(amount)
        recepteur.save()

    # RECUPERE LE POIDS D UN BLOCK VIA LA FONCTION GETSIZE

    def get_weight(self):
        self.taille = os.path.getsize(
            FOLDER_NAME + '/' + self.hash + '.json') / 1024
        print("Actual size: " + str(self.taille) + " KO")
        return self.taille

    # ENREGISTRE UN BLOCK AVEC SES ATTRIBUTS
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
                print('Le bloc ne peut pas se sauvegarder', e)

    # PERMET DE CHARGER LE CONTENU D UN BLOCK PRECIS A PARTIR DE SON HASH
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
