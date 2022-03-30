from Transaction import Transaction

class TransactionPool():
    def __init__(self):
        self.transactions = []

    def addTransaction(self, transaction: Transaction):
        self.transactions.append(transaction)
        return

    def transactionExists(self, transaction: Transaction) -> bool:
        for trans in self.transactions:
            if trans.equals(transaction):
                return True
        return False