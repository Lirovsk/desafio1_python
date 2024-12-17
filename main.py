from time import *

menu = '''
Seja Bem vindo ao novo sistema do banco!!
Selecione as opções abaixo conforme o que deseja utilizar hoje:
        Saque[1]
        Depósito[2]
        Extrato[3]
        Sair do sistema[4]
'''
msg_saque = '''Digite o valor desajado para o saque. 
Caso queira retornar ao menu sem realizar o saque, digite 'sair'.
'''

LMT_S_D = 3
LMT_S_OP = 500
extrato = []
valor_conta = 1500
lmt_usado = 0
tempo = 0.5

while True:
    opcao = input(menu)
    if int(opcao) == 1:
        if lmt_usado < LMT_S_D:    
            valor_saque = input(msg_saque)
            
            if valor_saque != 'sair' and float(valor_saque)>=0:
                if float(valor_saque) <= LMT_S_OP and float(valor_saque) <= valor_conta:
                    valor_conta = valor_conta - float(valor_saque)
                    extrato.append(['saque', str(valor_saque)])
                    lmt_usado += 1
                    sleep(tempo)
                    print("operação concluída")
                    sleep(tempo)                    

                elif float(valor_saque) > 500:
                    sleep(tempo)
                    print("\n")
                    print("O valor inserido é maior que o permitido para essa operação")
                    sleep(tempo)
                    continue

                else :
                    continue
            else:
                print("valor ")

        else:
            sleep(tempo)
            print("Valor limite de saques por dia atingido")
            sleep(tempo)

    elif int(opcao) ==2:
        pass
    elif int(opcao) == 3:
        pass
    elif int(opcao) == 4:
        break
    else:
        print("Opção inválida, selecione outra opção do menu.")
        print("Caso queira sair, pressione 4.")
    sleep(tempo)
    