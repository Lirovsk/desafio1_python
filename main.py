from time import *
from os import *
MENU = '''
Seja Bem vindo ao novo sistema do banco!!
Selecione as opções abaixo conforme o que deseja utilizar hoje:
        Saque[1]
        Depósito[2]
        Extrato[3]
        Sair do sistema[4]
'''
MSG_SAQUE = '''Digite o valor desajado para o saque. 
Caso queira retornar ao menu sem realizar o saque, digite 'sair'.
'''
MSG_DEPOSITO = """Digite o valor desejado para o depósito.
"""
keep = True
while keep:
    lista_contas = []
    lista_clientes = []
    print("deseja adicionar um novo cliente?")
    resp = input()
    if resp == 'sim':
        from functions import *
        cliente = client()
        lista_clientes.append(cliente)
        print("Cliente adicionado com sucesso!")
    else:
        continue
    resp2 = input("Deseja adicionar uma nova conta para o cliente?")
    #tornar isso uma função para despoluir o código
    if resp2 == 'sim':
        cpf = input("Digite o número do cpf do cliente que deseja adicionar a conta")
        conta = bank(cpf, lista_contas)
        lista_contas.append(conta)
        print("Conta adicionada com sucesso!")
    print("para entrar emum conta digite primeiro seu cpf:")
    cpf = str(input())
    for i in lista_contas:
        if lista_clientes[i]['cpf'] == cpf:
            print(lista_clientes[i]['contas'])

            break
