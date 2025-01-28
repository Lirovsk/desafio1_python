from time import *
from os import *
from functions import *

procss = process()
lista_contas = []
list_clientes = []
keep = True
while keep:
    print("o que deseja fazer hoje no banco?")
    print("1.add cliente, 2 criar contas")
    resp = input()
    if resp == '1':
        procss.add_cliente(list_clientes)
    elif resp == '2':
        procss.add_conta(lista_contas, list_clientes)
    
    for i in range(len(list_clientes)):
        procss.print_data(list_clientes[i])
        print("\n")
    for i in range(len(lista_contas)):
        procss.print_data(lista_contas[i])
        