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
Bom dia, o que o Senhor(a) deseja fazer no banco hoje?
1. Adicionar cliente
2. Criar conta
3. Entrar no caixa eletrônico
4. Sair
"""
    ENTER_ATM = """Deseja entrar no caixa eletrônico?"""
    ENTER_CPF = """Digite o número do CPF"""
    ENTER_ACCOUNT = """Digite o número da conta"""
    CLIENT_NOT_FOUND = """Cliente não encontrado"""
    ACCOUNT_NOT_FOUND = """Conta não encontrada"""
    class BANK:
        MENU = """
O que deseja fazer Hoje?
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
        DEPOSIT_SUCCESS = """Depósito realizado com sucesso!"""
        EXTRATO = """Extrato bancário: """
    
    class CLIENT:
        ADD_NAME = """Digite o nome do cliente: """
        ADD_BIRTH = """Digite a data de nascimento do cliente: """
        ADD_CPF = """Digite o CPF do cliente: """
        ADD_ADDRESS = """Digite o endereço do cliente: """