from time import *
import os
import time
from TEXT import *

text = TEXTO()
class bank_actions:
    __LMT_S_OP = 500
    __LMT_S_D = 3
    
    def saque(self, valor, conta):
        valor = float(valor)
        if valor > self.__LMT_S_OP:
            print(text.BANK.ABOVE_LIMIT)
            return
        elif valor <= 0:
            print(text.BANK.INVALID_VALUE)
            return
        else:
            if conta.dados['saldo'] < valor:
                print(text.BANK.INSUFFICIENT_FUNDS)
                return
            else:
                conta.dados['saldo'] -= valor
                conta.dados['extrato'].append([f"Saque no valor de R${valor:.2f}", time.ctime()])
                conta.dados['lmt_d'] += 1
                print(text.BANK.WITHDRAW_SUCCESS)
                return
            
    def deposito(self, valor, conta):
        valor = float(valor)
        if valor <= 0:
            print(text.BANK.INVALID_VALUE)
            return
        else:
            conta.dados['saldo'] += valor
            conta.dados['extrato'].append([f"Depósito no valor de R${valor:.2f}", time.ctime()])
            print(text.BANK.DEPOSIT_SUCCESS)
            return
    
    def extrato(self, conta):
        print(text.BANK.EXTRATO)
        for i in range(len(conta.dados['extrato'])):
            print(conta.dados['extrato'][i])
        print(f"Saldo atual: R${conta.dados['saldo']:.2f}")
        return
        
    
class client:
    def __init__(self):
        self.dados={
            'Nome': '',
            'data_nasc': '',
            'CPF': '',
            'Endereço': '',
            'contas': []
        }
        self.criar_nome()
        self.criar_data_nasc()
        self.criar_cpf()
        self.criar_endereco()

    def criar_nome(self):
        nome = input(text.CLIENT.ADD_NAME)
        self.dados['Nome'] = nome
        return
    
    def criar_data_nasc(self):
        data_nasc = input(text.CLIENT.ADD_BIRTH)
        self.dados['data_nasc'] = data_nasc
        return
    
    def criar_cpf(self):
        cpf = input(text.CLIENT.ADD_CPF)
        self.dados['CPF'] = cpf
        return
    
    def criar_endereco(self):
        endereco = input(text.CLIENT.ADD_ADDRESS)
        self.dados['Endereço'] = endereco
        return
      
      
class bank:
    def __init__(self, cpf, lista_contas):
        N_contas = self.criar_n_conta(lista_contas)
        self.dados = {
            'CPF': cpf,
            'Agencia': '0001',
            'n_conta': N_contas,
            'saldo': 1500,
            'extrato': [],
            'lmt_d': 0
        }
        
       

    def criar_n_conta(self, lista_contas):
        if len(lista_contas) == 0:
            n_conta = 1
        else:
            n_conta = lista_contas[-1].dados['n_conta'] + 1       
        return n_conta
    

class search:
    def search_client(self, cpf, lista_clientes):
        #search for a client in the list of clients by cpf
        a=0
        for i in range(len(lista_clientes)):
            if lista_clientes[i].dados['CPF'] == cpf:
                a = 1
                return lista_clientes[i]
                
        if a != 1: 
            print(text.CLIENT_NOT_FOUND)
            return
    
    def search_n_conta(self, n_conta, lista_contas):
        #search for a bank account in the list of bank accounts by account number
        a=0
        n_conta = int(n_conta)
        for i in range(len(lista_contas)):
            if lista_contas[i].dados['n_conta'] == n_conta:
                return lista_contas[i]
                a = 1

        if a != 1:
            print(text.ACCOUNT_NOT_FOUND)
            return

class process:
    #Classe responsável por funções de processsamento, aquisição e impressão de dados inerentes ao funcionamento do banco
    def add_cliente(self, lista_clientes):
        #add a new client to the list of clients
        answer = input(text.CLIENT.ADD_CLIENT)
        if answer == 'sim':
            cliente = client()
            lista_clientes.append(cliente)
            print(text.CLIENT.CLIENT_ADDED)
            sleep(1.)
            self.verify_data(cliente)
        return

    def add_conta(self, lista_contas, lista_clientes):
        #create a bank account to a client and add it to the list of bank accounts
        cpf = input(text.BANK.ENTER_CPF_FOR_ACCOUNT)
        conta = bank(cpf, lista_contas)
        lista_contas.append(conta)
        #adding the account number to the client's account list
        n_conta = conta.dados['n_conta']
        serc = search()
        cliente = serc.search_client(cpf, lista_clientes)
        if cliente != None:
            cliente.dados['contas'].append(n_conta)
        print(text.BANK.ACCOUNT_ADDED)
        sleep(0.8)
        text.functions.going_back()
        return
        
    def get_key(self, dict, index, retunr_option = None):
        if retunr_option == None:
            keys = list(dict.dados.keys())
            if 0 <= index < len(keys):
                return keys[index]
            else:
                return None
        else:
            if retunr_option == 0:
                keys = list(dict.dados.keys())
                return len(keys)
            if retunr_option == 1:
                keys = list(dict.dados.keys())
                return keys
    
    def print_data(self, objt):
        
        key_list = self.get_key(objt, 0, 1)
        zero_key = self.get_key(objt, 0)
        if zero_key == "CPF":
            for i in range(self.get_key(objt, 0, 0)):
                if (i>=0) and (i<3):
                    if i == 2:
                        print("Número da conta: ", objt.dados['n_conta'])
                    else:
                        print(f"{key_list[i]}: ", objt.dados[self.get_key(objt, i)])
            return
        if zero_key == "Nome":
            for i in range(self.get_key(objt, 0, 0)):
                if i != 4 and i != 1:
                    print(f"{key_list[i]}: ", objt.dados[self.get_key(objt, i)])
                if i == 1:
                    print("Data de nascimento:", objt.dados[self.get_key(objt, i)])
            return

    def verify_data(self, objt):
        #Função responsável por verificar se os dados inseridos são válidos
        #Se estiverem corretos ela apenas volta a tela inicial, caso o contrario, chama uma função parar corrigir os dados incorretos
        os.system('cls')
        negative = ['não', 'nao', 'n', 'nn', 'no', 'nop']
        positive = ['sim', 's', 'ss', 'yes', 'yep']
        print(text.CLIENT.VERIFY_DATA)
        self.print_data(objt)
        print(text.CLIENT.INCORRECT_DATA_)
        to_correct = input().lower()
        if to_correct in negative:
            text.functions.going_back()
            return
        elif to_correct in positive:
            keep_fixing = True
            show_twice = False
            while keep_fixing:
                if show_twice:
                    self.print_data(objt)
                    print("\n")
                print(text.CLIENT.INFO_TO_CORRECT)
                campo = input().title()
                self.call_correction(objt, campo)
                print(text.CLIENT.INFO_CORRECTED)
                sleep(1.5)
                os.system('cls')
                self.print_data(objt)
                print(text.CLIENT.ANOTHER_TO_CORRECT)
                still_wrong = input()
                if still_wrong in negative:
                    keep_fixing = False
                    text.functions.going_back()
                elif still_wrong in positive:
                    keep_fixing = True
                    show_twice = True
                    os.system('cls')
                else:
                    print(text.INVALID_OPTION)
                    
        return

    def call_correction(self, objt, campo):
        if campo == 'Nome':
            objt.criar_nome()
        elif campo == 'Data De Nascimento':
            objt.criar_data_nasc()
        elif campo == 'Cpf':
            objt.criar_cpf()
        elif campo == 'Endereço':
            objt.criar_endereco()
        return