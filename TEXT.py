import os
import time

class TEXTO:
    # Define default values for the constants
    WELCOME = ""
    MENU = ""
    ENTER_ATM = ""
    ENTER_CPF = ""
    ENTER_ACCOUNT = ""
    CLIENT_NOT_FOUND = ""
    ACCOUNT_NOT_FOUND = ""
    INVALID_OPTION = ""
    GOING_BACK = ""
    CLOSING_APP = ""

    class BANK:
        MENU = ""
        DEPOSIT = ""
        WITHDRAW = ""
        ABOVE_LIMIT = ""
        INVALID_VALUE = ""
        INSUFFICIENT_FUNDS = ""
        WITHDRAW_SUCCESS = ""
        DEPOSIT_SUCCESS = ""
        EXTRATO = ""
        ENTER_CPF_FOR_ACCOUNT = ""
        ACCOUNT_ADDED = ""
        PRESS_TO_CLEAR = ""

    class CLIENT:
        ADD_NAME = ""
        ADD_BIRTH = ""
        ADD_CPF = ""
        ADD_ADDRESS = ""
        ADD_CLIENT = ""
        CLIENT_ADDED = ""
        VERIFY_DATA = ""
        INCORRECT_DATA_ = ""
        INFO_TO_CORRECT = ""
        INFO_CORRECTED = ""
        ANOTHER_TO_CORRECT = ""

    def __init__(self):
        self.option = input("""
Choose your language:
    1. English
    2. Português
    Type only the number: """)
        self.get_language(self.option)
    
    def get_language(self, variable):
        if variable == '1':
            TEXTO.WELCOME = """
/$$$$$$$                                                      /$$                 /$$       /$$                   
| $$__  $$                                                    | $$                | $$      |__/                   
| $$  \ $$  /$$$$$$  /$$$$$$$   /$$$$$$$  /$$$$$$         /$$$$$$$  /$$$$$$       | $$       /$$  /$$$$$$  /$$$$$$ 
| $$$$$$$  |____  $$| $$__  $$ /$$_____/ /$$__  $$       /$$__  $$ /$$__  $$      | $$      | $$ /$$__  $$|____  $$
| $$__  $$  /$$$$$$$| $$  \ $$| $$      | $$  \ $$      | $$  | $$| $$  \ $$      | $$      | $$| $$  \__/ /$$$$$$$
| $$  \ $$ /$$__  $$| $$  | $$| $$      | $$  | $$      | $$  | $$| $$  | $$      | $$      | $$| $$      /$$__  $$
| $$$$$$$/|  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$/      |  $$$$$$$|  $$$$$$/      | $$$$$$$$| $$| $$     |  $$$$$$$
|_______/  \_______/|__/  |__/ \_______/ \______/        \_______/ \______/       |________/|__/|__/      \_______/
"""
            TEXTO.MENU = """
Good morning, what would you like to do at the bank today? (to exit type 4)
1. Add client
2. Create account
3. Enter ATM
4. Exit
"""
            TEXTO.ENTER_ATM = "Do you want to enter the ATM?"
            TEXTO.ENTER_CPF = "Enter the CPF number"
            TEXTO.ENTER_ACCOUNT = "Enter the account number"
            TEXTO.CLIENT_NOT_FOUND = "Client not found"
            TEXTO.ACCOUNT_NOT_FOUND = "Account not found"
            TEXTO.INVALID_OPTION = "Invalid option"
            TEXTO.GOING_BACK = "Returning to the main menu"
            TEXTO.CLOSING_APP = "Closing application"

            TEXTO.BANK.MENU = """
ATM        
What would you like to do today? (to exit type 4)
1. Deposit
2. Withdraw
3. View statement
4. Exit
"""
            TEXTO.BANK.DEPOSIT = "Enter the deposit amount"
            TEXTO.BANK.WITHDRAW = "Enter the withdrawal amount"
            TEXTO.BANK.ABOVE_LIMIT = "Amount above the limit"
            TEXTO.BANK.INVALID_VALUE = "Invalid amount"
            TEXTO.BANK.INSUFFICIENT_FUNDS = "Insufficient funds"
            TEXTO.BANK.WITHDRAW_SUCCESS = "Withdrawal successful!"
            TEXTO.BANK.DEPOSIT_SUCCESS = "Deposit successful!"
            TEXTO.BANK.EXTRATO = "Bank statement: "
            TEXTO.BANK.ENTER_CPF_FOR_ACCOUNT = "Enter the CPF number of the client to add the account\n"
            TEXTO.BANK.ACCOUNT_ADDED = "Account added successfully!"
            TEXTO.BANK.PRESS_TO_CLEAR = "Press enter to clear this screen and return to the bank menu"

            TEXTO.CLIENT.ADD_NAME = "Enter the client's name: "
            TEXTO.CLIENT.ADD_BIRTH = "Enter the client's birth date: "
            TEXTO.CLIENT.ADD_CPF = "Enter the client's CPF: "
            TEXTO.CLIENT.ADD_ADDRESS = "Enter the client's address: "
            TEXTO.CLIENT.ADD_CLIENT = "Do you want to add a new client?\n"
            TEXTO.CLIENT.CLIENT_ADDED = "Client added successfully!"
            TEXTO.CLIENT.VERIFY_DATA = "Check below if the client's data is correct."
            TEXTO.CLIENT.INCORRECT_DATA_ = "\nIs any data incorrect?"
            TEXTO.CLIENT.INFO_TO_CORRECT = "Which data do you want to correct? (Write it as it appears above)"
            TEXTO.CLIENT.INFO_CORRECTED = "\nData corrected successfully!\n"
            TEXTO.CLIENT.ANOTHER_TO_CORRECT = "\nDo you want to correct any other data?"

        elif variable == '2':
            TEXTO.WELCOME = """ 
/$$$$$$$                                                      /$$                 /$$       /$$                   
| $$__  $$                                                    | $$                | $$      |__/                   
| $$  \ $$  /$$$$$$  /$$$$$$$   /$$$$$$$  /$$$$$$         /$$$$$$$  /$$$$$$       | $$       /$$  /$$$$$$  /$$$$$$ 
| $$$$$$$  |____  $$| $$__  $$ /$$_____/ /$$__  $$       /$$__  $$ /$$__  $$      | $$      | $$ /$$__  $$|____  $$
| $$__  $$  /$$$$$$$| $$  \ $$| $$      | $$  \ $$      | $$  | $$| $$  \ $$      | $$      | $$| $$  \__/ /$$$$$$$
| $$  \ $$ /$$__  $$| $$  | $$| $$      | $$  | $$      | $$  | $$| $$  | $$      | $$      | $$| $$      /$$__  $$
| $$$$$$$/|  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$/      |  $$$$$$$|  $$$$$$/      | $$$$$$$$| $$| $$     |  $$$$$$$
|_______/  \_______/|__/  |__/ \_______/ \______/        \_______/ \______/       |________/|__/|__/      \_______/
                                                                                                                   """
            TEXTO.MENU = """
Bom dia, o que o Senhor(a) deseja fazer no banco hoje? (para sair digite 4)
1. Adicionar cliente
2. Criar conta
3. Entrar no caixa eletrônico
4. Sair
"""
            TEXTO.ENTER_ATM = """Deseja entrar no caixa eletrônico?"""
            TEXTO.ENTER_CPF = """Digite o número do CPF"""
            TEXTO.ENTER_ACCOUNT = """Digite o número da conta"""
            TEXTO.CLIENT_NOT_FOUND = """Cliente não encontrado"""
            TEXTO.ACCOUNT_NOT_FOUND = """Conta não encontrada"""
            TEXTO.INVALID_OPTION = """Opção inválida"""
            TEXTO.GOING_BACK = "Voltando ao menu principal"
            TEXTO.CLOSING_APP = "Fechando aplicativo"

            TEXTO.BANK.MENU = """
CAIXA ELETRÔNICO        
O que deseja fazer Hoje? (para sair digite 4)
1. Depositar
2. Sacar
3. Ver extrato
4. Sair
"""
            TEXTO.BANK.DEPOSIT = """Digite o valor do depósito"""
            TEXTO.BANK.WITHDRAW = """Digite o valor do saque"""
            TEXTO.BANK.ABOVE_LIMIT = """Valor acima do limite"""
            TEXTO.BANK.INVALID_VALUE = """Valor inválido"""
            TEXTO.BANK.INSUFFICIENT_FUNDS = """Saldo insuficiente"""
            TEXTO.BANK.WITHDRAW_SUCCESS = """Saque realizado com sucesso!"""
            TEXTO.BANK.DEPOSIT_SUCCESS = """Depósito realizado com sucesso!"""
            TEXTO.BANK.EXTRATO = """Extrato bancário: """
            TEXTO.BANK.ENTER_CPF_FOR_ACCOUNT = """Digite o número do cpf do cliente que deseja adicionar a conta\n"""
            TEXTO.BANK.ACCOUNT_ADDED = """Conta adicionada com sucesso!"""
            TEXTO.BANK.PRESS_TO_CLEAR = """Pressione enter para apagar essa tela e voltar ao menu do banco"""

            TEXTO.CLIENT.ADD_NAME = """Digite o nome do cliente: """
            TEXTO.CLIENT.ADD_BIRTH = """Digite a data de nascimento do cliente: """
            TEXTO.CLIENT.ADD_CPF = """Digite o CPF do cliente: """
            TEXTO.CLIENT.ADD_ADDRESS = """Digite o endereço do cliente: """
            TEXTO.CLIENT.ADD_CLIENT = """Deseja adicionar um novo cliente?\n"""
            TEXTO.CLIENT.CLIENT_ADDED = """Cliente adicionado com sucesso!
"""
            TEXTO.CLIENT.VERIFY_DATA = """Verifique abaixo se os dados do cliente estão corretos."""
            TEXTO.CLIENT.INCORRECT_DATA_ = """\nAlgun dado esta incorreto?"""
            TEXTO.CLIENT.INFO_TO_CORRECT = """Qual dado deseja corrigir? (Escreva-o assim como aparece acima)"""
            TEXTO.CLIENT.INFO_CORRECTED = """\nDado corrigido com sucesso!\n"""
            TEXTO.CLIENT.ANOTHER_TO_CORRECT = """\nDeseja corrigir mais algum dado?"""

    class functions:    
        @staticmethod
        def going_back():
            print(TEXTO.GOING_BACK, end='', flush=True)
            for i in range(3):
                print('.', end='', flush=True)
                time.sleep(0.5)
            os.system('cls')
            return
            
        @staticmethod
        def closing_app():
            print(TEXTO.CLOSING_APP, end='', flush=True)
            for i in range(3):
                print('.', end='', flush=True)
                time.sleep(0.8)
            os.system('cls')
            return


