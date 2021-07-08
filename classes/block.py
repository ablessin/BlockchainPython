import json
import os
import hashlib

FOLDER_NAME = "./content/blocs"


class Block:

    def __init__(self):
        self.taille = 0
        self.hash = '00'
        self.parent_hash = '00'
        self.transactions = []
        self.base_hash = 0

    def check_hash(self, base_hash):
        hash = hashlib.sha256(base_hash.encode()).hexdigest()
        if hash == self.hash{
            return True
        } else:
            return False

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

    def load(self, hash):

        fileName = hash + ".json"
        with open(FOLDER_NAME+"/"+fileName, 'r') as jsonFile:
            jsonObject = json.load(jsonFile)
        b = Block()
        b.hash = hash
        b.parent_hash = jsonObject['parent_hash']
        b.transactions = jsonObject['transactions']
        b.base_hash = jsonObject['base_hash']
