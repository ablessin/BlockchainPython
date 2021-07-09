import uuid
import json
import os

FOLDER_NAME = "./content/wallets"


class Wallet:

    # INITIALISE LES WALLETS A DES VALEURS PAR DEFAUT
    def __init__(self):
        self.unique_id = 0
        self.balance = 100
        self.history = []

    # GENERE UNE CHAINE DE CARACTERE VIA UUID
    def generate_unique_id(self):
        self.unique_id = str(uuid.uuid4())

        # VERIFIE SI LA CHAINE DE CARACTERE N EXISTE PAS DEJA SINON EN RECREER UN
        while (os.path.exists(FOLDER_NAME + "/" + self.unique_id + ".json")):
            self.unique_id = str(uuid.uuid4())
        return self.unique_id

    # AJOUTE DE LA MONNAIE DANS UNE WALLET
    def add_balance(self, cashin):
        self.balance = self.balance + cashin
        return self.balance

    # SOUSTRAIE DE LA MONNAIE DANS UNE WALLET
    def sub_balance(self, cashout):
        self.balance = self.balance - cashout
        return self.balance

    # JE CROIS QUE J Y SUIS PAS REVENU
    def send(self):
        pass

    # SAVE LA WALLET AVEC SES ATTRIBUTS
    def save(self):

        entry = {'unique_id': self.unique_id,
                 'balance': self.balance, 'history': self.history}

        if (os.path.exists(FOLDER_NAME)):

            try:

                fileName = self.unique_id + ".json"
                fpJ = os.path.join(FOLDER_NAME, fileName)
                with open(fpJ, "w") as jsf:
                    json.dump(entry, jsf)
            except Exception as e:
                print(e)
    # RECUPERE LES ELEMENTS D UNE WALLETS PRECISE EN FONCTION SE SON UNIQUE_ID

    def load(self, unique_id):

        fileName = unique_id + ".json"
        with open(FOLDER_NAME+"/"+fileName, 'r') as jsonFile:
            jsonObject = json.load(jsonFile)
        w = Wallet()
        w.unique_id = unique_id
        w.balance = jsonObject['balance']

        return w

    # FONCTION QUI ME PERMET DE TEST SI LE DOSSIER EXISTE OU NON
    def exist(self):
        return os.path.exists(FOLDER_NAME + "/" + self.unique_id + ".json")
