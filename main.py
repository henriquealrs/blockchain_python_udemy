# This is a sample Python script.
from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import  TransactionPool

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    t_type = 'TRANSFER'
    fraudulentWallet = Wallet()
    pool = TransactionPool()

    wallet = Wallet()
    transaction = wallet.createTransaction(receiver, amount, t_type)
    #print(Wallet.signatureValid(transaction.payload(), transaction.signature, wallet.publicKeyString()))
    #print(Wallet.signatureValid(transaction.payload(), transaction.signature, fraudulentWallet.publicKeyString()))
    if not pool.transactionExists(transaction):
        pool.addTransaction(transaction)
    print(pool.transactions)