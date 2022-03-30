import  uuid
import time
import copy

class Transaction():
    def __init__(self, senderPublicKey, receiverPublicKey, amount, t_type):
        self.senderPublicKey = senderPublicKey
        self.receiverPublicKey = receiverPublicKey
        self.amount = amount
        self.type = t_type
        self.id = uuid.uuid1().hex
        self.timestamp = time.time()
        self.signature = ''
    def toJson(self):
        return self.__dict__

    def sign(self, signature):
        self.signature = signature
        return

    def payload(self):
        jsonRep = copy.deepcopy(self.toJson())
        jsonRep['signature'] = ''
        return jsonRep

    def equals(self, other) -> bool:
        return self.id == other.id