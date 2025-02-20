from services import *
from TEXT import *
import os

text = TEXTO()
lista_clientes = []
lista_contas = []

def bank_loop():
    #define this function
    print(text.BANK.CLIENT_CPF)
    cpf = input()
    time_client = search_client(cpf, lista_clientes)
    print(text.BANK.WHICH_ACCOUNT)
    print(time_client._count[0]._count)
    account = input()
    conta = search_count(account, time_client._count)

    while True:
        print(text.BANK.MENU)
        option = input()
        if option == "1":
            print(text.BANK.DEPOSIT)
        elif option == "2":
            print(text.BANK.WITHDRAW)
        elif option == "3":
            print(text.BANK.EXTRATO)
        elif option == "4":
            going_back()
            break


def main():
    while True:
        print(text.WELCOME)
        print(text.MENU)
        option = input()
        if option == "1":
            print(text.ENTER_ADD_CLIENT)
            option = input()
            if option in ["s", "S", "sim", "Sim", "SIM"]:
                lista_clientes.append(adding_client())
                going_back()
            else:
                going_back()
            pass
        elif option == "2":
            print(text.ENTER_ADD_ACCOUNT)
            option = input()
            if option in ["s", "S", "sim", "Sim", "SIM"]:
                print(text.ENTER_CPF_FOR_ACCOUNT)
                cpf = input()
                cliente = search_client(cpf, lista_clientes)
                new_account = conta_corrente.new_account(cliente, lista_contas)
                lista_contas.append(new_account._count)
                cliente._count.append(new_account)
                print(text.BANK.ACCOUNT_ADDED)
                going_back()

            else:
                going_back()

        elif option == "3":
            print(text.ENTER_ATM)
            option = input()
            if option in ["s", "S", "sim", "Sim", "SIM"]:
                bank_loop()

            else:
                going_back()

        elif option == "4":
            closing_app()
            break

        else:
            print(text.INVALID_OPTION)
            os.system('cls')

main()