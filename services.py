from abc import ABC, abstractmethod
from time import *
from datetime import datetime
from TEXT import *
import os
import textwrap

text = TEXTO()
class def_Client(ABC):
    @abstractmethod
    def __init__(self, address):
        self._address = address
        self._count = []
        pass
    
    @abstractmethod
    def make_transaction(self, count, transaction):
        pass
    
    @abstractmethod
    def add_count(self, count):
        pass

class pessoa_fisica(def_Client):
    def __init__(self, address, cpf, name, birth):
        super().__init__(address)
        self._cpf = cpf
        self._name = name
        self._birth = birth
    
    def make_transaction(self, count, transaction):
        transaction.register_transaction(count)
    
    def add_count(self, count):
        self._count.append(count)


class def_Conta(ABC):
    @abstractmethod
    def __init__(self, count, saldo, client, agency):
        self._count = count
        self._saldo = saldo
        self._client = client
        self._agency = agency
        self._transactions = History()
        
    @abstractmethod
    def new_account(self, client):
        #should return a new account
        pass

    @abstractmethod
    def deposit(self, value):
        pass

    @abstractmethod
    def withdraw(self, value):
        pass


class conta_corrente(def_Conta):
    wthdr_set_act = 3
    
    def __init__(self, count, saldo, client, agency):
        super().__init__(count, saldo, client, agency)
        self.wthdr_lmt = 500.0
        self.wthdr_act = 0
    
    def new_account(self, client, number):
        pass

    def deposit(self, value):
        pass

    def withdraw(self, value):
        pass


class History():
    def __init__(self):
        self.transactions = []
    
    def register_transaction(self, transaction):
        _transaction = []
        _datetime = datetime.now()
        _transaction_name = transaction.__class__.__name__
        _transaction_time = _datetime.strftime('%d/%m/%Y--%H:%M:%S')
        _transaction.extend([_transaction_name, _transaction_time])
        self.transactions.append(_transaction)
        del _transaction, _datetime, _transaction_name, _transaction_time

    def show_transactions(self):
        for i in range(len(self.transactions)):
            _text = f"""--------------------------------
                        Operação: {self.transactions[i][0]}
                        Data: {self.transactions[i][1]}
                        """
            print(textwrap.dedent(_text))
            del _text
    

class transaction(ABC):
    @property
    @abstractmethod
    def value(self):
        pass

    @abstractmethod
    def register(self, count):
        pass


class withdraw(transaction):
    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        return self._value
    
    def register(self, count):
        pass


class deposit(transaction):
    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        return self._value
    
    def register(self, count):
        pass