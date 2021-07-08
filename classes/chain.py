from classes.block import Block
import string
import random
import hashlib
import os

FOLDER_NAME = "./content/blocs"


class Chain:

    def __init__(self):
        firstBlock = Block()
        entry = {"hash": firstBlock.hash, "parent_hash": firstBlock.parent_hash,
                 "transactions": firstBlock.transactions, "base_hash": firstBlock.base_hash}
        firstBlock.save(firstBlock.hash, entry)
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
        entry = {"hash": newB.hash, "parent_hash": newB.parent_hash,
                 "transactions": newB.transactions, "base_hash": newB.base_hash}
        newB.save(newB.hash, entry)
        self.blocks.append(newB)
        print(self.blocks)

    def get_block(self):
        pass

        # add_transaction()

        # find_transaction()

        # get_last_transaction_number()
