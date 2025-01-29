from time import *
from os import *
from functions import *
from TEXT import *

procss = process()
text = TEXTO()
bank_ = bank_actions()
src = search()
lista_contas = []
list_clientes = []
keep = True

def bank_loop():
    os.system('cls')
    print(text.ENTER_CPF)
    cpf = input()
    cliente = src.search_client(cpf, list_clientes)
    if cliente == None:
        print(text.CLIENT_NOT_FOUND)
        return
    print(text.ENTER_ACCOUNT)
    number = input()
    conta = src.search_n_conta(number, lista_contas)
    os.system('cls')
    while True:
        print(text.WELCOME)
        print(text.BANK.MENU)
        action = input()
        if action == '1':
            os.system('cls')
            print(text.WELCOME)
            print(text.BANK.DEPOSIT)
            value = input()
            bank_.deposito(value, conta)
            sleep(0.8)
            text.functions.going_back()
        elif action == '2':
            os.system('cls')
            print(text.WELCOME)
            print(text.BANK.WITHDRAW)
            value = input()
            bank_.saque(value, conta)
            sleep(0.8)
            text.functions.going_back()
        elif action == '3':
            os.system('cls')
            print(text.WELCOME)
            bank_.extrato(conta)
            print(text.BANK.PRESS_TO_CLEAR)
            input()
            os.system('cls')
        elif action == '4':
            text.functions.going_back()
            break
    pass

while keep:
    print(text.WELCOME)
    print(text.MENU)
    answer = input()
    if answer == '1':
        os.system('cls')
        print(text.WELCOME)
        procss.add_cliente(list_clientes)
    elif answer == '2':
        os.system('cls')
        print(text.WELCOME)
        procss.add_conta(lista_contas, list_clientes)
    elif answer == '3':
        bank_loop()
    elif answer == '4':
        keep = False
        text.functions.closing_app()
