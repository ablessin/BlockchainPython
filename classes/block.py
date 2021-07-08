import hashlib
import uuid
import json
import os

FOLDER_NAME = "./content/blocs"


class Block:

    def __init__(self):
        self.taille = 0
        self.hash = '00'
        self.parent_hash = '00'
        self.transactions = []
        self.base_hash = 0

    def check_hash(self, base_hash):
        pass

    def add_transaction(self):
        pass

    def get_weight(self):
        pass

    def save(self, hash):

        if (os.path.exists(FOLDER_NAME)):
            print('aaa')

            try:
                fileName = str(hash) + ".json"
                print(fileName)
                fpJ = os.path.join(FOLDER_NAME, fileName)
                with open(fpJ, "w") as jsf:
                    json.dump({"hash": hash}, jsf)
            except Exception as e:
                print(e)

    def load(self):
        pass
