from blockchain import Blockchain
from datetime import datetime
from hashlib import sha256
import random

mempool = []
wallets = []


class CreateWallet():
    def __init__(self):
        # use proper way to create wallet address later
        self.wallet_address = random.randint(0, 10000)
        self.wallet_balance = 0
        self.airdrop()
        self.add_to_wallets()

    def airdrop(self):
        if self.wallet_balance == 0:
            self.wallet_balance += 100
        else:
            print("Fuck You Cunt")

    def add_to_wallets(self):
        wallets.append({

            "wallet_address": self.wallet_address,
            "wallet_balance": self.wallet_balance
        })


class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.time_submitted = datetime.now()
        self.transaction_hash = self.generate_hash()
        self.add_to_mem()
        self.transaction_info()

    def generate_hash(self):
        transaction_header = str(self.sender) + str(self.receiver) + str(self.amount) + str(self.time_submitted)
        transaction_hash = sha256(transaction_header.encode())
        return transaction_hash.hexdigest()

    def add_to_mem(self):
        mempool.append({

            "transaction_hash": self.transaction_hash,
            "sender": self.sender,
            "receiver": self.receiver,
            "amount": self.amount,
            "time_submitted": self.time_submitted

        })

    def transaction_info(self):
        print(f"{self.sender} has requested to send {self.receiver} {self.amount} bigcoins at {self.time_submitted}")


Bigcoin = Blockchain()

CreateWallet()
CreateWallet()
# print(wallets)
Transaction(wallets[0]["wallet_address"], wallets[1]["wallet_address"], 50)
Transaction(wallets[0]["wallet_address"], wallets[1]["wallet_address"], 20)
Transaction(wallets[1]["wallet_address"], wallets[0]["wallet_address"], 10)
# print(mempool)


Bigcoin.add_block(mempool)
Bigcoin.print_blocks()
Bigcoin.validate_chain()
