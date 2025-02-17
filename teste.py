from time import *
from os import *
from services import *
from TEXT import *

procss = process()
src = search()
texto =TEXTO()

lista_contas = []
list_clientes = []
keep = True
print(texto.WELCOME)
while keep:
    print(texto.MENU)
    resp = input()
    if resp == '1':
        procss.add_cliente(list_clientes)
    elif resp == '2':
        procss.add_conta(lista_contas, list_clientes)
    
    for i in range(len(list_clientes)):
        procss.print_data(list_clientes[i])
        print(list_clientes[i].dados)
    for i in range(len(lista_contas)):
        procss.print_data(lista_contas[i])
        print(lista_contas[i].dados)
    print(texto.ENTER_ATM)
    resp = input()
    os.system('cls')
    if resp == 'sim':
        bank_ = bank_actions()
        print(texto.ENTER_CPF)
        cpf = input()
        cliente = src.search_client(cpf, list_clientes)
        if cliente == None:
            print(texto.CLIENT_NOT_FOUND)
            break
            
        print(texto.ENTER_ACCOUNT)
        number = input()
        conta = src.search_n_conta(number, lista_contas)
        while True:
            print(texto.BANK.MENU)
            action = input()
            if action == '1':
                print(texto.BANK.DEPOSIT)
                value = input()
                bank_.deposito(value, conta)
            elif action == '2':
                print(texto.BANK.WITHDRAW)
                value = input()
                bank_.saque(value, conta)
            elif action == '3':
                bank_.extrato(conta)
            elif action == '4':
                break

