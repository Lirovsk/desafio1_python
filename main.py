from time import *
from os import *
from functions import *

add = adding()
lista_contas = []
list_clientes = []
keep = True
while keep:
    print("o que deseja fazer hoje no banco?")
    print("1.add cliente, 2 criar contas")
    resp = input()
    if resp == '1':
        add.add_cliente(list_clientes)
    elif resp == '2':
        add.add_conta(lista_contas, list_clientes)
    
    for i in range(len(list_clientes)):
        print(list_clientes[i].dados)
    
    for i in range(len(lista_contas)):
        print(lista_contas[i].dados)