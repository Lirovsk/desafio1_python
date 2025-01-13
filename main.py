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

LMT_S_D = 3
LMT_S_OP = 500
extrato = []
valor_conta = 1500
lmt_usado = 0
tempo = 0.5

while True:
    opcao = input(MENU)
    if int(opcao) == 1:
        if lmt_usado < LMT_S_D:    
            valor_saque = input(MSG_SAQUE)
            
            if valor_saque != 'sair' and float(valor_saque)>=0:
                if float(valor_saque) <= LMT_S_OP and float(valor_saque) <= valor_conta:
                    valor_conta = valor_conta - float(valor_saque)
                    extrato.append(['saque', float(valor_saque)])
                    lmt_usado += 1
                    sleep(tempo)
                    print("operação concluída")
                    sleep(tempo)                    

                elif float(valor_saque) > LMT_S_OP:
                    sleep(tempo)
                    print("\n")
                    print("O valor inserido é maior que o permitido para essa operação")
                    sleep(tempo)
                    continue
                
                else :
                    continue
            elif valor_saque == 'sair':
                continue
            else:
                sleep(tempo)
                print("Valor inválido")
                sleep(tempo)

        else:
            sleep(tempo)
            print("Valor limite de saques por dia atingido")
            sleep(tempo)

    elif int(opcao) ==2:
        valor_deposito = input(MSG_DEPOSITO)
        if float(valor_deposito) > 0:
            valor_conta = valor_conta + float(valor_deposito)
            extrato.append(['deposito', float(valor_deposito)])
            sleep(tempo)
            print("operação concluída")
            sleep(tempo)
        else:
            sleep(tempo)
            print("Valor inválido")
            sleep(tempo)

    elif int(opcao) == 3:
        if extrato == []:
            system('cls')
            sleep(tempo)
            print("Extrato vazio")
            system("cls")
            sleep(tempo)
        else:    
            system('cls')
            print("Extrato completo:\n\n")
            for i in range(len(extrato)):
                print(f"Operação: {extrato[i][0]} | Valor: R${extrato[i][1]:.2f}\n\n")
            print(f"Saldo atual: R${valor_conta:.2f}")
            input("Pressione uma tecla para fechar a exibição do estrato")
            system('cls')

    elif int(opcao) == 4:
        break
    else:
        print("Opção inválida, selecione outra opção do MENU.")
        print("Caso queira sair, pressione 4.")
    sleep(tempo)
    