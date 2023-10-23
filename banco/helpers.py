from decimal import Decimal

def obter_conta_por_cpf(contas, cpf):
    if cpf in contas:
        return contas[cpf]
    return None

def formatar_valor_monetario(valor):
    return f'R$ {valor:.2f}'

def exibir_menu_principal():
    print("\n===== MENU PRINCIPAL =====")
    print("1. Criar Conta")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Transferir")
    print("5. Visualizar Extrato")
    print("6. Sair")

def exibir_extrato(conta):
    print(f"Extrato para {conta.nome}:")
    for movimento in conta.extrato:
        print(movimento)
    print(f'Saldo atual: {formatar_valor_monetario(conta.saldo)}')
