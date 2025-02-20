from abc import ABC, abstractmethod
from time import *
from datetime import datetime
from TEXT import *
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
    def __init__(self, count, saldo, client):
        self._count = count
        self._saldo = saldo
        self._client = client
        self._agency = 1
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
    __wthdr_set_act = 3
    __wthdr_lmt = 500
    def __init__(self, count, saldo, client):
        super().__init__(count, saldo, client)
        self._wthdr_act = 0
    
    @classmethod
    def new_account(self, client, count_list):
        count = new_count_number(count_list)
        return conta_corrente(count, 0, client)

    def deposit(self, value):
        #need to be completed
        if value > 0:
            self._saldo += value
            return True
        else:
            print("A operação falhou")
            return False

    def withdraw(self, value):
        #need to be completed
        if self._wthdr_act > self.__wthdr_set_act:
            print(text.BANK.WITHDRAW_LIMIT_EXCEEDED)
            return False
        if value > self.__wthdr_lmt:
            print(text.BANK.ABOVE_LIMIT)
            return False
        if value > self._saldo:
            print(text.BANK.INSUFFICIENT_FUNDS)
            return False
        elif value > 0:
            self._saldo -= value
            self._wthdr_act += 1
            return True
        else:
            print("A operação falhou")
            return False

    def do_transaction(self, transaction, value):
        if transaction == 'deposit':
            if self.deposit(value):
                deposit.register(self)
        elif transaction == 'withdraw':
            if self.withdraw(value):
                withdraw.register(self)
        else:
            print("Operação inválida")
            return False
        
    def show_transactions(self):
        self._transactions.show_transactions()


class History():
    def __init__(self):
        self.transactions = []
    
    def register_transaction(self, transaction):
        _transaction = []
        _datetime = datetime.now()
        _transaction_name = transaction.__class__.__name__
        _transaction_time = _datetime.strftime('%d/%m/%Y--%H:%M:%S')
        _transaction_value = transaction.value
        _transaction.extend([_transaction_name, _transaction_value, _transaction_time])
        self.transactions.append(_transaction)
        del _transaction, _datetime, _transaction_name, _transaction_time, _transaction_value

    def show_transactions(self):
        for i in range(len(self.transactions)):
            _text = f"""--------------------------------
                        Operação: {self.transactions[i][0]}
                        Valoe da operação: {self.transactions[i][1]}
                        Data: {self.transactions[i][2]}
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
        History.register_transaction(self)


class deposit(transaction):
    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        return self._value
    
    def register(self, count):
        History.register_transaction(self)



def new_count_number(count_list):
        #Define a new number for a new account
    if count_list != []:
        for i in range(len(count_list)):
            if i+1 != count_list[i]:
                    return i+1
            if i == len(count_list)-1:
                return count_list[i]+1
    else:
        return 1
        
def data_aquis():
    #Get the data from the user
    data_list = []
    print(text.CLIENT.ADD_ADDRESS)
    address = input()
    data_list.append(address)
    print(text.CLIENT.ADD_CPF)
    cpf = input()
    data_list.append(cpf)
    print(text.CLIENT.ADD_NAME)
    name = input()
    data_list.append(name)
    print(text.CLIENT.ADD_BIRTH)
    birth = input()
    data_list.append(birth)
    return data_list

def adding_client():
    #Add a new client to the bank
    data_list = data_aquis()
    return pessoa_fisica(data_list[0], data_list[1], data_list[2], data_list[3])

#Add new fucntions to search for a client and a account
def search_client(cpf, client_list):
    for i in range(len(client_list)):
        if client_list[i]._cpf == cpf:
            return client_list[i]
    return False 

def search_count(number, account_list):
    for i in range(len(account_list)):
        if account_list[i]._count == number:
            return account_list[i]
    pass