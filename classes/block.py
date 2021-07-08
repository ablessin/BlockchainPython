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

    def check_hash(self, base_hash, goodhash):
        hash = '0000' + hashlib.sha256(base_hash.encode()).hexdigest()
        if hash == goodhash:
            return True
        else:
            return False

    def add_transaction(self):
        pass

    def get_weight(self):
        pass

    def save(self, hash, entry):

        if (os.path.exists(FOLDER_NAME)):
            try:
                fileName = str(hash) + ".json"
                print(fileName)
                fpJ = os.path.join(FOLDER_NAME, fileName)
                with open(fpJ, "w") as jsf:
                    json.dump(entry, jsf)
            except Exception as e:
                print(e)

    def load(self, hash):

        fileName = str(hash) + ".json"
        with open(FOLDER_NAME+"/"+fileName, 'r') as jsonFile:
            jsonObject = json.load(jsonFile)
        b = Block()
        b.hash = hash
        b.parent_hash = jsonObject['parent_hash']
        b.transactions = jsonObject['transactions']
        b.base_hash = jsonObject['base_hash']

        return b
