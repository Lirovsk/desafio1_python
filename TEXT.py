import os
import time

class TEXTO:
    WELCOME = """ 
/$$$$$$$                                                      /$$                 /$$       /$$                   
| $$__  $$                                                    | $$                | $$      |__/                   
| $$  \ $$  /$$$$$$  /$$$$$$$   /$$$$$$$  /$$$$$$         /$$$$$$$  /$$$$$$       | $$       /$$  /$$$$$$  /$$$$$$ 
| $$$$$$$  |____  $$| $$__  $$ /$$_____/ /$$__  $$       /$$__  $$ /$$__  $$      | $$      | $$ /$$__  $$|____  $$
| $$__  $$  /$$$$$$$| $$  \ $$| $$      | $$  \ $$      | $$  | $$| $$  \ $$      | $$      | $$| $$  \__/ /$$$$$$$
| $$  \ $$ /$$__  $$| $$  | $$| $$      | $$  | $$      | $$  | $$| $$  | $$      | $$      | $$| $$      /$$__  $$
| $$$$$$$/|  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$/      |  $$$$$$$|  $$$$$$/      | $$$$$$$$| $$| $$     |  $$$$$$$
|_______/  \_______/|__/  |__/ \_______/ \______/        \_______/ \______/       |________/|__/|__/      \_______/
                                                                                                                   """
    MENU = """
Bom dia, o que o Senhor(a) deseja fazer no banco hoje? (para sair digite 4)
1. Adicionar cliente
2. Criar conta
3. Entrar no caixa eletrônico
4. Sair
"""
    ENTER_ATM = """Deseja entrar no caixa eletrônico?"""
    ENTER_ADD_CLIENT = """Deseja mesmo adicionar um cliente?"""
    ENTER_ADD_ACCOUNT = """Deseja mesmo adicionar uma conta?"""
    ENTER_CPF = """Digite o número do CPF"""
    ENTER_ACCOUNT = """Digite o número da conta"""
    CLIENT_NOT_FOUND = """Cliente não encontrado"""
    ACCOUNT_NOT_FOUND = """Conta não encontrada"""
    INVALID_OPTION = """Opção inválida"""
    GOING_BACK = "Voltando ao menu principal"
    ENTER_CPF_FOR_ACCOUNT = """Digite o número do cpf do cliente que deseja adicionar a conta\n"""
    
    class BANK:
        MENU = """
CAIXA ELETRÔNICO        
O que deseja fazer Hoje? (para sair digite 4)
1. Depositar
2. Sacar
3. Ver extrato
4. Sair
"""
        DEPOSIT = """Digite o valor do depósito"""
        WITHDRAW = """Digite o valor do saque"""
        ABOVE_LIMIT = """Valor acima do limite"""
        INVALID_VALUE = """Valor inválido"""
        INSUFFICIENT_FUNDS = """Saldo insuficiente"""
        WITHDRAW_SUCCESS = """Saque realizado com sucesso!"""
        WITHDRAW_LIMIT_EXCEEDED = """Limite de saques excedido!"""
        DEPOSIT_SUCCESS = """Depósito realizado com sucesso!"""
        EXTRATO = """Extrato bancário: """
        CLIENT_CPF = """Digite o CPF do cliente"""
        WHICH_ACCOUNT = """Qual conta deseja acessar?"""
        ACCOUNT_ADDED = """Conta adicionada com sucesso!"""
        PRESS_TO_CLEAR = """Pressione enter para apagar essa tela e voltar ao menu do banco"""

    class CLIENT:
        ADD_NAME = """Digite o nome do cliente: """
        ADD_BIRTH = """Digite a data de nascimento do cliente: """
        ADD_CPF = """Digite o CPF do cliente: """
        ADD_ADDRESS = """Digite o endereço do cliente: """
        ADD_CLIENT = """Deseja adicionar um novo cliente?\n"""
        CLIENT_ADDED = """Cliente adicionado com sucesso!
        """
        VERIFY_DATA = """Verifique abaixo se os dados do cliente estão corretos."""
        INCORRECT_DATA_ = """\nAlgun dado esta incorreto?"""
        INFO_TO_CORRECT = """Qual dado deseja corrigir? (Escreva-o assim como aparece acima)"""
        INFO_CORRECTED = """\nDado corrigido com sucesso!\n"""
        ANOTHER_TO_CORRECT = """\nDeseja corrigir mais algum dado?"""
    
    
def going_back():
    print(TEXTO.GOING_BACK, end='', flush=True)
    for i in range(3):
        print('.', end='', flush=True)
        time.sleep(0.5)
    os.system('cls')
    return
        
def closing_app():
    print("Fechando aplicativo", end='', flush=True)
    for i in range(3):
        print('.', end='', flush=True)
        time.sleep(0.8)
    os.system('cls')
    return