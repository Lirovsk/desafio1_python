from time import *
import os
import time


class bank_actions:
    __LMT_S_OP = 500
    __LMT_S_D = 3
    
    def saque(self, valor, conta):
        valor = float(valor)
        if valor > self.__LMT_S_OP:
            print("Valor acima do limite permitido")
            return
        elif valor <= 0:
            print("Valor inválido")
            return
        else:
            if conta.dados['saldo'] < valor:
                print("Saldo insuficiente")
                return
            else:
                conta.dados['saldo'] -= valor
                conta.dados['extrato'].append([f"Saque no valor de R${valor:.2f}", time.ctime()])
                conta.dados['lmt_d'] += 1
                print("Saque realizado com sucesso!")
                return
            
    def deposito(self, valor, conta):
        valor = float(valor)
        if valor <= 0:
            print("Valor inválido")
            return
        else:
            conta.dados['saldo'] += valor
            conta.dados['extrato'].append([f"Depósito no valor de R${valor:.2f}", time.ctime()])
            print("Depósito realizado com sucesso!")
            return
    
    def extrato(self, conta):
        print("Extrato bancário: ")
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
        nome = input("Digite o nome do cliente: ")
        self.dados['Nome'] = nome
        return
    
    def criar_data_nasc(self):
        data_nasc = input("Digite a data de nascimento do cliente: ")
        self.dados['data_nasc'] = data_nasc
        return
    
    def criar_cpf(self):
        cpf = input("Digite o CPF do cliente: ")
        self.dados['CPF'] = cpf
        return
    
    def criar_endereco(self):
        endereco = input("Digite o endereço do cliente: ")
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
        for i in range(len(lista_clientes)):
            if lista_clientes[i].dados['CPF'] == cpf:
                a = 1
                return lista_clientes[i]
                
        if a != 1: 
            print("Cliente não encontrado")
            return
    
    def search_n_conta(self, n_conta, lista_contas):
        #search for a bank account in the list of bank accounts by account number
        n_conta = int(n_conta)
        for i in range(len(lista_contas)):
            if lista_contas[i].dados['n_conta'] == n_conta:
                return lista_contas[i]
            else:
                print("Conta não encontrada")
                return

class process:
    #Classe responsável por funções de processsamento, aquisição e impressão de dados inerentes ao funcionamento do banco
    def add_cliente(self, lista_clientes):
        #add a new client to the list of clients
        answer = input("Deseja adicionar um novo cliente?\n")
        if answer == 'sim':
            cliente = client()
            lista_clientes.append(cliente)
            print("Cliente adicionado com sucesso!\n")
            sleep(1.)
            self.verify_data(cliente)
        return

    def add_conta(self, lista_contas, lista_clientes):
        #create a bank account to a client and add it to the list of bank accounts
        cpf = input("Digite o número do cpf do cliente que deseja adicionar a conta\n")
        conta = bank(cpf, lista_contas)
        lista_contas.append(conta)
        #adding the account number to the client's account list
        n_conta = conta.dados['n_conta']
        serc = search()
        cliente = serc.search_client(cpf, lista_clientes)
        if cliente != None:
            cliente.dados['contas'].append(n_conta)
        print("Conta adicionada com sucesso!")
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
        print("Verifique abaixo se os dados do cliente estão corretos.")
        self.print_data(objt)
        print("\nAlgun dado esta incorreto?")
        to_correct = input()
        if to_correct in negative:
            print("Voltando ao menu pirncipal", end = '', flush=True)
            for i in range(3):
                print(".", end = '', flush=True)
                sleep(0.5)
            os.system('cls')
            return
        elif to_correct in positive:
            keep_fixing = True
            show_twice = False
            while keep_fixing:
                if show_twice:
                    self.print_data(objt)
                    print("\n")
                print("Qual dado deseja corrigir? (Escreva-o assim como aparece acima)")
                campo = input().title()
                self.call_correction(objt, campo)
                print("\nDado corrigio com sucesso!\n")
                sleep(1.5)
                os.system('cls')
                self.print_data(objt)
                print("\nDeseja corrigir mais algum dado?")
                still_wrong = input()
                if still_wrong in negative:
                    keep_fixing = False
                    print("Voltando ao menu pirncipal", end = '', flush=True)
                    for i in range(3):
                        print(".", end = '', flush=True)
                        sleep(0.5)
                    os.system('cls')
                elif still_wrong in positive:
                    keep_fixing = True
                    show_twice = True
                    os.system('cls')
                else:
                    print("Opção inválida")
                    
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