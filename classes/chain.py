from classes.block import Block
import string
import random
import hashlib
import os
import json

FOLDER_NAME = "./content/blocs"


class Chain:

    def __init__(self):
        firstBlock = Block()
        firstBlock.save(firstBlock.hash)
        self.blocks = [firstBlock]

    def generate_string(self):
        length_of_string = 30
        res = (''.join(random.choice(string.ascii_letters + string.digits)
                       for _ in range(length_of_string)))
        return res

    def generate_hash(self):
        newB = Block()
        string = self.generate_string()
        newB.base_hash = string
        hash = '0000' + hashlib.sha256(string.encode()).hexdigest()
        newB.hash = hash
        cpt = 0

        while not(self.verify_hash(hash)):
            string = self.generate_string()
            newB.base_hash = string
            hash = hashlib.sha256(string.encode()).hexdigest()
            newB.hash = hash
            self.verify_hash(hash)
            cpt = cpt+1

        return newB

    def verify_hash(self, hash):
        if not(os.path.exists(FOLDER_NAME + "/" + hash + ".json")):
            return hash.startswith('0000')
        else:
            return False

    def add_block(self, newB: Block):

        newB.parent_hash = self.blocks[len(self.blocks)-1].hash
        newB.save(newB.hash)
        self.blocks.append(newB)
        print(self.blocks)

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

    def add_transaction(self, hash, amount, emetteur, recepteur):

        block = self.get_block(hash)

        if (block.get_weight() > 256):
            newBlock = self.generate_hash()
            self.add_block(newBlock)
            self.add_transaction(newBlock.hash, amount, emetteur, recepteur)
        else:
            block.add_transaction(amount, emetteur, recepteur)

        # find_transaction()

        # get_last_transaction_number()
