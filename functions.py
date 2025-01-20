from time import *
import os

class bank_actions:
    __LMT_S_OP = 500
    __LMT_S_D = 3
    
    def saque(self,*, valor_saque, valor_conta, extrato):
        #nessa função ainda precisarei implementar a chamada do extrato, os textos de erro
        #textos de guis para os usuários, tratamento de erro por limite de operações diárias e tempo de resposta
        float(valor_saque)
        float(valor_conta)
        if valor_saque > self.__LMT_S_OP or valor_saque> valor_conta:
            print("Transação não autorizada")
            return
        else:
            valor_conta = valor_conta - valor_saque
            return [valor_conta, ['saque', valor_saque]]
    
    def deposito(self, valor_deposito, valor_conta):
        float(valor_deposito)
        float(valor_conta)
        if valor_deposito > 0:
            valor_conta = valor_conta + valor_deposito
            return [valor_conta, ['deposito', valor_deposito]]
        else:
            print("Transação não autorizada")
            return
    
    def extrato(self, saldo, * extrato):
        for i in extrato:
            print(i)
        print(f"Saldo atual: R${saldo:.2f}")
        return
    
class client:
    def __init__(self):
        self.dados={
            'nome': '',
            'data_nasc': '',
            'cpf': '',
            'endereço': '',
            'contas': []
        }
        self.criar_nome(self)
        self.criar_data_nasc(self)
        self.criar_cpf(self)
        self.criar_endereco(self)

    def criar_nome(self):
        nome = input("Digite o nome do cliente: ")
        self.dados['nome'] = nome
        return
    
    def criar_data_nasc(self):
        data_nasc = input("Digite a data de nascimento do cliente: ")
        self.dados['data_nasc'] = data_nasc
        return
    
    def criar_cpf(self):
        cpf = input("Digite o CPF do cliente: ")
        self.dados['cpf'] = cpf
        return
    
    def criar_endereco(self):
        endereco = input("Digite o endereço do cliente: ")
        self.dados['endereço'] = endereco
        return
    
class bank:
    def __init__(self, cpf, lista_contas):
        #tranformar isso em um dicionário
        self.dados = {
            'cpf': cpf,
            'AGENCIA': '0001',
            'n_conta': self.criar_n_conta(lista_contas),
            'saldo': 1500,
            'extrato': [],
            'lmt_d': 0
        }
       

    def criar_n_conta(self, lista_contas):
        if len(lista_contas) == 0:
            self.n_conta = 1
        else:
            self.n_conta = lista_contas[-1]['n_conta'] + 1
        return self.n_conta
