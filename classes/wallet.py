import uuid


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
