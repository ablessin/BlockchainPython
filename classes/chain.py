from classes.block import Block
import string
import random
import hashlib
import os

FOLDER_NAME = "./content/blocs"


class Chain:

    def __init__(self):
        firstBlock = Block()
        firstBlock.save(firstBlock.hash)
        self.blocks = [firstBlock]

    def generate_string(self):
        length_of_string = 30
        return (''.join(random.choice(string.ascii_letters + string.digits)
                        for _ in range(length_of_string)))

    def generate_hash(self):
        string = self.generate_string()
        hash = hashlib.sha256(string.encode()).hexdigest()
        print(hash)
        cpt = 0

        while not(self.verify_hash(hash)):
            string = self.generate_string()
            hash = hashlib.sha256(string.encode()).hexdigest()
            print(hash)
            toto = self.verify_hash(hash)
            cpt = cpt+1
            print(cpt)
            print(toto)

        return hash

    def verify_hash(self, hash):
        if not(os.path.exists(FOLDER_NAME + "/" + hash + ".json")):
            print(hash.startswith('0000'))
            return hash.startswith('0000')
        else:
            return False

    def add_block(self):

        hash = self.generate_hash()
        print(hash)
        b = Block()
        b.hash = hash
        b.parent_hash = self.blocks[len(self.blocks) - 1].hash
        b.save(hash)

        self.blocks.append(b)

        # get_block()

        # add_transaction()

        # find_transaction()

        # get_last_transaction_number()
