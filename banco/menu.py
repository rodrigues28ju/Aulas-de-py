from decimal import Decimal
from conta_bancaria import ContaBancaria
from helpers import formatar_valor_monetario, obter_conta_por_cpf, exibir_menu_principal, exibir_extrato

contas = {}

def criar_conta():
    nome = input("Nome do titular: ")
    telefone = input("Telefone: ")
    cpf = input("CPF: ")
    endereco = input("Endereço: ")
    conta = ContaBancaria(nome, telefone, cpf, endereco)
    contas[cpf] = conta
    print(f"Conta criada com sucesso para {nome}.")

def depositar(cpf):
    valor = Decimal(input("Informe o valor a ser depositado: "))
    conta = obter_conta_por_cpf(contas, cpf)
    if conta:
        conta.depositar(valor)
        print(f"Depósito de {formatar_valor_monetario(valor)} realizado com sucesso.")  
    else:
        print("Conta não encontrada.")

def sacar(cpf):
    valor = Decimal(input("Informe o valor a ser sacado: "))
    conta = obter_conta_por_cpf(contas, cpf)
    if conta:
        conta.sacar(valor)
        print("Saque realizado com sucesso.")
    else:
        print("Conta não encontrada.")

def transferir(cpf_origem, cpf_destino):
    valor = Decimal(input("Informe o valor a ser transferido: "))
    conta_origem = obter_conta_por_cpf(contas, cpf_origem)
    conta_destino = obter_conta_por_cpf(contas, cpf_destino)
    
    if conta_origem and conta_destino:
        conta_origem.transferir(conta_destino, valor)
        print("Transferência realizada com sucesso.")
    else:
        print("Conta de origem ou conta de destino não encontrada.")

def menu_principal():
    while True:
        exibir_menu_principal()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criar_conta()
        elif opcao == '2':
            cpf = input("Informe o CPF da conta: ")
            depositar(cpf)
        elif opcao == '3':
            cpf = input("Informe o CPF da conta: ")
            sacar(cpf)
        elif opcao == '4':
            cpf_origem = input("Informe o CPF da conta de origem: ")
            cpf_destino = input("Informe o CPF da conta de destino: ")
            transferir(cpf_origem, cpf_destino)
        elif opcao == '5':
            cpf = input("Informe o CPF da conta: ")
            conta = obter_conta_por_cpf(contas, cpf)
            if conta:
                exibir_extrato(conta)
            else:
                print("Conta não encontrada.")
        elif opcao == '6':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()
