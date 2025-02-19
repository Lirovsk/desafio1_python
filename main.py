from services import *
from TEXT import *
import os

text = TEXTO()
lista_clientes = []
lista_contas = []

def bank_loop():
    pass

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
                text.functions.going_back()
            else:
                text.functions.going_back()
            pass
        elif option == "2":
            print(text.ENTER_ADD_ACCOUNT)
            option = input()
            if option in ["s", "S", "sim", "Sim", "SIM"]:
                cliente = conta_corrente.new_account(cliente, lista_contas)
                pass
            else:
                text.functions.going_back()
        elif option == "3":
            print(text.ENTER_ATM)
            option = input()
            if option in ["s", "S", "sim", "Sim", "SIM"]:
                bank_loop()
                text.functions.going_back()
            else:
                text.functions.going_back()
        elif option == "4":
            text.functions.closing_app()
            break
        else:
            print(text.INVALID_OPTION)
            os.system('cls')

main()