import uuid
import json
import os

FOLDER_NAME = "./content/wallets"


class Wallet:

    def __init__(self):
        self.unique_id = 0
        self.balance = 0
        self.history = []

    def generate_unique_id(self):
        return str(uuid.uuid4())

    def add_balance(self, cashin):
        return self.balance + cashin

    def sub_balance(self, cashout):
        return self.balance - cashout

    def save(self, id, entry):

        if (os.path.exists(FOLDER_NAME)):

            try:

                fileName = id + ".json"
                fpJ = os.path.join(FOLDER_NAME, fileName)
                with open(fpJ, "w") as jsf:
                    json.dump(entry, jsf)
                    print("finish writing")
            except Exception as e:
                print(e)

    def load(self, unique_id):

        fileName = unique_id + ".json"
        with open(FOLDER_NAME+"/"+fileName, 'r') as jsonFile:
            jsonObject = json.load(jsonFile)
        w = Wallet()
        w.unique_id = unique_id
        w.balance = jsonObject['balance']
        print(w.balance)
        return w
